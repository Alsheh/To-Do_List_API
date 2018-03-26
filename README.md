# To-Do List API
This to-do list API provides the following functionalities:
* Adding a new task.
* Marking an exiting task as completed.
* Deleting an existing task.
* Retrieving all tasks, completed and uncompleted.
* Retrieving completed tasks.
* Retrieving uncompleted tasks.

## Docker
To build and run a docker image:<br>
~~~
docker-compose up
~~~

## Interaction with the API (locally)

1. <b>Adding a new task:</b> <br>
      Request:<br>
      ~~~~
      curl -X POST -H "Content-Type: application/json" -d '{
          "description": "<New Task>"
      }' http://localhost:5000/add-new-task 
      ~~~~
      Respose:<br>
      `204`

2. <b>Marking an exiting task as completed:</b> <br>
      Request:
      ~~~ 
      curl -X POST -H "Content-Type: application/json" -d '{
          "description": "<Task Name>"
      }' http://localhost:5000/mark-task-as-completed
      ~~~~
      Respose:<br>
      `204`

3. <b>Deleting an existing task:</b> <br>
      Request:
      ~~~
      curl -X DELETE -H "Content-Type: application/json" -d '{
          "description": "<Task Name>"
      }' http://localhost:5000/delete-task
      ~~~
      Respose:<br>
      `204`        

4. <b>Retrieving all tasks:</b> <br>
      Request:
      ~~~~
      curl http://localhost:5000/all-tasks
      ~~~~
      Respose:(sample response)<br>
      ~~~
      [
        {
          "created_at": "2018-03-23T01:50:16.016712", 
          "description": "Task#1", 
          "type": "COMPLETED"
        }, 
        {
          "created_at": "2018-03-23T01:50:16.016717", 
          "description": "Task#2", 
          "type": "UNCOMPLETED"
        }, 
        ...
      ]
      ~~~
      
5. <b>Retrieving completed tasks:</b> <br>
      Request:
      ~~~~
      curl http://localhost:5000/completed-tasks
      ~~~~
      Respose:(sample response)<br>
      ~~~
      [
        {
          "created_at": "2018-03-23T01:50:16.016712", 
          "description": "Task#1", 
          "type": "COMPLETED"
        }, 
        ...
      ]
      ~~~
6. <b>Retrieving uncompleted tasks:</b> <br>
      Request:
      ~~~~
      curl http://localhost:5000/uncompleted-tasks
      ~~~~
      Respose:(sample response)<br>
      ~~~
      [
        {
          "created_at": "2018-03-23T01:50:16.016717", 
          "description": "Task#2", 
          "type": "UNCOMPLETED"
        }, 
        ...
      ]
      ~~~
