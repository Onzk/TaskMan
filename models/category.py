"""
Le module models.category contient 
la représentation en classe de l'arbre des catégories.

"""

import uuid


class Category:
    """
    Cette classe représente la structure d'arbre
    des tâches qui permet de les organiser.
    """

    def __init__(
        self, description: str, sub_categories=[], id: str = None
    ):  # Complexité temporelle totale : O(n)
        """Constructeur d'une catégorie.

        Args:
            description (str): la description de la catégorie
            sub_categories (list, optional): la liste des sous catégories. Par défaut to [].
            id (str, optional): id de la catégorie. Par défaut to None.
        """
        # Génère un nouveau id pour la catégorie si
        # id est None dans l'appelle du constructeur
        self.__id = str(uuid.uuid4()).replace("-", "_") if id == None else id  # O(n)
        # Affecte la description à la catégorie
        self.description = description  # O(1)
        # Définit des sous catégories à la catégorie
        self.sub_categories = sub_categories  # O(1)

    def addChild(self, sub_category):  # Complexité temporelle totale : O(1)
        """Ajoute une sous catgéorie à la catégorie.

        Args:
            sub_category (Category): la sous catégorie
        """
        # Ajoute la nouvelle catégorie à la liste des
        # sous catégories.
        self.sub_categories.append(sub_category)  # O(1)

    def filterTasks(self, tasks: list) -> list:  # Complexité temporelle totale : O(n)
        """Retourne la liste des tâches directement
        à l'intérieur  de la catégorie.

        Args:
            tasks (list): liste des tâche à filtrer

        Returns:
            list: les tâches directement à l'intérieur de la catégorie
        """
        # Filtre les tâches appartenant directement à la catégorie
        return [task for task in tasks if task.id.endswith(self.id)]  # O(n)

    def containsTasks(self, tasks: list) -> list:  # Complexité temporelle totale : O(n)
        """Retourne la liste des tâches à l'intérieur
        de la catégorie ou d'une de ses sous-catégories.

        Args:
            tasks (list): liste des tâche à filtrer

        Returns:
            list: les tâches directement à l'intérieur de la catégorie
            ou d'une de ses sous catégories.
        """
        # Filtre les tâches appartenant aux sous catégories
        # ou à la catégorie.
        return [task for task in tasks if self.id in task.id]  # O(n)

    def complationRate(
        self, tasks: list
    ) -> float:  # Complexité temporelle totale : O(n)
        """Calcule le taux de tâches accomplies dans la catégorie.

        Args:
            tasks (list): liste des tâches

        Returns:
            float: le taux de tâches accomplies
        """
        # Filtre les tâches qui appartiennet à la catégorie
        Category_tasks = self.containsTasks(tasks)  # O(n)
        # S'il n'y a pas de tâches
        if len(Category_tasks) == 0:  # O(1)
            # Renvoie 100
            return 100  # O(1)
        # Sinon, trouve les tâches accomplies
        completed = [
            task for task in tasks if self.id in task.id and task.completed
        ]  # O(n)
        # Retourne le taux de tâches accomplies
        return round((len(completed) / len(Category_tasks)) * 100)  # O(n)

    @property
    def id(self) -> str:  # Complexité temporelle totale : O(1)
        """Permet de récupérer la propriété id de la catégorie.

        Returns:
            list: la propriété id de la catégorie
        """
        return self.__id  # O(1)

    @id.setter
    def id(self, id: str) -> None:  # Complexité temporelle totale : O(1)
        """Définit l'id de la catégorie

        Args:
            id (str): nouvel id de la catégorie

        Raises:
            Exception: empêchant la modification de l'id
        """
        raise Exception("Unable to change a category id.")  # O(1)

    @property
    def description(self) -> str:  # Complexité temporelle totale : O(1)
        """Permet de récupérer la description de la catégorie.

        Returns:
            list: la description de la catégorie
        """
        return self.__description  # O(1)

    @description.setter
    def description(
        self, description: str
    ) -> None:  # Complexité temporelle totale : O(1)
        """Définit une nouvelle description à la catégorie.

        Args:
            description (str): nouvelle description de la catégorie
        """
        self.__description = description  # O(1)

    @property
    def sub_categories(self) -> list:  # Complexité temporelle totale : O(1)
        """Permet de récupérer les sous catégories de la catégorie.

        Returns:
            list: les sous catégories de la catégorie
        """
        return self.__sub_categories  # O(1)

    @sub_categories.setter
    def sub_categories(
        self, sub_categories: list
    ) -> None:  # Complexité temporelle totale : O(n)
        """Définit une nouvelle liste de sous catégories

        Args:
            sub_categories (list): nouvelle liste de sous catégorgies
        """
        self.__sub_categories = sub_categories.copy()  # O(n)
