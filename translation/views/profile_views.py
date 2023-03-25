from flask import Blueprint, render_template

profile_views = Blueprint("profile_views", __name__)

@profile_views.route('/profile')
def profile():
    # Replace this with the actual user object after implementing authentication
    user = {
        "username": "Anthony's",
        "email": "sample@example.com",
        "preferred_language": "English",
        "friends": [
            {"username": "Friend 1"},
            {"username": "Friend 2"},
        ],
    }
    return render_template('profile.html', user=user)
