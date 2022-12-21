from . import bp as app
from flask import render_template, request, redirect, url_for
from app import db
from .models import Pokemon

@app.route('/pokemon')
def pokemon():
    all_pokemon = Pokemon.query.all()
    return render_template('pokemon.html', pokemon=all_pokemon)

@app.route('/pokemon/<id>')
def post_poke_id(id):
    pokemon= Pokemon.query.get(int(id))
    print(pokemon.user)
    return render_template('pokemon-single.html', pokemon=pokemon)

@app.route('/add-pokemon')
def add_poke():
    return render_template('add-pokemon.html')

@app.route('/create-pokemon', methods=["POST"])
def create_poke():
    name = request.form['inputPname']
    description = request.form['inputDescription']
    type = request.form['inputType']
    new_pokemon = Pokemon(name=name, description=description, type= type, owner_id=1)
    db.session.add(new_pokemon)
    db.session.commit()
    print(f'{name} has been added to the pokemon library.')
    return redirect(url_for('main2.add_poke'))