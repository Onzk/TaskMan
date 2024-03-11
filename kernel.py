import copy
from state import *

def apply_search(tasks:list, search:str) -> list:
    return [task for task in tasks if task.matches(search)]

def apply_priority_type(sort_by: str) -> list:
    if sort_by == "default":
        return task_list
    if "deadline" in sort_by:
        return task_file.to_list()
    if "priority" in sort_by:
        _stack = copy.deepcopy(task_stack)
        stack = [_stack.pop() for _ in range(len(_stack.queue))]
        if "upper" in sort_by:
            stack.reverse()
        return stack
    return []


def apply_sub_status(sub_status: str, tasks) -> list:
    if sub_status == "completed":
        return [task for task in tasks if task.completed]
    elif sub_status == "remaining":
        return [task for task in tasks if not task.completed]
    return tasks
