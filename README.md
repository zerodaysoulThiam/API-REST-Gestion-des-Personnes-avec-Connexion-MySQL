![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3.2-orange?logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql&logoColor=white)
![Licence MIT](https://img.shields.io/badge/License-MIT-green)
![Build passing](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-blue)
![Swagger](https://img.shields.io/badge/Swagger-OpenAPI-orange?logo=swagger&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker&logoColor=white)
![Code Size](https://img.shields.io/github/languages/code-size/ton-repo/ton-projet)
![Last Commit](https://img.shields.io/github/last-commit/ton-repo/ton-projet)
![Issues](https://img.shields.io/github/issues/ton-repo/ton-projet)
![Stars](https://img.shields.io/github/stars/ton-repo/ton-projet?style=social)
![Forks](https://img.shields.io/github/forks/ton-repo/ton-projet?style=social)
![License](https://img.shields.io/github/license/ton-repo/ton-projet)
![PyPI](https://img.shields.io/pypi/v/nom-du-package)
![Downloads](https://img.shields.io/pypi/dm/nom-du-package)
![Commit Activity](https://img.shields.io/github/commit-activity/m/ton-repo/ton-projet)
![Top Language](https://img.shields.io/github/languages/top/ton-repo/ton-projet)

====================================================================
  API REST — Repertoire de Personnes
  Flask + MySQL (XAMPP / phpMyAdmin)
====================================================================

STRUCTURE
---------
api_project/
├── app.py           Point d entree Flask
├── database.py      Connexion MySQL
├── routes.py        Endpoints CRUD
├── swagger.yml      Documentation OpenAPI 3.0
├── requirements.txt Dependances
├── init_db.sql      Script SQL (base + table + donnees)
└── README.txt       Ce fichier


ETAPE 1 — BASE DE DONNEES (phpMyAdmin)
---------------------------------------
1. Demarrez XAMPP et activez Apache + MySQL
2. Ouvrez http://localhost/phpmyadmin
3. Cliquez sur l onglet "SQL"
4. Copiez-collez le contenu de init_db.sql
5. Cliquez "Executer"
   → La base api_people et la table person sont creees
   → 3 personnes sont inserees (Diallo, Sow, Fall)


ETAPE 2 — INSTALLATION PYTHON
--------------------------------
Dans le dossier api_project, ouvrez un terminal et tapez :

   pip install flask mysql-connector-python


ETAPE 3 — LANCER LE SERVEUR
-----------------------------
   python app.py

   Serveur : http://localhost:5000


ENDPOINTS
---------
GET    /api/people                Toutes les personnes
GET    /api/people?lname=Diallo   Filtrer par nom
GET    /api/people/1              Une personne par ID
POST   /api/people                Ajouter une personne
PUT    /api/people/2              Modifier une personne
DELETE /api/people/3              Supprimer une personne


EXEMPLES JSON
--------------
POST / PUT body :
{
  "lname": "Diop",
  "fname": "Fatou"
}

Reponse succes :
{"message": "Personne ajoutee avec succes"}

Reponse erreur :
{"error": "Personne introuvable"}


SECURITE SQL
-------------
Toutes les requetes SQL sont parametrees avec %s.
Aucune concatenation de chaine dans les requetes.
Protection totale contre l injection SQL.


SI VOUS AVEZ UN MOT DE PASSE MYSQL
------------------------------------
Ouvrez database.py et modifiez :
   password=""   →   password="votre_mot_de_passe"
====================================================================
