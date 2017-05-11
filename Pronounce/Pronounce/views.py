"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from Pronounce import app, db
from .forms import VolunteersForm
from .models import Volunteer

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
            return redirect(url_for('sentences'))
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

@app.route('/sentences')
def sentences():
    """Renders the sentence page."""
    return render_template(
        'sentences.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )