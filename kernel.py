import copy
from state import *


def apply_priority_type(sort_by: str) -> list:
    if sort_by == "default":
        return task_list
    if "deadline" in sort_by:
        [task_file.put(_) for _ in task_list]
        return [task_file.get(False) for _ in task_list]
    if "priority" in sort_by:
        [task_stack.put(_) for _ in task_list]
        stack = [task_stack.get(False) for _ in task_list]
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
