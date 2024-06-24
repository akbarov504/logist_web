from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField, FloatField

class OfferForm(FlaskForm):
    price = FloatField(label="Enter offer price")
    month = IntegerField(label="Enter month")
    is_active = BooleanField(label="Is active", default=True)
    submit = SubmitField(label="Submit")
