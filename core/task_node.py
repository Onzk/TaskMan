from models.task import Task


class TaskNode:
    def __init__(self, task: Task):
        self.task = task
        self.next = None

    @property
    def task(self) -> int:
        return self.__task

    @task.setter
    def task(self, task: Task) -> None:
        self.__task = task

    @property
    def next(self) -> int:
        return self.__next

    @next.setter
    def next(self, next) -> None:
        self.__next = next
