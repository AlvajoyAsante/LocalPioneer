from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from app.models import User, Event, Map
from app.extensions import db
from sqlalchemy import func, and_

# Create a blueprint object
main = Blueprint("main", __name__)


# Main Routes 
@main.route('/', methods=['GET', 'POST'])
def home(request):

    if request.method == 'POST':
        if 'user_id' in session:
            return render_template("main.html", page_name="feed_page")
        else:
            return render_template("main.html", page_name="login")

    return render_template("main.html", page_name="feed_page") 

@main.route('/forgot_password', methods=['GET', 'POST'])
def forgot_pass(request):
    return render_template("main.html", page_name="forgot_password")

@main.route('/login', methods=['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return render_template("main.html", page_name="feed_page")
        else:
            return render_template("main.html", page_name="login")

    return render_template("main.html", page_name="login") 

@main.route('/signup', methods=['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template("main.html", page_name="signup")
        else:
            new_user = User(email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit() 

            session['user_id'] = user.id

            return render_template("main.html", page_name="feed_page")

    return render_template("main.html", page_name="signup")

@main.route('/profile', methods=['GET', 'POST'])
def profile(request):
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    user = User.query.get(session['user_id']).first()
    return render_template("main.html", page_name="profile", user=user)

@main.route('/map')
def map():
    return render_template("main.html", page_name="map")

@main.route('/network', methods=['GET', 'POST'])
def network():
    return render_template("main.html", page_name="network")

@main.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template("main.html", page_name="logout")

# Organization pages

@main.route('/create_event', methods=['GET', 'POST'])
def create_event():
    return render_template("main.html", page_name="create_event")

@main.route('/edit_event', methods=['GET', 'POST'])
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

@main.route('/messages')
def messages():
    return render_template("main.html", page_name="messages")

@main.route('/follow')
def follow():
    pass 
    # return render_template("main.html", page_name="follow")

@main.route('/unfollow')
def unfollow():
    pass 
    # return render_template("main.html", page_name="unfollow")

# @main.route('/search')
# def search():
#     pass 
    # return render_template("main.html", page_name="search")
    
# @main.route('/notifications')
# def notifications():
#     pass 
    # return render_template("main.html", page_name="notifications")

# API Routes

@main.route('/api/events')
def get_events():
    # Get radius parameter from request (in kilometers)
    radius = float(request.args.get('radius', 10))
    # Get user's location from request
    user_lat = float(request.args.get('lat'))
    user_lng = float(request.args.get('lng'))
    
    # Calculate distance using Haversine formula
    distance = func.ST_Distance_Sphere(
        func.ST_GeomFromText(f'POINT({user_lng} {user_lat})'),
        func.ST_GeomFromText(f'POINT(Map.longitude Map.latitude)')
    ) / 1000  # Convert to kilometers
    
    # Query events within radius with their coordinates and type flags
    events = db.session.query(Event, Map)\
        .join(Map, Event.id == Map.event_id)\
        .filter(and_(
            Event.is_active == True,
            Event.is_complete == False,
            Event.is_cancelled == False,
            distance <= radius
        )).all()
    
    return jsonify([{
        'id': event.id,
        'name': event.title,
        'description': event.description,
        'type': get_event_type(event),
        'coords': [map_data.latitude, map_data.longitude],
        'date': event.date.strftime('%Y-%m-%d'),
        'time': event.time.strftime('%H:%M')
    } for event, map_data in events])

def get_event_type(event):
    """Helper function to determine event type"""
    if event.is_volunteer:
        return 'volunteering'
    elif event.is_workshop:
        return 'workshop'
    elif event.is_fundraiser:
        return 'fundraiser'
    elif event.is_social:
        return 'social'
    return 'other'
