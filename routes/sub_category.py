from state import *


cat = root.sub_categories[0]
cat.addChild(Category("Linux server installation"))
cat.addChild(Category("Redis server uninstallation"))
# root.addChild(Category("Maintenance of Rizis Sever"))


@app.route("/add-sub-category/<id>", methods=["POST"])
def add_sub_category(id: str):
    for i in range(len(root.sub_categories)):
        if root.sub_categories[i].id == id:
            root.sub_categories[i].addChild(Category(request.form["description"]))
            break

    flash("Sub category added successfully !")
    return redirect("/")


@app.route("/update-sub-category/<id>/<sub>", methods=["POST"])
def udpate_sub_category(id: str, sub: str):
    category = [_ for _ in root.sub_categories if _.id == id]
    if len(category) > 0:
        sub_category = [_ for _ in category[0].sub_categories if _.id == sub][0]
        sub_category.description = request.form["description"]
        flash("Sub category updated successfully !")
    else:
        flash("Sub category not found.")
    return redirect("/")


@app.route("/delete-sub-category/<id>/<sub>", methods=["POST"])
def delete_sub_category(id: str, sub: str):
    category = [_ for _ in root.sub_categories if _.id == id]
    if len(category) > 0:
        [
            category[0].sub_categories.remove(_)
            for _ in category[0].sub_categories
            if _.id == sub
        ]
        [
            task_list.remove(_) for _ in task_list if sub in _.id
        ]
        flash("Sub category deleted successfully !")
    else:
        flash("Sub category not found.")
    return redirect("/")
