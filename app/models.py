from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Login information
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    password_hash = db.Column(db.String(128))

    # Profile information
    bio = db.Column(db.String(500), nullable=True)
    interests = db.Column(db.String(500), nullable=True)
    following = db.Column(db.String(500), nullable=True)
    network = db.Column(db.String(500), nullable=True)

    # Permissions
    is_volunteer = db.Column(db.Boolean, default=False)
    is_originator = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    is_staff = db.Column(db.Boolean, default=False)
    is_superuser = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.Time, nullable=False)
    
    # Flags for event status
    is_active = db.Column(db.Boolean, default=True)
    is_complete = db.Column(db.Boolean, default=False)
    is_cancelled = db.Column(db.Boolean, default=False)

    # Flags for event type
    is_volunteer = db.Column(db.Boolean, default=False)
    is_workshop = db.Column(db.Boolean, default=False)
    is_fundraiser = db.Column(db.Boolean, default=False)
    is_social = db.Column(db.Boolean, default=False)
    is_other = db.Column(db.Boolean, default=False)

    # Foreign Key
    originator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    originator = db.relationship('User', backref='events')

    def __repr__(self):
        return f'<Event {self.title}>'
    
class Map(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Map information
    coordinate = db.Column(db.String(100), nullable=False) 
    

    def __repr__(self):
        return f'<Map {self.title}>'