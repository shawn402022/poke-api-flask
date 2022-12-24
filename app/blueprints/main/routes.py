from . import bp as app
from flask import render_template, request, redirect, url_for
from app import app,db
from flask_login import current_user
# from app.blueprints.main.models import Pokemon


@app.route('/')
def home():
    return render_template('home.html', user=current_user)

@app.route('/about')
def about():
    return render_template('about.html')