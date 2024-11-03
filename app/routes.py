from flask import Blueprint, render_template
from app.models import User, Event, Map

# Create a blueprint object
main = Blueprint("main", __name__)


# Main Routes 
@main.route('/')
def home():
    # Check if the user is logged in
    # If the user is logged in, show the feed page
    # If the user is not logged in, show the login page    


    return render_template("main.html", page_name="feed_page") 

@main.route('/forgot_password')
def forgot_pass():
    return render_template("main.html", page_name="forgot_password")


@main.route('/login')
def login():
    return render_template("main.html", page_name="login") 

@main.route('/signup')
def signup():
    return render_template("main.html", page_name="signup")

@main.route('/profile')
def profile():
    return render_template("main.html", page_name="profile")

@main.route('/map')
def map():
    return render_template("main.html", page_name="map")

@main.route('/network')
def network():
    return render_template("main.html", page_name="network")

@main.route('/logout')
def logout():
    return render_template("main.html", page_name="logout")

# Organization pages

@main.route('/create_event')
def create_event():
    return render_template("main.html", page_name="create_event")

@main.route('/edit_event')
def edit_event():
    return render_template("main.html", page_name="edit_event")

@main.route('/delete_event')
def delete_event():
    return render_template("main.html", page_name="delete_event")


# User pages

@main.route('/edit_profile')
def edit_profile():
    return render_template("main.html", page_name="edit_profile")

@main.route('/delete_profile')
def delete_profile():
    return render_template("main.html", page_name="delete_profile")

@main.route('/settings')
def settings():
    return render_template("main.html", page_name="settings")

@main.route('/message')
def message():
    return render_template("main.html", page_name="message")

@main.route('/follow')
def follow():
    pass 
    # return render_template("main.html", page_name="follow")

@main.route('/unfollow')
def unfollow():
    pass 
    # return render_template("main.html", page_name="unfollow")

@main.route('/search')
def search():
    pass 
    # return render_template("main.html", page_name="search")
    
@main.route('/notifications')
def notifications():
    pass 
    # return render_template("main.html", page_name="notifications")

