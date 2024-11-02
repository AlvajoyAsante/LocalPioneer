from flask import Blueprint, render_template
from app.models import User, Event, Map


# Create a blueprint object
main = Blueprint("main", __name__)

@main.route('/')
def home():
    

    return render_template("main.html", page_name="feed_page") 




