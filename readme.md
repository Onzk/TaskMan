# Taskman : Système de gestion de tâches
<span style="font-size:46px;">T</span>
<img src="https://raw.githubusercontent.com/Onzk/TaskMan/master/static/assets/main-logo.png" width="10" style="margin-top:2rem" /> <span style="font-size:46px;">skman</span>

[![pyversions](https://img.shields.io/pypi/pyversions/scrapy-playwright.svg)](https://pypi.python.org/pypi/scrapy-playwright)

## A propos

Taskman est un programme basé sur le micro framework [Flask 3.0](https://flask.palletsprojects.com/en/3.0.x/) permettant
de gérer des tâches. Il s'agit globalement d'une `to-do list` implémentant une gestion des tâches par catégories et sous-catégories, conçues sur la ``structure de données d'arbre``, organisant les tâches par date limite proche en priorité grâce à une ``structure de file`` et par priorité, par une ``structure de donnée de pile``. 

Il est facilement configurable et adapté pour gérer les tâches par priorité, par date limite proche en priorité et par catégories, le tout grâce à aux structures de données, citées ci-haut.

Ce projet a été réalisé dans un cadre scolaire par des étudiants. 

Université : Université Catholique de l'Afrique de l'Ouest - Unité Universitaire du Togo ([UCAO-UUT](https://ucao-uut.tg/)).

Professeur en charge : Mr GBODUI Roland

Cours : Algorithme et Structure de Données

Institu : Cycle Ingénieur (ISTIN)

Parcours : Cybersécurité - Année préparatoire

Année scolaire : 2023-2024 

Etudiants :
    - KOUDOSSOU Messan Dhani Justin (chef de groupe)
    - ASSIGNON Akofala Bénédicta
    - d'ALMEIDA Ayité Juste Mawugnon


## Système

Le programme peut tout aussi bien fonctionner sous Windows comme sous un système Linux.


### Minimum requis pour les versions

* python >= 3.11.2
* flask >= 3.0


## Installation

Pour pouvoir utiliser cette application, vous aurez besoin de certains modules python.


### - Installation rapide

Pour une installation rapide de tous les modules dont vous aurez besoin, placez-vous à la racine du projet et faites :

```
pip install -r requirements.txt
```

### - Installation progressive

Pour une installation progressive de tous les modules dont vous aurez besoin, tapez les commandes suivantes pour installer :

* `flask` qui est disponible sur PyPI et peut être installé avec `pip`:

```
pip install flask
```

## Lancement

Pour lancer l'application (sous Windows/Linux), entrez la commande suivante dans le terminal.
```
python main.py
```

## Utilisation

Après avoir [lancé l'application](#lancement), vous pouvez accéder à l'application.

Le serveur `flask` démarre sur l'adresse ` http://127.0.0.1:5000` après le lancement.
```sh
* Serving Flask app 'state'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
* Debugger PIN: 151-996-108
```
<hr>
<div style="text-align:center">
<span style="font-size:18px;">Copyright &copy; T</span>
<img src="https://raw.githubusercontent.com/Onzk/TaskMan/master/static/assets/main-logo.png" width="10" style="margin-top:2rem" /> <span style="font-size:20px;">skman</span>.inc
</div>