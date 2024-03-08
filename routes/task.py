from state import *

task_list.append(Task("Start Influx DB server", "2024-02-08 10:33", 4))
# task_list.append(Task("Start Grafana server", "2024-02-08 20:33", 5))
# task_list.append(Task("Reload Telegraf monitoring system", "2024-03-08 06:33", 5))
# task_list.append(
#     Task("Enter Elixir Notification Service under maintenace", "2024-02-12 15:00", 3)
# )
# [task_stack.put(_) for _ in task_list]


# Done
@app.route("/create-task", methods=["POST"])
def createTask():
    description = request.form["description"]
    priority = int(request.form["priority"])
    deadline = request.form["deadline"]
    category = (request.form["category"], request.form["sub_category"])
    task = Task(
        description=description,
        deadline=deadline,
        priority=priority,
        category=category,
    )
    task_list.append(task)
    # task_stack.put(task)
    flash("Task created successfully !")
    return redirect("/")


@app.route("/update-task/<id>", methods=["POST"])
def updateTask(id: str):
    for i in range(len(task_list)):
        if task_list[i].id == id:
            task_list[i].description = request.form["description"]
            task_list[i].priority = int(request.form["priority"])
            task_list[i].deadline = request.form["deadline"]
            break
    flash("Task updated successfully !")
    return redirect("/")


# Done
@app.route("/toggle-task-state/<id>", methods=["POST"])
def toggleTaskState(id: str):
    for i in range(len(task_list)):
        if task_list[i].id == id:
            task_list[i].completed = not task_list[i].completed
            break

    flash("Task updated successfully !")
    return redirect("/")


@app.route("/delete-task/<id>", methods=["POST"])
def deleteTask(id: str):
    [task_list.remove(task) for task in task_list if task.id == id]

    flash("Task deleted successfully !")
    return redirect("/")
