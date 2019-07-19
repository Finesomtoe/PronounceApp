"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template, request, redirect, url_for, session, send_from_directory, flash
from Pronounce import app, db
from .forms import VolunteersForm, LoginForm, ChangePasswordForm, PasswordResetRequestForm, PasswordResetForm
from .models import Volunteer, Sentence, Recording
from flask.ext.login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from random import randint, sample
from flask_paginate import Pagination, get_page_parameter, get_page_args

sid = 0
Per_page = 10
UPLOAD_FOLDER = '/var/www/maasgeluide/live/writable/volunteerUploads/'
global volunteerrecordings_count


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
            volunteerrecordings_count = Recording.query.filter(Recording.volunteer_id == current_user.id).count()    
            remaining_sentences = 69 - volunteerrecordings_count
            return render_template('splash.html', remaining_sentences=remaining_sentences)
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
        global reclist
        global sentence_count
        reclist = []
        dialect = request.form.get("dialect")
        sentence_count = request.form.get("sentencecount")  
        volunteerrecordings = Recording.query.filter(Recording.volunteer_id == current_user.id)
        if volunteerrecordings is not None:
            for rec in volunteerrecordings:
                reclist.append(rec.sentence_id)
        rndNumber = sample([i for i in range(1, 70) if i not in reclist], int(sentence_count))
        length = len(rndNumber) - 1       
        return redirect(url_for('sentences', rand=0))


@app.route('/sentences/<int:rand>', defaults={'page': 1})
@app.route('/sentences/<int:rand>/<int:page>')
@login_required
def sentences(rand, page):
    form = VolunteersForm()
    """Renders the sentence page."""
    sentence = Sentence.query.get(int(rndNumber[rand]))
    rnd = rand

    if sentence is None:
        return redirect(url_for('contact'))
    else:
        global sid
        sid = rndNumber[rand]
        search = False
        perpage = Per_page
        offset = (page - 1) * perpage  
        audiofiles = {}

        recordings = Recording.query.filter(Recording.volunteer_id == current_user.id).limit(perpage).offset(offset)
        recording_count = Recording.query.filter(Recording.volunteer_id == current_user.id).count()
        remaining_sentences = 69 - recording_count
        if recording_count == 0:
             return render_template('sentences.html', sentence=sentence, remaining_sentences=remaining_sentences, rnd=rnd, length=length, dialect=dialect, form=form, recording_count=recording_count)
        else:
            for rec in recordings:
                edit = rec.audiofilepath.replace('/var/www/limburgs/live/writable/volunteerUploads/', '')
                edit2 = "/static/volunteerUploads/"+edit
                audiofiles[rec.audiofilepath] = edit2
    
            rows = Recording.query.filter(Recording.volunteer_id == current_user.id).count()
            pagination = Pagination(page=page, total=rows, per_page=perpage, search=search, record_name='recordings', css_framework='bootstrap3')
            # 'page' is the default name of the page parameter, it can be customized
            # e.g. Pagination(page_parameter='p', ...)
            # or set PAGE_PARAMETER in config file
            # also likes page_parameter, you can customize for per_page_parameter
            # you can set PER_PAGE_PARAMETER in config file
            # e.g. Pagination(per_page_parameter='pp')
         
            return render_template('sentences.html', sentence=sentence, rnd=rnd, reclist=reclist, remaining_sentences=remaining_sentences, length=length, dialect=dialect, form=form, mypage=page, per_page=perpage, recordings=recordings, pagination=pagination, audiofiles=audiofiles, recording_count=recording_count)

#@app.route('/update')
#def updaterows():
#    recording = Recording.query.filter(Recording.recordingname.like("sjommert%")).all()
#    for rec in recording:
#        filepath = rec.audiofilepath
#        s1 = filepath.replace("/var/www/limburgs/live/writable/volunteerUploads", "")
#        #s2 = s1.replace(".webm", "-edited.mp3")
#        rec.audiofilepath = UPLOAD_FOLDER + s1
#        db.session.commit()
#    return redirect(url_for('home'))    

#@app.route('/update')
#def updaterows():
#    name = 'sjömmert'
#    recording = Recording.query.filter(Recording.volunteer_id == 36).all()
#    for rec in recording:
#        filepath = rec.audiofilepath
#        s1 = filepath.replace(".ogg", ".mp3")
#        #s1 = s1.replace(".ogg", "-edited.mp3")
#        rec.audiofilepath = s1
#        db.session.commit()
#    return redirect(url_for('home'))

@app.route('/assemblies', methods=['GET', 'POST'])
def assemblies():
    #volunteer = Volunteer.query.filter_by(email = session['email']).first()   
    if request.method == 'POST':
        file = request.files['data']
        spokendialect = request.form.get('fname')
        print (spokendialect)
        volunteer = Volunteer.query.filter_by(email = current_user.email).first()
        sentence = Sentence.query.get(int(sid))

        if file:
            filename = secure_filename(file.filename)
            print (filename)
            #path = os.path.dirname(os.path.abspath(__file__)) + "/uploads/May2018"
            path = UPLOAD_FOLDER
            #path = "Pronounce/uploads/"
            print(path)
            if not os.path.exists(path):
                os.makedirs(path)
            app.config["UPLOAD_FOLDER"] = path
            basename = spokendialect  + str(sentence.sentenceid) + "_" + "V" + str(volunteer.id)
            ext = os.path.splitext(filename)[1]
            filename = basename + ext
            #if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
                #basename = volunteer.fullname + "_" + os.path.splitext(filename)[0]+ "_" + str(sentence.sentenceid)
                #ext = os.path.splitext(filename)[1]
                #filename = basename + ext
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            recording = Recording(basename, filepath, sentence.sentenceid, volunteer.id)
            existing_record = Recording.query.filter_by(recordingname = recording.recordingname).first()
            if existing_record is None:
                db.session.add(recording)
                db.session.commit()
                reclist.append(recording.sentence_id)
            else:
                flash("Hey, je hebt eerder de vorige zin uitgesproken. Dus, de opname die u heeft ingediend, heeft de oude overgeschreven. Geen probleem, ga verder met uitspraak!")
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
    recording_count = Recording.query.filter(Recording.volunteer_id == current_user.id).count() 
    global remaining_sentences
    search = False
    page = 1
    perpage = Per_page
    offset = (page - 1) * perpage  
    audiofiles = {}

    recordings = Recording.query.filter(Recording.volunteer_id == current_user.id).limit(perpage).offset(offset)
    remaining_sentences = 69 - recording_count
    if remaining_sentences == 0:
        for rec in recordings:
            edit = rec.audiofilepath.replace('/var/www/limburgs/live/writable/volunteerUploads/', '')
            edit2 = "/static/volunteerUploads/"+edit
            audiofiles[rec.audiofilepath] = edit2   
        rows = Recording.query.filter(Recording.volunteer_id == current_user.id).count()
        pagination = Pagination(page=page, total=rows, per_page=perpage, search=search, record_name='recordings', css_framework='bootstrap3')           
        return render_template('sentences.html', remaining_sentences=remaining_sentences, mypage=page, per_page=perpage, recordings=recordings, pagination=pagination, recording_count=recording_count, audiofiles=audiofiles)
    else:
        return render_template('splash.html', remaining_sentences=remaining_sentences)

@app.route('/update', methods=['GET', 'POST'])
def updatevolunteer():
    form = VolunteersForm()
    if request.method == 'POST':
        volunteer = Volunteer.query.filter_by(email=current_user.email).first()
        if volunteer is None:
            flash("U kunt deze actie niet uitvoeren. je bent niet ingelogd")
        else:
            volunteer.fullname = request.form.get("fullname")
            volunteer.phonenumber = request.form.get("phonenr")
            db.session.commit()
            return redirect(url_for('signout'))

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
