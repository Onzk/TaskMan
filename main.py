from state import *
from routes.task import *
from routes.category import *
from routes.sub_category import *
from routes.error import *
from kernel import *


@app.route("/")
def index():
    tasks = apply_priority_type(sort_by)
    tasks = apply_sub_status(sub_status, tasks=tasks)
    tasks = apply_search(tasks, search=search)
    # tasks = [task for task in tasks if task is not None]
    return render_template(
        "index.html",
        default_tasks=[task for task in tasks if task.id.endswith("@")],
        tasks=tasks,
        categories=root.sub_categories,
        sub_status=sub_status,
        sort=sort_by,
        search=search,
    )


@app.route("/sub_status/<status>")
def change_sub_status(status: str = ""):
    global sub_status
    sub_status = status if status.lower() in ["completed", "remaining"] else "all"
    return redirect(request.referrer)

@app.route("/search",  methods=["POST"])
def set_search():
    global search
    search = request.form["search"]
    return redirect(request.referrer)


@app.route("/sort/<sort>")
def change_sort(sort: str = ""):
    global sort_by
    sort_by = (
        sort
        if sort.lower()
        in "default upper_priority lower_priority by_deadline"
        else "default"
    )
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(debug=True)
