from flask import Flask
from app.routes import main
from app.extensions import db, DATABASE_URL

def create_application(config_filename=None):
    app = Flask(__name__)

    configure_app(app, config_filename)
    configure_extensions(app)
    register_blueprints(app)

    return app

def configure_app(app, config_filename):
    if config_filename:
        app.config.from_pyfile(config_filename)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'
    app.config['DEBUG'] = True

def configure_extensions(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
        print("\t Database tables created")

def register_blueprints(app):
    app.register_blueprint(main)
