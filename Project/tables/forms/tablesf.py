from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,validators

class AddTable(FlaskForm):
    name = StringField('اسم المائدة',validators=[validators.DataRequired()])
    description = TextAreaField('الوصف',validators=[validators.DataRequired()])
    location = StringField("العنوان",validators=[validators.DataRequired()])
    lat = StringField("lat")
    lng = StringField("lng")
    submit = SubmitField("اضف مائدة جديدة")
    