from flask.ext.wtf import Form
from .models import Volunteer
from Pronounce import db
from wtforms import StringField, IntegerField, RadioField, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField, BooleanField

class VolunteersForm(Form):
  name = TextField("Naam",  [validators.Required("Vul alsjeblieft je volledige naam in."), validators.Regexp('[A-Za-z]', 0, 'Usernames must have only letters')], render_kw={"placeholder": "Voor-en Achternaam"})
  email = TextField("Email",  [validators.Required("Vul alsjeblieft uw e-mailadres in."), validators.Email("Please enter your email address.")], render_kw={"placeholder": "E-mail Adres"})
  phonenr = IntegerField("Mobiele nummer", [validators.Optional(strip_whitespace=True), validators.Regexp('[0-9+()*#]+', 0, 'You entered a false character')], render_kw={"placeholder": "Mobiele nummer(Optional)"})
  age = IntegerField("Leeftijd", [validators.Required("Vul alstublieft uw leeftijd in")], render_kw={"placeholder": "Leeftijd"})
  dialectregion = TextField("Spreekt het dialect van? (buurt)",  [validators.Required("Vul alstublieft het dialect in dat u spreekt.")], render_kw={"placeholder": "Spreekt het dialect van? (buurt)"})
  originregion = TextField("Is geboren in..",  [validators.Required("Vul alstublieft het dorp/de stad in waar u het langst bent gewoond.")], render_kw={"placeholder": "'t langste gewoond in? (dorp,stad)"})
  gender = RadioField("Gender", [validators.Required("Selecteer een geslacht alstublieft")], choices=[('man', 'Man'), ('vrouw', 'Vrouw')])
  submit = SubmitField("Ga Verder")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    volunteer = Volunteer.query.filter_by(email = self.email.data.lower()).first()
    if volunteer:
      self.email.errors.append("Dat e-mailadres is al geregistreerd")
      return False
    else:
      return True

class LoginForm(Form):
  emailname = TextField("Email",  [validators.Required("Vul alsjeblieft je volledige naam in."), validators.Email("Please enter your email address.")], render_kw={"placeholder": "Email Adres"})
  login = SubmitField("Inloggen")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    volunteer = Volunteer.query.filter_by(emailname = self.emailname.data.lower()).first()
    if volunteer:
      return True
    else:
      self.emailname.errors.append("Ongeldig e-mail")
      return False