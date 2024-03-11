import heapq

from models.task import Task

class TaskStack:
    def __init__(self):
        self.queue: list = []

    def push(self, task: Task):
        heapq.heappush(self.queue, task) # O(log n)

    def pop(self):
        if not self.queue:
            return None
        return heapq.heappop(self.queue)
