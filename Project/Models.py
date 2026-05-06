from Project import db,loginmanager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
@loginmanager.user_loader
def loaduser(id):
    return User.query.get(id)



class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text,unique=True)
    password = db.Column(db.Text)
    Image = db.Column(db.Text)
    tables = db.relationship('Tables',back_populates='provider',lazy=True)
    def __init__(self,name,email,password,Image):
        self.name = name
        self.email = email
        self.password=password
        self.Image=Image
    @property
    def password(self):
        raise AttributeError('Password is not readable')
    @password.setter
    def password(self,text_pass):
        self._password=generate_password_hash(text_pass)

    def checkpass(self,Inserted_password):
        return check_password_hash(self._password,Inserted_password)
    
class Tables(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    provider_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    name = db.Column(db.Text,unique=True)
    desc = db.Column(db.Text)
    loc = db.Column(db.Text)
    lng = db.Column(db.Text,nullable=False)
    lat = db.Column(db.Text,nullable=False)
    provider = db.relationship('User',back_populates='tables')
    __table_args__ = (
    db.UniqueConstraint('lat', 'lng', name='uq_tables_lat_lng'),)
    def __init__(self,provid,name,desc,loc,lng,lat):
        self.provider_id = provid
        self.name = name
        self.desc = desc
        self.loc = loc
        self.lng=lng
        self.lat = lat

