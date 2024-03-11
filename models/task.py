import datetime
import uuid


class Task:

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
        self.comp_by_priority = True

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
        self.__priority = priority

    def parsePriority(self) -> tuple:
        return [
            ("VERY LOW", "info"),
            ("LOW", "primary"),
            ("NORMAL", "success"),
            ("HIGH", "warning"),
            ("CRITICAL", "error"),
        ][self.__priority - 1]

    def __lt__(self, other):
        if self.comp_by_priority :
            return self.priority <= other.priority
        return self.remaining_time() <= other.remaining_time()

    def timestamp(self) -> float:
        return datetime.datetime.strptime(self.deadline, "%Y-%m-%d %H:%M").timestamp()
    
    def remaining_time(self) -> float :
        return max(datetime.datetime.now().timestamp - self.timestamp(), 0)
