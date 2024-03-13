"""
Le module routes.sub_category contient les routes
relatives à la gestion des sous-catégories.

"""

from state import *


@app.route("/add-sub-category/<id>", methods=["POST"])
def add_sub_category(id: str): # Complexité temporelle totale : O(n**2)
    """Ajoute une sous-catégorie à une catégorie.

    Args:
        id (str): id de la catégorie

    Returns:
        Any: redirige vers la page d'accueil
    """
    # On parcours les catégories
    for i in range(len(root.sub_categories)):  # O(n)
        # Si la catégorie à la position i
        # a l'id cible
        if root.sub_categories[i].id == id: # O(1)
            # On ajoute une nouvelle sous-catégorie à
            # la catégorie
            root.sub_categories[i].addChild(Category(request.form["description"])) # O(n)
            # On sort de la boucle
            break # O(1)
    # On charge un message de confirmation
    flash("Sub category added successfully !") # O(1)
    # On redirige vers la page d'accueil
    return redirect("/") # O(1)


@app.route("/update-sub-category/<id>/<sub>", methods=["POST"])
def udpate_sub_category(id: str, sub: str): # Complexité temporelle totale : O(n)
    """Mets à jour une sous-catégorie.

    Args:
        id (str): id de la catégorie contenant la sous-catégorie
        sub (str): id de la sous-catégorie cible

    Returns:
        Any: redirige vers la page d'accueil
    """
    # On récupère la catégorie cible
    category = [_ for _ in root.sub_categories if _.id == id] # O(n)
    # Si elle existe
    if len(category) > 0: # O(1)
        # On récupère la sous-catégorie cible
        sub_category = [_ for _ in category[0].sub_categories if _.id == sub][0] # O(n)
        # On mets à jour sa description
        sub_category.description = request.form["description"] # O(1)
        # On charge un message de confirmation
        flash("Sub category updated successfully !") # O(1)
    # Si la catégorie n'existe pas
    else:
        # On charge un message d'erreur
        flash("Sub category not found.") # O(1)
    # On redirige vers la page d'accueil
    return redirect("/") # O(1)


@app.route("/delete-sub-category/<id>/<sub>", methods=["POST"])
def delete_sub_category(id: str, sub: str): # Complexité temporelle totale : O(n**2)
    """Supprime une sous-catégorie.

    Args:
        id (str): id de la catégorie contenant la sous-catégorie
        sub (str): id de la sous-catégorie

    Returns:
        Any: redirige vers la page d'accueil
    """
    # On récupère la catégorie correspondante
    category = [_ for _ in root.sub_categories if _.id == id] # O(n)
    # Si elle existe
    if len(category) > 0: # O(1)
        # On supprime toutes les tâches appartenant
        # à la sous-catégorie
        [
            task_list.remove(_) for _ in task_list if sub in _.id 
        ] # O(n**2)
        # On supprime de la liste des sous-catégories,
        # la sosus-catégorie cible
        [
            category[0].sub_categories.remove(_)
            for _ in category[0].sub_categories
            if _.id == sub
        ] # O(n**2)
        # On charge un message de confirmation
        flash("Sub category deleted successfully !") # O(1)
    # Sinon
    else: 
        # On charge un message d'erreur
        flash("Sub category not found.") # O(1)
    # On redirige vers la page d'accueil
    return redirect("/") # O(1)
