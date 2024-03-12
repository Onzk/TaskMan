import uuid

class Category:
    def __init__(self, description: str, sub_categories=[], id:str = None):
        self.__id = str(uuid.uuid4()).replace("-", "_") if id == None else id
        self.description = description
        self.sub_categories = sub_categories

    def addChild(self, sub_category):
        self.sub_categories.append(sub_category)

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str) -> None:
        raise Exception("Unable to change a category id.")

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    def filterTasks(self, tasks:list) -> list:
        return [task for task in tasks if task.id.endswith(self.id)]

    def containsTasks(self, tasks:list) -> list:
        return [task for task in tasks if self.id in task.id]

    def complationRate(self, tasks:list) -> float:
        completed = [task for task in tasks if self.id in task.id and task.completed]
        return round((len(completed) / max(1, len(self.containsTasks(tasks)))) * 100)

    @property
    def sub_categories(self) -> list:
        return self.__sub_categories

    @sub_categories.setter
    def sub_categories(self, sub_categories: list) -> None:
        self.__sub_categories = sub_categories.copy()
    
