from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

# app = Flask(__name__)
# app.config.from_object(Config)
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)

    from app import models

    from app.auth import bp_auth
    app.register_blueprint(bp_auth, url_prefix='')

    from app.main import bp_main
    app.register_blueprint(bp_main, url_prefix='')

    from app.meeting import bp_meeting
    app.register_blueprint(bp_meeting, url_prefix='/meeting')

    return app
    # ... no changes to blueprint registration
