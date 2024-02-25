class Task:
    
    def __init__(self, description:str, deadline:str, priority: int = 1, completed:bool = False) -> None:
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = completed
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description:str) -> None:
        self.__description = description
   
    @property
    def deadline(self) -> str:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline:str) -> None:
        self.__deadline = deadline
   
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority:int) -> None:
        self.__priority = min(max(priority, 1), 4)
        
   
        