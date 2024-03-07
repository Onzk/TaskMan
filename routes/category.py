from server import *


@app.route("/category", methods=["POST"])
def add_category():
    categories.add(request.form["name"])
    return redirect("/")
