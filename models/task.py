"""
Le module models.task contient 
la représentation en classe de d'une tâche.

"""

import datetime
import uuid


class Task:
    """
    Cette classe représente une tâche.
    """

    def __init__(
        self,
        description: str,
        deadline: str,
        priority: int = 1,
        completed: bool = False,
        category: tuple = ("", ""),
    ) -> None: # Complexité temporelle totale : O(n)
        """Constructeur d'une tâche.

        Args:
            description (str): la description de la tâche
            deadline (str): la date limite de la tâche
            priority (int, optional): la priorité de la tâche. Par défault à 1.
            completed (bool, optional): le status de la tâche. Par défault à False.
            category (tuple, optional): la catégorie et/ou sous catégorie de la classe. Par défault à ("", "").
        """
        # Définit l'id de la tâche
        self.__id = (
            str(uuid.uuid4()).replace("-", "_")
            + str(category[0].strip())
            + str(category[1].strip())
        ) # O(n)
        # Définit la catégorie de la tâche
        self.description = description # O(1)
        # Définit la date limite de la tâche
        self.deadline = deadline.replace("T", " ") # O(n)
        # Définit la priorité de la tâche
        self.priority = priority # O(1)
        # Définit le status de la tâche
        self.completed = completed # O(1)
        # Définit si la tâche doit être comparée
        # par rapport à sa priorité
        self.comp_by_priority = True # O(1)

    def parsePriority(self) -> tuple: # Complexité temporelle totale : O(1)
        """Renvoie un couple (PRIORITE, COULEUR) par rapport
        à la priorité de la tâche.

        Returns:
            tuple: le couple (PRIORITE, COULEUR)
        """
        # Retourne le couple correspondant à la priorité
        # de la tâche
        return [
            ("VERY LOW", "info"),
            ("LOW", "primary"),
            ("NORMAL", "success"),
            ("HIGH", "warning"),
            ("CRITICAL", "error"),
        ][self.__priority - 1] # O(1)

    def __lt__(self, other) -> bool: # Complexité temporelle totale : O(1)
        """Définit la comparaison entre deux tâches.

        Args:
            other (Task): l'autre tâche à comparer

        Returns:
            bool: si la tâche est prioritaire à l'other
        """
        # Si on fait une comparaison par priorité
        if self.comp_by_priority: # O(1)
            # On compare par priorité
            return self.priority <= other.priority # O(1)
        # Sinon, on compare par rapport au temps restant avant
        # la fin de la date limite
        return self.remaining_time() >= other.remaining_time() # O(1)

    def timestamp(self) -> float: # Complexité temporelle totale : O(1)
        """Convertit la date limite en secondes.

        Returns:
            float: le timestamp de la date limite
        """
        # Retourne la date limite sous forme de secondes.
        return datetime.datetime.strptime(self.deadline, "%Y-%m-%d %H:%M").timestamp() # O(1)

    def remaining_time(self) -> float: # Complexité temporelle totale : O(1)
        """Récupère le temps restant avant la fin de la date limite.

        Returns:
            float: le temps restant en seconde
        """
        # Renvoie le maximum entre 0 et la valeur du temps restant
        # avant la fin de la date limite
        return max(self.timestamp() - datetime.datetime.now().timestamp(), 0) # O(1)

    def matches(self, search: str) -> bool: # Complexité temporelle totale : O(n)
        """Vérifie search correspond à la tâche.

        Args:
            search (str): la valeur à chercher

        Returns:
            bool: l'existence de la valeur dans la description
            ou la date limite de la tâche
        """
        # Renvoie la présence de search dans les informations de la tâche
        return search.lower() in f"{self.description} {self.deadline}".lower() # O(n)

    @property
    def id(self) -> str: # Complexité temporelle totale : O(1)
        """Récupère l'identifiant de la tâche.

        Returns:
            str: l'identifiant de la tâche
        """
        return self.__id # O(1)

    @id.setter
    def id(self, id: str) -> None: # Complexité temporelle totale : O(1)
        """ "Définit l'id de la tâche

        Args:
            id (str): nouvel id de la tâche

        Raises:
            Exception: empêchant la modification de l'id
        """
        raise Exception("Unable to change a task id.") # O(1)

    @property
    def description(self) -> str: # Complexité temporelle totale : O(1)
        """Permet de récupérer la description de la tâche.

        Returns:
            list: la description de la tâche
        """
        return self.__description # O(1)

    @description.setter
    def description(self, description: str) -> None: # Complexité temporelle totale : O(1)
        """Définit une nouvelle description à la tâche.

        Args:
            description (str): nouvelle description de la tâche
        """
        self.__description = description # o(1)

    @property
    def deadline(self) -> str: # Complexité temporelle totale : O(1)
        """Permet de récupérer la date limite de la tâche.

        Returns:
            list: la date limite de la tâche
        """
        return self.__deadline # O(1)

    @deadline.setter
    def deadline(self, deadline: str) -> None: # Complexité temporelle totale : O(1)
        """Définit une nouvelle date limite à la tâche.

        Args:
            deadline (str): nouvelle date limite de la tâche
        """
        self.__deadline = deadline # O(1)

    @property
    def priority(self) -> int: # Complexité temporelle totale : O(1)
        """Permet de récupérer la priorité de la tâche.

        Returns:
            list: la priorité de la tâche
        """
        return self.__priority # O(1)

    @priority.setter
    def priority(self, priority: int) -> None: # Complexité temporelle totale : O(1)
        """Définit une nouvelle priorité à la tâche.

        Args:
            sub_categories (list): nouvelle priorité de la tâche
        """
        self.__priority = priority # O(1)
