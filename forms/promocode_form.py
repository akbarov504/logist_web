from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField

class PromocodeForm(FlaskForm):
    name = StringField(label="Enter promo code name")
    publish_day = IntegerField(label="Enter publish day")
    is_active = BooleanField(label="Is active", default=True)
    submit = SubmitField(label="Submit")
