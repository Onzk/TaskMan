"""
Le module routes.category contient les routes
relatives à la gestion des catégories.

"""

from state import *


@app.route("/add-category", methods=["POST"])
def add_category(): # Complexité temporelle totale : O(n)
    """Permet de créer une catégorie.

    Returns:
        Any : redirection vers la page d'accueil
    """
    # Ajout de la nouvelle catégorie à la racine des
    # catégories
    root.addChild(Category(request.form["description"]))  # O(n)
    # Sauvegarde un message de confirmation à afficher
    flash("Category added successfully !")  # O(1)
    # Redirige vers la page d'accueil
    return redirect("/")  # O(1)


@app.route("/update-category/<id>", methods=["POST"])
def update_category(id: str):  # Complexité temporelle totale : O(n)
    """Met à jour une catégorie.

    Args:
        id (str): l'id de la catégorie à mettre à jour

    Returns:
        Any : redirection vers la page d'accueil
    """
    # On parcourt la liste des catégories
    for i in range(len(root.sub_categories)):  # O(n)
        # Si l'id de la catégorie à la position
        # i correspond à l'id cible
        if root.sub_categories[i].id == id:  # O(1)
            # On met à jour la description de la catégorie
            # par rapport à la valeur saisie
            root.sub_categories[i].description = request.form["description"]  # O(1)
            # On arrête la boucle
            break  # O(1)
    # On charge un message de confirmation
    flash("Category updated successfully !")  # O(1)
    # On redirige vers la page d'accueil
    return redirect("/")  # O(1)


@app.route("/delete-category/<id>", methods=["POST"])
def delete_category(id: str):  # Complexité temporelle totale : O(n**2)
    """Supprime une catégorie.

    Args:
        id (str): id de la catégorie à supprimer

    Returns:
        Any: redirige vers la page d'accueil
    """
    # Supprime les tâches qui appartiennent à la catégorie cible
    [task_list.remove(task) for task in task_list if id in task.id]  # O(n**2)
    # Supprime la catégorie cible de la liste des catégories
    [
        root.sub_categories.remove(category)
        for category in root.sub_categories
        if category.id == id
    ]  # O(n**2)
    # On charge un message de confirmation
    flash("Category deleted successfully !")  # O(1)
    # On redirige vers la page d'accueil
    return redirect("/")  # O(1)
