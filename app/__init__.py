from flask import Flask
from app.routes import main
from app.extensions import db, DATABASE_URL

def create_application(config_filename=None):
    app = Flask(__name__)

    configure_app(app, config_filename)
    register_blueprints(app)

    with app.app_context():
        db.create_all()
        insert_placeholder_data()

    return app

def configure_app(app, config_filename):
    if config_filename:
        app.config.from_pyfile(config_filename)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'
    app.config['DEBUG'] = True

    db.init_app(app)

def register_blueprints(app):
    app.register_blueprint(main)

def insert_placeholder_data():
    from datetime import datetime, time
    from app.models import Event, Map

    # Placeholder data for events
    events_data = [
        {
            'title': 'Event 1',
            'description': 'Description for Event 1',
            'location': 'New York, NY',
            'date': datetime(2023, 10, 1),
            'time': time(10, 0),
            'latitude': 40.7128,
            'longitude': -74.0060,
            'is_social': False,
            'is_workshop': False,
            'is_volunteer': False,
            'is_fundraiser': False,
            'is_other': True
        },
        {
            'title': 'Event 2',
            'description': 'Description for Event 2',
            'location': 'Los Angeles, CA',
            'date': datetime(2023, 10, 2),
            'time': time(11, 0),
            'latitude': 34.0522,
            'longitude': -118.2437,
            'is_social': False,
            'is_workshop': False,
            'is_volunteer': False,
            'is_fundraiser': False,
            'is_other': True
        },
        {
            'title': 'Event 3',
            'description': 'Description for Event 3',
            'location': 'Chicago, IL',
            'date': datetime(2023, 10, 3),
            'time': time(12, 0),
            'latitude': 41.8781,
            'longitude': -87.6298,
            'is_social': False,
            'is_workshop': False,
            'is_volunteer': False,
            'is_fundraiser': False,
            'is_other': True
        },
        {
            'title': 'Event 4',
            'description': 'Description for Event 4',
            'location': 'Houston, TX',
            'date': datetime(2023, 10, 4),
            'time': time(13, 0),
            'latitude': 29.7604,
            'longitude': -95.3698,
            'is_social': False,
            'is_workshop': False,
            'is_volunteer': False,
            'is_fundraiser': False,
            'is_other': True
        },
        {
            'title': 'Event 5',
            'description': 'Description for Event 5',
            'location': 'Denver, CO',
            'date': datetime(2023, 10, 5),
            'time': time(14, 0),
            'latitude': 39.7392,
            'longitude': -104.9903,
            'is_social': False,
            'is_workshop': False,
            'is_volunteer': False,
            'is_fundraiser': False,
            'is_other': True
        },
        {
            'title': 'Volunteer at UNC Concessions',
            'description': 'Concessions for charity! Calling all do-gooders to help out at the UNC football game.',
            'location': 'Chapel Hill, NC',
            'date': datetime(2023, 8, 2),
            'time': time(11, 30),
            'latitude': 35.909157,
            'longitude': -79.0470482,
            'is_social': False,
            'is_workshop': False,
            'is_volunteer': True,
            'is_fundraiser': False,
            'is_other': False
        },
        {
            'title': 'Cary Food and Flea',
            'description': 'Come out to the Cary Food and Flea market for a day of food, fun, and shopping!',
            'location': 'Cary, NC',
            'date': datetime(2023, 8, 2),
            'time': time(11, 30),
            'latitude': 35.789511,
            'longitude': -78.782276,
            'is_social': True,
            'is_workshop': False,
            'is_volunteer': False,
            'is_fundraiser': False,
            'is_other': False
        }
    ]

    # Insert events and map data
    for event_data in events_data:
        event = Event(
            title=event_data['title'],
            description=event_data['description'],
            location=event_data['location'],
            date=event_data['date'],
            time=event_data['time'],
            is_active=True,
            is_complete=False,
            is_cancelled=False,
            is_volunteer=event_data['is_volunteer'],
            is_workshop=event_data['is_workshop'],
            is_fundraiser=event_data['is_fundraiser'],
            is_social=event_data['is_social'],
            is_other=event_data['is_other']
        )
        db.session.add(event)
        db.session.commit()

        map_entry = Map(
            event_id=event.id,
            latitude=event_data['latitude'],
            longitude=event_data['longitude']
        )
        db.session.add(map_entry)

        db.session.commit()