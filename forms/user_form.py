from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

class LoginForm(FlaskForm):
    phone_number = StringField(label="Enter your Phone number")
    password = PasswordField(label="Enter your password")
    submit = SubmitField(label="Login")

class ReceptionForm(FlaskForm):
    first_name = StringField(label="Enter reception first name")
    last_name = StringField(label="Enter reception last name")
    phone_number = StringField(label="Enter reception phone number")
    password = StringField(label="Enter reception password")
    is_active = BooleanField(label="Is active", default=True)
    submit = SubmitField(label="Submit")
