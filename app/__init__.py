from flask import Flask
from app.routes import main
from app.extensions import db, DATABASE_URL

def create_application(config_filename=None):
    app = Flask(__name__)

    # Load the default configuration
    # app.config.from_object('app.config')

    # Optionally load instance-specific config (like secret keys, DB URIs)
    if config_filename:
        app.config.from_pyfile(config_filename)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'
    app.config['DEBUG'] = True


    # Initialize extensions
    db.init_app(app)

    # Create the database
    # db.create_all()

    # Register blueprints
    app.register_blueprint(main)

    return app
