from datetime import datetime
from Data.Models.TaskStatus import TaskStatus


def createTaskSuccessStatus(message):
    return TaskStatus("success", message, datetime.now())


def createTaskFailedStatus(message):
    return TaskStatus("fail", message, datetime.now())
