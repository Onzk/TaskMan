import uuid


class Task:

    priorityParser: list = [
        ("VERY LOW", "info"),
        ("LOW", "primary"),
        ("NORMAL", "success"),
        ("HIGH", "warning"),
        ("CRITICAL", "error"),
    ]

    def __init__(
        self,
        description: str,
        deadline: str,
        priority: int = 1,
        completed: bool = False,
        category: tuple = ("", ""),
    ) -> None:
        self.__id = (
            str(uuid.uuid4()).replace("-", "_")
            + "@"
            + str(category[0].strip())
            + str(category[1].strip())
        )
        self.description = description
        self.deadline = deadline.replace("T", " ")
        self.priority = priority
        self.completed = completed

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str) -> None:
        raise Exception("Unable to change a task id.")

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    @property
    def deadline(self) -> str:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str) -> None:
        self.__deadline = deadline

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int) -> None:
        self.__priority = min(max(priority, 1), 5)

    def parsePriority(self) -> tuple:
        return Task.priorityParser[self.__priority - 1]

    def __lt__(self, other):
        return self.priority < other.priority
