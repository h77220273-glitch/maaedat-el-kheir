from Project.home import bp
from flask import render_template,request
from Project.Models import Tables,User

@bp.route('/')
def index():
    tables = Tables.query.all()
    l = []
    for i in tables:
        l.append({
                'name': i.name,
                'desc': i.desc,
                'lat': i.lat,
                'lng': i.lng
            })
            

    return render_template("index.html",tables=l)

@bp.route('/admin')
def admin():
    return render_template("admin.html")

@bp.route('/admin/login',methods=['POST'])
def adminlogin():
    data = User.query.all()
    name = request.form.get('username')
    password = request.form.get('password')
    if name == 'mohamed' and password == 'admin':
        return {'ids':[i.id for i in data],'names':[i.name for i in data],'emails':[i.email for i in data]}
    