from flask import Flask, jsonify, request

from todo.model.task import TaskSchema
from todo.model.completed import CompletedTask, CompletedTaskSchema
from todo.model.uncompleted import UncompletedTask, UncompletedTaskSchema
from todo.model.task_type import TaskType
from todo.cache import TaskCache

app = Flask(__name__)

tasks = TaskCache()


# Adding sample tasks
sampleTasks = [
    CompletedTask('Get Groceries'),
    CompletedTask('Call David'),
    UncompletedTask('Get Dentist Appointment'),
    UncompletedTask('Pay Mobile Bill')
]
for t in sampleTasks:
    key, value = t.description, t
    print(key, value)
    tasks.put(key, value)



@app.route('/all-tasks')
def get_all_tasks():
    schema = TaskSchema(many=True)
    allTasks = tasks.toList(allowedTypes = [TaskType.COMPLETED, TaskType.UNCOMPLETED])
    allTasks = schema.dump( allTasks )
    return jsonify(allTasks.data)


@app.route('/completed-tasks')
def get_completed_tasks():
    schema = CompletedTaskSchema(many=True)
    completedTasks = tasks.toList(allowedTypes = [TaskType.COMPLETED])
    completedTasks = schema.dump(completedTasks)
    return jsonify(completedTasks.data)


@app.route('/uncompleted-tasks')
def get_uncompleted_tasks():
    schema = UncompletedTaskSchema(many=True)
    uncompletedTasks = tasks.toList(allowedTypes = [TaskType.UNCOMPLETED])    
    uncompletedTasks = schema.dump(uncompletedTasks)
    return jsonify(uncompletedTasks.data)


@app.route('/add-new-task', methods=['POST'])
def add_new_tasks():
    newTask = UncompletedTaskSchema().load(request.get_json())
    key, value = newTask.data.description, newTask.data
    if not tasks.contains(key):
        tasks.put(key, value)
    elif tasks.get(key).val.type == TaskType.COMPLETED:
        node = tasks.get(key)
        node.val = value
    return "", 204

@app.route('/mark-task-as-completed', methods=['POST'])
def mark_task_as_completed():
    completedTask = CompletedTaskSchema().load(request.get_json())
    key, value = completedTask.data.description, completedTask.data
    if tasks.contains(key) and tasks.get(key).val.type == TaskType.UNCOMPLETED:
        node = tasks.get(key)
        node.val = value
    return "", 204


@app.route('/delete-task', methods=['DELETE'])
def delete_tasks():
    task = TaskSchema().load(request.get_json())
    key = task.data["description"]
    tasks.remove(key)
    return "", 204


if __name__ == "__main__":
    app.run()
