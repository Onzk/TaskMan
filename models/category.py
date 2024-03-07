import uuid


class Category:
    def __init__(self, description:str, tasks: list = [],  sub_categories=[]):
        self.__id = str(uuid.uuid4()).replace('-', '_')
        self.description = description
        self.tasks = tasks
        self.sub_categories = sub_categories


    def addChild(self, sub_category):
        self.sub_categories.append(sub_category)
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str) -> None:
        raise Exception('Unable to change a task id.')
    
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description
        
    @property
    def tasks(self) -> list:
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks: list) -> None:
        self.__tasks = tasks

    # def __str__(self, level=0):
    #     ret = "  " * level + str(self.tasks) + "\n"
    #     for child in self.sub_categories:
    #         ret += child.__str__(level + 1)
    #     return ret