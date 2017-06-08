"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template, request, redirect, url_for, session, send_from_directory, flash
from Pronounce import app, db
from .forms import VolunteersForm, LoginForm
from .models import Volunteer, Sentence, Recording
from flask.ext.login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from random import randint, sample

sid = 0

global string 
string = "My name is Somto"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    form = VolunteersForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html', form=form)
        else:
            newvolunteer = Volunteer(form.email.data, form.password.data, form.name.data, form.phonenr.data, form.age.data, form.dialectregion.data, form.originregion.data, form.gender.data)
            db.session.add(newvolunteer)
            db.session.commit()
            session['email'] = newvolunteer.email
            login_user(newvolunteer)
            return render_template('splash.html')
            #return redirect(url_for('sentences', rand = 0))
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

@app.route('/passdata', methods=['GET', 'POST'])
def passdata():
    if request.method == 'POST':
        global rndNumber 
        global length
        global file_number
        global dialect
        global sentence_count
        dialect = request.form.get("dialect")
        sentence_count = request.form.get("sentencecount")
        rndNumber = sample(range(1, 69), int(sentence_count))
        length = len(rndNumber) - 1
        return redirect(url_for('sentences', rand=0))

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
        return render_template('sentences.html', sentence=sentence, rnd=rnd, length=length, dialect=dialect)

    

@app.route('/assemblies', methods=['GET', 'POST'])
def assemblies():
    #volunteer = Volunteer.query.filter_by(email = session['email']).first()   
    if request.method == 'POST':
        file = request.files['data']
        volunteer = Volunteer.query.filter_by(email = current_user.email).first()
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
            basename = volunteer.dialectregion  + str(sentence.sentenceid) + "_" + "V" + str(volunteer.id)
            ext = os.path.splitext(filename)[1]
            filename = basename + ext
            #if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
                #basename = volunteer.fullname + "_" + os.path.splitext(filename)[0]+ "_" + str(sentence.sentenceid)
                #ext = os.path.splitext(filename)[1]
                #filename = basename + ext
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            recording = Recording(volunteer.fullname + "_" + str(sentence.sentenceid), filepath, sentence.sentenceid, volunteer.id)
            existing_record = Recording.query.filter_by(recordingname = recording.recordingname).first()
            if existing_record is None:
                db.session.add(recording)
                db.session.commit()
            else:
                flash("Your previous recording will be overwritten")
            print (app.config['UPLOAD_FOLDER'])
            return "Upload successful"
 

@app.route('/logged_in', methods=['GET','POST'])
def login():   
    form = LoginForm() 

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('badlogin.html', form=form)
        else:
            volunteer = Volunteer.query.filter_by(email=request.form.get("emailname")).first()
            #session['email'] = form.email.data
            if volunteer is None:
                flash("Dat is een ongeldige e-mail. Probeer het opnieuw")
                return redirect(url_for('home'))               
            else:
                login_user(volunteer)
                return redirect(url_for('instructie'))         
                        
    elif request.method == 'GET':
        return redirect(url_for('home'))

@app.route('/logout')
@login_required
def signout():
    logout_user()
    return render_template('logout.html')


@app.route('/instructie')
@login_required
def instructie():
    return render_template('splash.html')



@app.errorhandler(404)
def page_not_found(e):
    if current_user.is_authenticated:
        return redirect(url_for('instructie'))
    else:
        return redirect(url_for('home'))

@app.errorhandler(500)
def page_not_found(e):
    if current_user.is_authenticated:
        return redirect(url_for('instructie'))
    else:
        return redirect(url_for('home'))
