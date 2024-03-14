"""
Le module routes.task contient les routes
relatives à la gestion des tâches.

"""

from state import *

@app.route("/create-task", methods=["POST"])
def createTask(): # Complexité temporelle totale : O(log n)
    """Crée une nouvelle tâche.

    Returns:
        Any: redirige vers la page d'accueil
    """
    # Récupère la description de la tâche
    description = request.form["description"] # O(1)
    # Récupère la priorité de la tâche
    priority = int(request.form["priority"]) # O(1)
    # Récupère la date limite de la tâche
    deadline = request.form["deadline"] # O(1)
    # Récupère la catégorie de la tâche
    category = (request.form["category"], request.form["sub_category"]) # O(1)
    # Crée une nouvelle tâche
    task = Task(
        description=description,
        deadline=deadline,
        priority=priority,
        category=category,
    ) # O(n)
    # Ajoute une nouvelle tâche à la liste des tâches
    task_list.append(task) # O(1)
    # Ajoute une nouvelle tâche à la pile des tâches
    task_stack.push(task) # O(1) 
    # Ajoute une nouvelle tâche à la file des tâches
    task_file.push(task) # O(log n) 
    # Charge un message de confirmation
    flash("Task created successfully !") # O(1)
    # Redirige vers la page d'accueil
    return redirect("/") # O(1)


@app.route("/update-task/<id>", methods=["POST"])
def updateTask(id: str): # Complexité temporelle totale : O(n**2)
    """Met à jour une tâche.

    Args:
        id (str): id de la tâche cible

    Returns:
        Any: redirige vers la page d'accueil
    """
    # On parcours la liste des tâches
    for i in range(len(task_list)): # O(n)
        # Si l'id de la tâche cible correpond à l'id
        # de la tâche à la position i
        if task_list[i].id == id: # O(1)
            # On met à jour la description de la tâche
            task_list[i].description = request.form["description"] # O(1)
            # On met à jour la priorité de la tâche
            task_list[i].priority = int(request.form["priority"]) # O(1)
            # On met à jour la date limite de la tâche
            task_list[i].deadline = request.form["deadline"].replace("T", " ") # O(n)
            # On sort de la boucle
            break # O(1)
    # On charge un message de confirmation
    flash("Task updated successfully !") # O(1)
    # On redirige vers la page d'accueil
    return redirect("/") # O(1)


@app.route("/toggle-task-state/<id>", methods=["POST"])
def toggleTaskState(id: str): # Complexité temporelle totale : O(n)
    """Permet de modifier l'état d'une tâche.

    Args:
        id (str): id de la tâche cible

    Returns:
        Any: redirige vers la page d'accueil
    """
    # On parcourt la liste des tâches
    for i in range(len(task_list)): # O(n)
        # Si la tâche à la position i a l'id cible
        if task_list[i].id == id: # O(1)
            # On change le status de la tâche
            task_list[i].completed = not task_list[i].completed # O(1)
            # On sort de la boucle
            break # O(1)
    # On charge un message de confirmation
    flash("Task updated successfully !") # O(1)
    # On redirige vers la page d'accueil
    return redirect("/") # O(1)


@app.route("/delete-task/<id>", methods=["POST"])
def deleteTask(id: str): # Complexité temporelle totale : O(n**2)
    """Permte de supprimer une tâche.

    Args:
        id (str): id de la tâche cible

    Returns:
        Any: redirige vers la page d'accueil
    """
    # On parcourt les tâches dans la liste des tâches
    for task in task_list: # O(n)
        # Si l'id de la tâche correspond à l'id cible
        if task.id == id: # O(1)
            # On supprime la tâche de la liste
            task_list.remove(task) # O(n)
            # On supprime la tâche de la file
            task_file.queue.queue.remove(task) # O(n)
            # On supprime la tâche de la pile
            task_stack.stack.remove(task) # O(n)
            # On sort de la boucle
            break # O(1)
    # On charge un message de confirmation
    flash("Task deleted successfully !") # O(1)
    # On redirige vers la page d'accueil
    return redirect("/") # O(1)
