"""
Le module state contient tout ce qui a un lien
avec le fonctionnement de l'application et qui 
doit être accessible globalement.
"""

from flask import Flask, render_template, request, redirect, flash
from queue import SimpleQueue, LifoQueue, PriorityQueue
from core.task_queue import TaskQueue
from core.task_stack import TaskStack
from models.task import Task
from models.category import Category

# Représente le point d'entrée de l'application.
# Il s'agit du démarreur du serveur Flask.
app = Flask(__name__)  # O(1)

# Affecte une clé de session à l'application.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # O(1)

# Définit la liste, la file et la pile des tâches.
task_list, task_file, task_stack = [], TaskQueue(), TaskStack()  # O(1) | O(1) | O(1)

# Définit le sous status des tâches, pour
# des filtres sur l'application.
sub_status = "all"  # O(1)

# Définit l'ordre d'affichage des tâches.
sort_by = "default"  # O(1)

# Définit la recherche faite par l'utilisateur.
search = ""  # O(1)

# Définit la racine de l'arbre des catégories.
root = Category("root")  # O(n)

# Ajoute une catégorie To-Do par défaut à l'arbre
# des catégories.
root.addChild(Category("To-Do", [], "@"))  # O(n)
