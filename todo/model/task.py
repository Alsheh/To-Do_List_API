import datetime as dt

from marshmallow import Schema, fields


class Task():
  def __init__(self, description, type):
    self.description = description
    self.created_at = dt.datetime.now()
    self.type = type

  def __repr__(self):
    return '<Task(name={self.description!r})>'.format(self=self)

  def get_dict(self):
    return {"description": self.description,
            "type": str(self.type),
            "created_at": self.created_at}

class TaskSchema(Schema):
  description = fields.Str()
  created_at = fields.Date()
  type = fields.Str()
