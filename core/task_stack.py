"""
Le module core.task_stack permet d'implémenter la 
struture de pile des tâches.
"""

import heapq
from models.task import Task


class TaskStack:
    """
    Cette classe représente la structure de pile
    des tâches qui permet de les ordonner par priorité.
    """

    def __init__(self):  # Complexité temporelle totale : O(1)
        """Constructeur de la pile."""
        # Initialisation de la proprité "stack" de la
        # classe qui est une simple liste.
        self.stack: list = []  # O(1)

    def push(self, task: Task):  # Complexité temporelle totale : O(1)
        """Permet d'insérer une tâche dans la pile.
        Celle-ci est automatiquement ordonnée dans la pile.

        Args:
            task (Task): tâche à insérer
        """
        # Insére la nouvelle tâche à la position qu'il faut
        # par rapport à sa priorité
        heapq.heappush(self.stack, task)  # O(log n)

    def pop(self):  # Complexité temporelle totale : O(log n)
        """Permet de dépiler la pile.

        Returns:
            None: si la pile est vide
            Task: la tâche en haut de la pile
        """
        # Si la pile est vide
        if not self.stack:
            # On renvoie None
            return None
        # Sinon, on renvoie la tâche en haut de la pile
        return heapq.heappop(self.stack)  # O(log n)

    @property
    def stack(self) -> list:  # Complexité temporelle totale : O(1)
        """Permet de récupérer la propriété stack de la pile.

        Returns:
            list: la propriété stack de la pile
        """
        return self.__stack  # O(1)

    @stack.setter
    def stack(self, stack: list) -> None:  # Complexité temporelle totale : O(1)
        """Permet de modifier la valeur de la propriété stack.

        Args:
            stack (list): la nouvelle valeur de la propriété stack
        """
        self.__stack = stack  # O(1)
