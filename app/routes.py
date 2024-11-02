from flask import Blueprint, render_template
from app.models import User, Event, Map


# Create a blueprint object
main = Blueprint("main", __name__)

@main.route('/')
def home():
    return render_template("main.html", page_name="feed_page") 

@main.route('/Login')
def login():
    return render_template("main.html", page_name="login") 

@main.route('/map')
def login():
    return render_template("main.html", page_name="map") 




