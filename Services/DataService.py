from Data.Models.TaskStatus import TaskStatus


class DataService:

    @staticmethod
    def createProcessLog(status: TaskStatus):
        print(status.message, status.executedAt)
