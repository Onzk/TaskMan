"""
Le module main est le point d'entrée de
l'application. Il s'agit du module qui s'exécute
pour le bon fonctionnement de l'application.

"""

from state import *
from routes.task import *
from routes.category import *
from routes.sub_category import *
from routes.error import *
from kernel import *


@app.route("/")
def index(): # Complexité temporelle totale : O(nlog n)
    """Gère l'affichage de la page d'accueil.

    Returns:
        Any: retourne le fichier index.html
    """
    # On applique l'arrangement par prioirité
    tasks = apply_priority_type(sort_by) # O(nlog n) 
    # On applique le filtre par status
    tasks = apply_sub_status(sub_status, tasks=tasks) # O(n)
    # On applique le filtre par correspondance
    tasks = apply_search(tasks, search=search) # O(n**2)
    # On renvoit le fichier index.html qui la page d'accueil
    return render_template(
        "index.html",
        tasks=tasks,
        categories=root.sub_categories,
        sub_status=sub_status,
        sort=sort_by,
        search=search,
    ) # O(1)


@app.route("/sub_status/<status>")
def change_sub_status(status: str = ""): # Complexité temporelle totale : O(n)
    """Change la valeur globale du type de status voulu.

    Args:
        status (str, optional): le nouveau status. Par défaut "".

    Returns:
        Any: redirige vers la page d'où la requête a été émise
    """
    # Signifie qu'on veut modifier la valeur globale 
    # du status
    global sub_status
    # Corrige si nécessaire la valeur du status
    sub_status = status if status.lower() in ["completed", "remaining"] else "all" # O(n)
    # Redirige vers la page d'òu la requête a été émise
    return redirect(request.referrer) # O(1)

@app.route("/search",  methods=["POST"])
def set_search(): # Complexité temporelle totale : O(1)
    """Permet de définir la correspondance recherchée
    dans les informations des tâches

    Returns:
        Any: redirige vers la page d'où la requête a été émise
    """
    # Signifie qu'on veut modifier la valeur globale de search
    global search # O(1)
    # Affecte une nouvelle valeur à search
    search = request.form["search"] # O(1)
    # Redirige vers la page d'où la requête a été émise
    return redirect(request.referrer) # O(1)


@app.route("/sort/<sort>")
def change_sort(sort: str = ""): # Complexité temporelle totale : O(n)
    """Change le mode d'arrangement de la liste des tâches.

    Args:
        sort (str, optional): la nouvelle façon d'ordonner la liste. Par défaut "".

    Returns:
        Any: redirige vers la page d'où la requête a été émise
    """
    # Signifie qu'on veut modifier la valeur globale de sort_by
    global sort_by # O(1)
    # Affecte une nouvelle valeur à sort_by
    sort_by = (
        sort
        if sort.lower()
        in "default upper_priority lower_priority by_deadline"
        else "default"
    ) # O(n)
    # Redirige vers la page d'où la requête a été émise
    return redirect(request.referrer) # O(1)


if __name__ == "__main__": # O(1)
    # Lance le serveur
    app.run(debug=True) # O(1)
