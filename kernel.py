"""
Le module kernel contient les fonctions de filtre des
tâches avant affichage.

"""

import copy
from state import *


def apply_search(
    tasks: list, search: str
) -> list:  # Complexité temporelle totale : O(n**2)
    """Filtre les tâches par correspondance à la recherche.

    Args:
        tasks (list): liste des tâches
        search (str): la valeur de correspondance recherchée

    Returns:
        list: liste des tâches correspondantes à la recherche
    """
    # On filtre les tâches par leurs correspondances
    return [task for task in tasks if task.matches(search)]  # O(n**2)


def apply_priority_type(
    sort_by: str,
) -> list:  # Complexité temporelle totale : O(nlog n)
    """Ordonne la liste des tâches par priorité.

    Args:
        sort_by (str): le mode d'ordonnancement

    Returns:
        list: la liste des tâches ordonnées
    """
    # Si on veut un arrangement par défaut
    if sort_by == "default":  # O(1)
        # On renvoit la liste des tâches sans modification
        return task_list  # O(1)
    # Si on veut un arrangement par
    # date limite proche en priorité
    if "deadline" in sort_by:  # O(1)
        # On renvoit la liste des tâches selon la file des tâches
        return task_file.to_list()  # O(1)
    # Si on veut un arrangement par priorité
    if "priority" in sort_by:  # O(1)
        # On copie la pile
        _stack = copy.deepcopy(task_stack)  # O(n)
        # On crée une liste à partir des tâches
        # de celle-ci
        stack = [_stack.pop() for _ in range(len(_stack.stack))]  # O(nlog n)
        # Si on veut les tâches ayant les plus grandes
        # priorité en premier
        if "upper" in sort_by:  # O(1)
            # On renverse la liste
            stack.reverse()  # O(n)
        # On retourne la liste
        return stack  # O(1)
    # Sinon, on renvoit la liste des tâches
    return task_list  # O(1)


def apply_sub_status(
    sub_status: str, tasks
) -> list:  # Complexité temporelle totale : O(n)
    """Filtre les tâches par status.

    Args:
        sub_status (str): le status voulou
        tasks (_type_): la liste des tâches

    Returns:
        list: liste des tâches filtrée
    """
    # Si on veut uniquement les tâches accomplies
    if sub_status == "completed":  # O(1)
        # On renvoit uniquement les tâches accomplies
        return [task for task in tasks if task.completed]  # O(n)
    # Sinon, si on veut uniquement les tâches non accomplies
    elif sub_status == "remaining":  # O(1)
        # On renvoit uniquement les tâches non accomplies
        return [task for task in tasks if not task.completed]  # O(n)
    # Sinon, on renvoit toutes les tâches
    return tasks  # O(1)
