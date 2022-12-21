from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# #route to show users pokemon collected
# @app.route('/pokemon/<username>')
# def display_all_poke(username):
    # return render_template('user_info.html')



#route to show users individual pokemon stats
# @app.route('/user/pokemon//<pokename>')
