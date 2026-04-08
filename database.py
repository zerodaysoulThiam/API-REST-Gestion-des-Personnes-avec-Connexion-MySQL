import mysql.connector

# ============================================================
# database.py — Connexion a MySQL (XAMPP / phpMyAdmin)
# ============================================================
# Modifiez uniquement "password" si vous en avez un.
# Avec XAMPP par defaut : user=root, password="" (vide)
# ============================================================

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",          # <-- mettez votre mot de passe ici si besoin
        database="api_people"
    )
    return conn
