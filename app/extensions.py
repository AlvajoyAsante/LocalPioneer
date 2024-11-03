from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

db = SQLAlchemy()

DATABASE_URL = "sqlite:///main.db" 
