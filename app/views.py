from flask import render_template
from app import app

# Chapter 1
@app.route('/basic_scene')
def basic_scene():
    return render_template('01.01-basic-scene.html', title='Basic Scene')

