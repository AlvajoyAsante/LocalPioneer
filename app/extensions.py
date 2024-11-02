from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

db = SQLAlchemy()

DATABASE_URL = "sqlite:///main.db?pitr=on&pitr_path=./main.db.pitr" 

engine = create_engine(DATABASE_URL, echo=True) 

Base = declarative_base() 