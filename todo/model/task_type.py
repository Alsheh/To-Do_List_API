from enum import Enum


class TaskType(Enum):
  COMPLETED = "COMPLETED"
  UNCOMPLETED = "UNCOMPLETED"

  def __str__(self):
    return str(self.value)
