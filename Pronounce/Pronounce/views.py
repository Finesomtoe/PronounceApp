"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template, request, redirect, url_for, session, send_from_directory
from Pronounce import app, db
from .forms import VolunteersForm
from .models import Volunteer, Sentence, Recording
from flask.ext.login import login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from random import randint, sample

sid = 0
global rndNumber 
global length
rndNumber = sample(range(1,31), 15)
length = len(rndNumber) - 1

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
            login_user(newvolunteer)
            return redirect(url_for('sentences', rand = 0))
    elif request.method == 'GET':
        return render_template('index.html', title='Home', form=form)


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'hi.html',
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

@app.route('/sentences/<int:rand>')
@login_required
def sentences(rand):
    """Renders the sentence page."""
    sentence = Sentence.query.get(int(rndNumber[rand]))
    rnd = rand

    if sentence is None:
        return redirect(url_for('contact'))
    else:
        global sid
        sid = rndNumber[rand]
        return render_template('sentences.html', sentence=sentence, rnd=rnd, length=length)

    

@app.route('/assemblies', methods=['GET', 'POST'])
def assemblies():
    #volunteer = Volunteer.query.filter_by(email = session['email']).first()   
    if request.method == 'POST':
        file = request.files['data']
        volunteer = Volunteer.query.filter_by(email = session['email']).first()
        sentence = Sentence.query.get(int(sid))

        if file:
            filename = secure_filename(file.filename)
            print (filename)
            path = os.path.dirname(os.path.abspath(__file__)) + "/uploads/"
            #path = "Pronounce/uploads/"
            print(path)
            if not os.path.exists(path):
                os.makedirs(path)
            app.config["UPLOAD_FOLDER"] = path
            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
                basename = volunteer.fullname + "_" + os.path.splitext(filename)[0]+ "_" + str(sentence.sentenceid)
                ext = os.path.splitext(filename)[1]
                filename = basename + ext
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            recording = Recording(volunteer.fullname + "_" + str(sentence.sentenceid), filepath, sentence.sentenceid, volunteer.id)
            db.session.add(recording)
            db.session.commit()
            print (app.config['UPLOAD_FOLDER'])
            return "Upload successful"
 
@app.route('/boxart')
def uploaded_boxart():
    return send_from_directory(app.config['UPLOAD_FOLDER'], "ogochukwu enendu_test_1.ogg")
    


    
