from flask import Flask, jsonify, request
from pymongo import MongoClient
import datetime

from todo.model.task import TaskSchema
from todo.model.completed import CompletedTask, CompletedTaskSchema
from todo.model.uncompleted import UncompletedTask, UncompletedTaskSchema
from todo.model.task_type import TaskType

app = Flask(__name__)
client = MongoClient()
db = client.todo_database
tasks = db.tasks


@app.route('/all-tasks')
def get_all_tasks():
    schema = TaskSchema(many=True)
    allTasks = schema.dump( tasks.find({}, {'_id': False}) )
    return jsonify(allTasks.data)



@app.route('/completed-tasks')
def get_completed_tasks():
    schema = CompletedTaskSchema(many=True)
    completedTasks = tasks.find({"type": str(TaskType.COMPLETED)}, {'_id': False})
    completedTasks = schema.dump(completedTasks)
    return jsonify(completedTasks.data)



@app.route('/uncompleted-tasks')
def get_uncompleted_tasks():
    schema = UncompletedTaskSchema(many=True)
    uncompletedTasks = tasks.find({"type": str(TaskType.UNCOMPLETED)}, {'_id': False})
    uncompletedTasks = schema.dump(uncompletedTasks)
    return jsonify(uncompletedTasks.data)



@app.route('/add-new-task', methods=['POST'])
def add_new_tasks():
    newTask = UncompletedTaskSchema().load(request.get_json()).data
    data = newTask.get_dict()
    task = tasks.find({"description": data["description"]})
    if task.count() == 0:
        tasks.insert_one(data)
    elif task[0]["type"] == str(TaskType.COMPLETED):
        tasks.remove({"description": data["description"]})
        tasks.insert_one(data)
    return "", 204


@app.route('/mark-task-as-completed', methods=['POST'])
def mark_task_as_completed():
    completedTask = CompletedTaskSchema().load(request.get_json()).data
    data = completedTask.get_dict()
    task = tasks.find({"description": data["description"]})
    if task.count() > 0 and task[0]["type"] == str(TaskType.UNCOMPLETED):
        tasks.remove({"description": data["description"]})
        tasks.insert_one(data)
    return "", 204



@app.route('/delete-task', methods=['DELETE'])
def delete_tasks():
    task = TaskSchema().load(request.get_json()).data
    tasks.remove({"description": task["description"]})
    return "", 204



if __name__ == "__main__":
    app.run()
