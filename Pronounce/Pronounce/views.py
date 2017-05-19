"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template, request, redirect, url_for, session
from Pronounce import app, db
from .forms import VolunteersForm
from .models import Volunteer, Sentence, Recording
from werkzeug.utils import secure_filename


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    form = VolunteersForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html', form=form)
        else:
            newvolunteer = Volunteer(form.email.data, form.name.data, form.phonenr.data, form.age.data, form.gender.data, form.dialectregion.data, form.originregion.data)
            db.session.add(newvolunteer)
            db.session.commit()
            session['email'] = newvolunteer.email
            return redirect(url_for('sentences', id = 1))
    elif request.method == 'GET':
        return render_template('index.html', title='Home', form=form)


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/sentences/<id>')
def sentences(id):
    """Renders the sentence page."""
    sentence = Sentence.query.get(int(id))
    #volunteer = Volunteer.query.filter_by(email = session['email']).first()
      
    if sentence is None:
        return redirect(url_for('contact'))
    else:
        return render_template('sentences.html', sentence=sentence)

@app.route('/assemblies', methods=['GET', 'POST'])
def assemblies():
    #volunteer = Volunteer.query.filter_by(email = session['email']).first()   
    if request.method == 'POST':
        file = request.files['data']

        if file:
            filename = secure_filename(file.filename)
            print (filename)
            file.save(filename)
            print (app.config['UPLOAD_FOLDER'])
            return render_template('contact.html')

    
