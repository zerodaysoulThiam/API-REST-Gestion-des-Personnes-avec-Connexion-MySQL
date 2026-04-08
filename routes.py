from flask import Blueprint, request, jsonify
from database import get_db_connection

# ============================================================
# routes.py — Tous les endpoints CRUD de l'API
# Requetes SQL 100% parametrees (protection injection SQL)
# ============================================================

people_bp = Blueprint('people', __name__)


def format_person(row):
    """Convertit une ligne MySQL en dict JSON propre."""
    return {
        "id":        row["id"],
        "lname":     row["lname"],
        "fname":     row["fname"],
        "timestamp": str(row["timestamp"]) if row["timestamp"] else None
    }


# ------------------------------------------------------------
# GET /api/people
# GET /api/people?lname=Diallo   (filtrage par nom)
# ------------------------------------------------------------
@people_bp.route('/api/people', methods=['GET'])
def get_people():
    lname = request.args.get("lname")
    try:
        conn   = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        if lname:
            # Requete parametree — securisee contre l'injection SQL
            cursor.execute(
                "SELECT id, lname, fname, timestamp FROM person "
                "WHERE lname = %s ORDER BY lname",
                (lname,)
            )
        else:
            cursor.execute(
                "SELECT id, lname, fname, timestamp FROM person ORDER BY lname"
            )

        rows   = cursor.fetchall()
        result = [format_person(r) for r in rows]
        cursor.close()
        conn.close()
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------------------------------------
# GET /api/people/<id>
# ------------------------------------------------------------
@people_bp.route('/api/people/<int:person_id>', methods=['GET'])
def get_person(person_id):
    try:
        conn   = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Requete parametree
        cursor.execute(
            "SELECT id, lname, fname, timestamp FROM person WHERE id = %s",
            (person_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            return jsonify(format_person(row)), 200
        return jsonify({"error": "Personne introuvable"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------------------------------------
# POST /api/people
# Body JSON : { "lname": "Diop", "fname": "Fatou" }
# ------------------------------------------------------------
@people_bp.route('/api/people', methods=['POST'])
def create_person():
    data = request.get_json()

    # Validation
    if not data:
        return jsonify({"error": "Corps JSON manquant"}), 400
    lname = data.get("lname", "").strip()
    fname = data.get("fname", "").strip()
    if not lname:
        return jsonify({"error": "Le champ lname est obligatoire"}), 400
    if not fname:
        return jsonify({"error": "Le champ fname est obligatoire"}), 400

    try:
        conn   = get_db_connection()
        cursor = conn.cursor()

        # Insertion parametree — timestamp gere par MySQL (NOW())
        cursor.execute(
            "INSERT INTO person (lname, fname, timestamp) VALUES (%s, %s, NOW())",
            (lname, fname)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Personne ajoutee avec succes"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------------------------------------
# PUT /api/people/<id>
# Body JSON : { "lname": "Sow", "fname": "Awa Marie" }
# ------------------------------------------------------------
@people_bp.route('/api/people/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.get_json()

    # Validation
    if not data:
        return jsonify({"error": "Corps JSON manquant"}), 400
    lname = data.get("lname", "").strip()
    fname = data.get("fname", "").strip()
    if not lname:
        return jsonify({"error": "Le champ lname est obligatoire"}), 400
    if not fname:
        return jsonify({"error": "Le champ fname est obligatoire"}), 400

    try:
        conn   = get_db_connection()
        cursor = conn.cursor()

        # Mise a jour parametree — timestamp mis a jour automatiquement
        cursor.execute(
            "UPDATE person SET lname = %s, fname = %s, timestamp = NOW() "
            "WHERE id = %s",
            (lname, fname, person_id)
        )
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()

        if affected == 0:
            return jsonify({"error": "Personne introuvable"}), 404
        return jsonify({"message": "Personne modifiee avec succes"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------------------------------------
# DELETE /api/people/<id>
# ------------------------------------------------------------
@people_bp.route('/api/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    try:
        conn   = get_db_connection()
        cursor = conn.cursor()

        # Suppression parametree
        cursor.execute(
            "DELETE FROM person WHERE id = %s",
            (person_id,)
        )
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()

        if affected == 0:
            return jsonify({"error": "Personne introuvable"}), 404
        return jsonify({"message": "Personne supprimee avec succes"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
