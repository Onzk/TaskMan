import copy
import queue
from models.task import Task

class TaskQueue:
    def __init__(self):
        self.queue = queue.PriorityQueue()
        
    def push(self, task:Task) -> None:
        copy_task = copy.deepcopy(task)
        copy_task.comp_by_priority = False
        self.queue.put(task)
        
    def pop(self):
        if not self.queue:
            return None
        return self.queue.get(False)
    
    def to_list(self) -> list:
        return self.queue.queue

