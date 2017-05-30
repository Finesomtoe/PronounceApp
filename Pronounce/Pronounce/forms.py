from flask.ext.wtf import Form
from .models import Volunteer
from Pronounce import db
from wtforms import StringField, IntegerField, RadioField, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField, BooleanField

class VolunteersForm(Form):
  name = TextField("Naam",  [validators.Required("Please enter your full name."), validators.Regexp('[A-Za-z]', 0, 'Usernames must have only letters')], render_kw={"placeholder": "Voor-en Achternaam"})
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")], render_kw={"placeholder": "Email Address"})
  phonenr = IntegerField("Mobile nummer", [validators.Optional(strip_whitespace=True)], render_kw={"placeholder": "Mobile nummer(Optional)"})
  age = IntegerField("Leeftijd", [validators.Optional(strip_whitespace=True)], render_kw={"placeholder": "Leeftijd(Optional)"})
  dialectregion = TextField("Spreekt het dialect van? (straat/buurt/stad)",  [validators.Required("Please enter the dialect you speak.")], render_kw={"placeholder": "Spreekt het dialect van? (straat/buurt/stad)"})
  originregion = TextField("Is geboren in..",  [validators.Required("Please enter your region of origin.")], render_kw={"placeholder": "Is geboren in.."})
  gender = RadioField("Gender", choices=[('man', 'Man'), ('vrouw', 'Vrouw')])
  submit = SubmitField("Ga Verder")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    volunteer = Volunteer.query.filter_by(email = self.email.data.lower()).first()
    if volunteer:
      self.email.errors.append("That email is already registered")
      return False
    else:
      return True

