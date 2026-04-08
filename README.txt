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
