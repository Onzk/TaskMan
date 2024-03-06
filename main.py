from flask import Flask, render_template, request, redirect
from queue import SimpleQueue, LifoQueue

from models.task import Task

app = Flask(__name__)

task_list, task_file, task_stack = [], SimpleQueue(), LifoQueue

sub_status = "all"
sort_by = "default"

categories = []


task_list.append(Task("Aller bosser", "20 Janvier"))


@app.route("/")
def index():
    if sub_status == "completed":
        tasks = [task for task in task_list if task.completed]
    elif sub_status == "remaining":
        tasks = [task for task in task_list if not task.completed]
    else:
        tasks = task_list

    return render_template(
        "index.html",
        tasks=tasks,
        categories=categories,
        sub_status=sub_status,
        sort=sort_by,
    )


@app.route("/sub_status/<status>")
def change_sub_status(status: str = ""):
    global sub_status
    sub_status = status if status.lower() in ["completed", "remaining"] else "all"
    return redirect(request.referrer)


@app.route("/sort/<sort>")
def change_sort(sort: str = ""):
    global sort_by
    sort_by = (
        sort
        if sort.lower()
        in [
            "default",
            "upper_priority",
            "lower_priority",
            "closer_deadline",
            "far_deadline",
        ]
        else "default"
    )
    return redirect(request.referrer)


@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    task_list.append(name)
    return redirect("/")


@app.route("/update", methods=["POST"])
def update():
    old_name = request.form["old_name"]
    new_name = request.form["new_name"]
    if old_name in task_list:
        index = task_list.index(old_name)
        task_list[index] = new_name
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    name = request.form["name"]
    if name in task_list:
        task_list.remove(name)
    return redirect("/")

@app.route("/category", methods=["POST"])
def add_category():
    categories.add(request.form["name"])
    return redirect("/")
    


@app.errorhandler(404)
def page_not_found(e):
    return render_template('./errors/404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('./errors/500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
