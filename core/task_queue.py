"""
Le module core.task_queue permet d'implémenter la 
struture de file des tâches.

"""

import copy
import queue as q
from models.task import Task


class TaskQueue:
    """
    Cette classe représente la structure de file
    des tâches qui permet de les ordonner par
    date limite proche en priorité.
    """

    def __init__(self):  # Complexité temporelle totale : O(1)
        """Constructeur de la file."""
        # Initialisation de la proprité "queue" de la
        # classe qui est une PriorityQueue.
        self.queue = q.PriorityQueue()

    def push(self, task: Task) -> None:  # Complexité temporelle totale : O(log n)
        """Permet d'insérer une tâche dans la file.
        Celle-ci est automatiquement ordonnée dans la file.

        Args:
            task (Task): tâche à insérer
        """
        # Crée une version copiée de la tâche
        copy_task = copy.deepcopy(task)  # O(1)
        # Désactive la comparaison par priorité de la tâche
        copy_task.comp_by_priority = False  # O(1)
        # Insére la tâche dans la file
        self.queue.put(task)  # O(log n)

    def pop(self) -> Task:  # Complexité temporelle totale : O(1)
        """Permet défiler la file.

        Returns:
            None: si la file est vide
            Task: la première tâche dans la file
        """
        # Si la file est vide
        if not self.queue:  # O(1)
            # Renvoie None
            return None  # O(1)
        # Sinon, renvoie la première tâche dans la file
        return self.queue.get(False)  # O(1)

    def to_list(self) -> list:  # Complexité temporelle totale : O(1)
        """Renvoie la file sous forme de liste.

        Returns:
            queue: liste des tâches
        """
        return self.queue.queue  # O(1)

    @property
    def queue(self) -> q.PriorityQueue:  # Complexité temporelle totale : O(1)
        """Permet de récupérer la propriété queue de la file.

        Returns:
            q.PriorityQueue: la propriété queue de la file
        """
        return self.__queue  # O(1)

    @queue.setter
    def queue(
        self, queue: q.PriorityQueue
    ) -> None:  # Complexité temporelle totale : O(1)
        """Permet de modifier la valeur de la propriété queue.

        Args:
            queue (q.PriorityQueue): la nouvelle valeur de la propriété queue
        """
        self.__queue = queue  # O(1)
