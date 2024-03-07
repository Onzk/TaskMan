from server import *
from routes.task import *
from routes.category import *
from routes.error import *


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


if __name__ == "__main__":
    app.run(debug=True)
