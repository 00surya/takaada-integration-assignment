from flask import Flask
from .database import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///takaada.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .controllers.insights_controller import insights_bp
    app.register_blueprint(insights_bp)

    with app.app_context():
        db.create_all()

    return app