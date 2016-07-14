from flask import render_template
from app import app

# Chapter 1
@app.route('/basic_scene')
def basic_scene():
    return render_template('01.01-basic-scene.html', title='Basic Scene')

@app.route('/simple_mesh')
def simple_mesh():
    return render_template('01.02-simple-mesh.html', title='Simple Mesh')

@app.route('/vertices')
def vertices():
    return render_template('01.03-vertices.html', title='vertices')

# Chapter 2
@app.route('/advanced_textures')
def advanced_textures():
    return render_template('02.05-advanced-textures.html', title='advanced_textures')

@app.route('/globe_and_camera')
def globe_and_camera():
    return render_template('02.01-globe-and-camera.html', title='globe_and_camera')

@app.route('/basic_textures')
def basic_textures():
    return render_template('02.02-basic-textures.html', title='basic_textures')

@app.route('/add_lighting')
def add_lighting():
    return render_template('02.03-add-lighting.html', title='add_lighting')


