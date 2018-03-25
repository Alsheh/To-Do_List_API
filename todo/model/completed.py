from marshmallow import post_load

from .task import Task, TaskSchema
from .task_type import TaskType


class CompletedTask(Task):
  def __init__(self, description):
    super(CompletedTask, self).__init__(description, TaskType.COMPLETED)

  def __repr__(self):
    return '<CompletedTask(name={self.description!r})>'.format(self=self)


class CompletedTaskSchema(TaskSchema):
  @post_load
  def make_completed_task(self, data):
    return CompletedTask(**data)
