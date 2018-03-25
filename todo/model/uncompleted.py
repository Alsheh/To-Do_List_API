from marshmallow import post_load

from .task import Task, TaskSchema
from .task_type import TaskType


class UncompletedTask(Task):
  def __init__(self, description):
    super(UncompletedTask, self).__init__(description, TaskType.UNCOMPLETED)

  def __repr__(self):
    return '<UncompletedTask(name={self.description!r})>'.format(self=self)


class UncompletedTaskSchema(TaskSchema):
  @post_load
  def make_uncompleted_task(self, data):
    return UncompletedTask(**data)
