from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, ForeignKey, Float, LargeBinary

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    # Login information
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    password_hash = Column(String(128))

    # Profile information
    bio = Column(String(500), nullable=True)
    interests = Column(String(500), nullable=True)
    following = Column(String(500), nullable=True)
    network = Column(String(500), nullable=True)
    background_image = Column(String(100), nullable=True)

    # Permissions
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'

class Network(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True)

    # Follower information
    follower_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    followed_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Followers {self.follower_id}>'

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)

    # Event information
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    location = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)
    time = Column(Time, nullable=False)
    image = Column(LargeBinary)
    
    # Flags for event status
    is_active = Column(Boolean, default=True)
    is_complete = Column(Boolean, default=False)
    is_cancelled = Column(Boolean, default=False)

    # Flags for event type
    is_volunteer = Column(Boolean, default=False)
    is_workshop = Column(Boolean, default=False)
    is_fundraiser = Column(Boolean, default=False)
    is_social = Column(Boolean, default=False)
    is_other = Column(Boolean, default=False)

    # Foreign Key
    organizer_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # organizer = relationship('User', backref='events')
    

    def __repr__(self):
        return f'<Event {self.title}>'
    
class Map(Base):
    __tablename__ = 'map'

    id = Column(Integer, primary_key=True)

    # Event Id
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)

    # Map information
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
        
    def __repr__(self):
        return f'<Map {self.event_id}>'