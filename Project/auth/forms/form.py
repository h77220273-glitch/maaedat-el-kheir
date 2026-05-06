from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,validators,EmailField
class form(FlaskForm):
    Image = FileField()
    name = StringField("الاسم ",validators=[validators.DataRequired()])
    email = EmailField("البريد الإلكتروني",validators=[validators.DataRequired(),validators.Email()])
    password = StringField("الباسوورد",validators=[validators.DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField("البريد الإلكتروني",validators=[validators.DataRequired(),validators.Email()])
    password = StringField("الباسوورد",validators=[validators.DataRequired()])
    submit  = SubmitField("Submit")

class PasswordEditForm(FlaskForm):
    password = StringField('كلمة المرور الحالية',validators=[validators.DataRequired()])
    new_password= StringField('كلمة المرور الجديدة',validators=[validators.DataRequired()])
    conf_new_pass = StringField("تأكيد كلمة المرور الجديدة",validators=[validators.DataRequired(),validators.EqualTo('new_password')]) 
    submit = SubmitField('تسجيل الدخول')   

class EditForm(FlaskForm):
    name = StringField("اسم المستخدم",validators=[validators.DataRequired()])
    email = EmailField("الايميل",validators=[validators.DataRequired(),validators.Email()])
    image = FileField("الايميل")   