from flask import Blueprint, render_template

home_views = Blueprint("home_views", __name__)

@home_views.route('/')
def index():
    return render_template('home.html')

@home_views.route('/ctest')
def index_ctest():
    return render_template('ctest.html')


