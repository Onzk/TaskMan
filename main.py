from flask import Flask, render_template, request, redirect
from queue import SimpleQueue, LifoQueue

from models.task import Task

app = Flask(__name__)

task_list, task_file, task_stack = [], SimpleQueue(), LifoQueue

sub_status = "all"

categories = []


task_list.append(Task("Aller bosser", "20 Janvier"))

@app.route("/")
def home():
    return render_template("index.html", tasks=task_list, categories=categories, sub_status=sub_status)

@app.route("/<section>")
def index(section:str = ""):
    path = section if section.lower() in ["", "completed", "all", "remaining"] else ""
    
    if path == "completed":
        tasks = [task for task in task_list if task.completed]
    elif path == "remaining":
        tasks = [task for task in task_list if not task.completed]
    else :
        tasks = task_list
    print(categories)
    return render_template("index.html", tasks=tasks, categories=categories, sub_status=sub_status)

@app.route("/sub_status/<status>")
def change_sub_status(status:str = ""):
    global sub_status 
    sub_status = status if status.lower() in ["completed", "remaining"] else "all"
    return redirect('/')

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

if __name__ == "__main__":
    app.run(debug=True)