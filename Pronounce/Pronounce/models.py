
from Pronounce import app, mysql, db, login_manager
from flask.ext.login import UserMixin
from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash
from flask import request

@login_manager.user_loader
def load_user(user_id):
    return Volunteer.query.get(int(user_id))

class Volunteer(UserMixin, db.Model):
    """description of class"""
    __tablename__ = 'volunteer'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    pwdhash = db.Column(db.String(100))
    fullname = db.Column(db.String(100))
    phonenumber = db.Column(db.Integer, unique = True)
    age = db.Column(db.Integer)
    dialectregion = db.Column(db.String(120))
    originregion = db.Column(db.String(120))
    gender = db.Column(db.String(45))
    recordings = db.relationship('Recording', backref='volunteer', lazy='dynamic')

    def __init__(self, email, password, name, phonenr, age, dialectregion, originregion, gender):      
        self.email = email.lower()
        self.set_password(password)
        self.fullname = name.lower()
        self.phonenumber = phonenr
        self.age = age
        self.dialectregion = dialectregion.title()
        self.originregion = originregion.title()
        self.gender = gender.lower()
    
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)    

    def __repr__(self):
        return '<Volunteer %r>' % self.fullname

class Sentence(db.Model):
    """description of class"""
    __tablename__ = 'sentence'
    sentenceid = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(120))
    sentencedutch = db.Column(db.String(200), unique=True)
    sentenceenglish = db.Column(db.String(200), unique=True)
    sentencemaas = db.Column(db.String(200), unique=True)
    sentenceeijsden = db.Column(db.String(200), unique=True)
    nrofrecordings = db.Column(db.Integer)
    recordings = db.relationship('Recording', backref='sentence', lazy='dynamic')
    

    def __init__(self, category, sentencedutch, sentenceenglish, sentencemaas, sentenceeijsden, nroforecordings):      
        self.category = category.lower()
        self.sentencedutch = sentencedutch.title()  
        self.sentenceenglish = sentenceenglish.title()
        self.sentencemaas = sentencemaas.title()
        self.sentenceeijsden = sentenceeijsden.title()
        self.nrofrecordings = nroforecordings      

    def __repr__(self):
        return '<Sentence %r>' % self.sentencedutch

class Recording(db.Model):
    """description of class"""
    __tablename__ = 'recording'
    recordingid = db.Column(db.Integer, primary_key=True)
    recordingname = db.Column(db.String(120))
    audiofilepath = db.Column(db.String(200))
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.sentenceid'))
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.id'))

    def __init__(self, recordingname, audiofilepath, sentence, volunteer):      
        self.recordingname = recordingname.lower()
        self.audiofilepath = audiofilepath
        self.sentence_id = sentence
        self.volunteer_id = volunteer    

    def __repr__(self):
        return '<Recording %r>' % self.recordingname