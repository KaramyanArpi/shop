from flask import Blueprint, request, jsonify
from app.services.users_service import register, update_usernme
from app.exceptions import UserError, UserAlreadyExistsError, UserDoesNotExistError

users_bp = Blueprint("users", __name__)

@users_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    age, username = data.get("age"), data.get("username")

    try:
        new_user = register(username, age)
        return {"user": new_user}, 201
    except UserError as e:
        return {"error": e.message}, e.status_code
    except UserAlreadyExistsError as e:
        return {"error": e.message}, e.status_code
    except Exception as e:
        return {"error": "Something went wrong. Please try again later."}, 500

@users_bp("/<int:id>/update-username")
def update_username(id):
    new_username = request.get_json().get("new_username")

    try:
        updated_user = update_usernme(id, new_username)
        return {"updated_user": updated_user}
    except UserDoesNotExistError as e:
        return {"error": e.message}, e.status_code
    except Exception as e:
        return {"error": "Something went wrong. Please try again later."}, 500
 