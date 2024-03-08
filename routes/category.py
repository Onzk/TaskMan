from state import *

root.addChild(Category("Crontab deploiement"))


@app.route("/add-category", methods=["POST"])
def add_category():
    root.addChild(Category(request.form["description"]))
    flash("Category added successfully !")

    return redirect("/")


@app.route("/update-category/<id>", methods=["POST"])
def update_category(id: str):
    for i in range(len(root.sub_categories)):
        if root.sub_categories[i].id == id:
            root.sub_categories[i].description = request.form["description"]
            break

    flash("Category updated successfully !")
    return redirect("/")


@app.route("/delete-category/<id>", methods=["POST"])
def delete_category(id: str):
    [
        task_list.remove(task) for task in task_list if id in task.id
    ]
    [
        root.sub_categories.remove(category)
        for category in root.sub_categories
        if category.id == id
    ]

    flash("Category deleted successfully !")
    return redirect("/")
