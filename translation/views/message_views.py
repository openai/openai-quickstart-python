from flask import Blueprint, render_template

message_views = Blueprint("message_views", __name__)

@message_views.route("/messages")
def messages():
    return render_template("messages.html")