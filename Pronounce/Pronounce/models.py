
from Pronounce import app, mysql, db
from datetime import datetime 
from flask import request

class Volunteer(db.Model):
    """description of class"""
    __tablename__ = 'volunteer_test'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    fullname = db.Column(db.String(100))
    phonenumber = db.Column(db.Integer, unique = True)
    age = db.Column(db.Integer)
    dialectregion = db.Column(db.String(120))
    originregion = db.Column(db.String(120))
    gender = db.Column(db.String(45))

    def __init__(self, email, name, phonenr, age, dialectregion, originregion, gender):      
        self.email = email.lower()
        self.fullname = name.lower()
        self.phonenumber = phonenr
        self.age = age
        self.dialectregion = dialectregion.title()
        self.originregion = originregion.title()
        self.gender = gender
     
    def __repr__(self):
        return '<User %r>' % self.fullname

class Sentence(db.Model):
    """description of class"""
    __tablename__ = 'sentences_test'
    sentenceid = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(120))
    sentencedutch = db.Column(db.String(200), unique=True)
    sentenceenglish = db.Column(db.String(200), unique=True)
    sentencemaas = db.Column(db.String(200), unique=True)
    nrofrecordings = db.Column(db.Integer)
    

    def __init__(self, category, sentencedutch, sentenceenglish, sentencemaas, nroforecordings):      
        self.category = category.lower()
        self.sentencedutch = sentencedutch.title()  
        self.sentenceenglish = sentenceenglish.title()
        self.sentencemaas = sentencemaas.title()
        self.nrofrecordings = nroforecordings      

    def __repr__(self):
        return '<User %r>' % self.sentencedutch