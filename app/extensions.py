from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

db = SQLAlchemy()

DATABASE_URL = "sqlite:///main.db" 
