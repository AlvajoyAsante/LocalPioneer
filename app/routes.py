from flask import Blueprint, render_template
from app.models import User, Event, Map


# Create a blueprint object
main = Blueprint("main", __name__)

@main.route('/')
def home(): 
    return "Welcome to the Home Page!"


# @main.route('/login')
# def login():
    # return render_template('login.html')




