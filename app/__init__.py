from flask import Flask

def start_app():
    app = Flask(__name__)

    from app.controllers.users_controller import users_bp
    app.register_blueprint(users_bp, url_prefix="/users")
    # blueprints... 

    return app