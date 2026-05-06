from Project.tables import bp 
from flask_login import login_user,login_required,current_user
from flask import redirect,render_template,url_for
from Project.tables.forms.tablesf import AddTable 
from Project.Models import Tables
from Project import db

@login_required
@bp.route('/addtable',methods=["POST",'GET'])
def addtable():
    add = AddTable()
    if add.validate_on_submit():
        name = add.name.data
        current_user_id = current_user.id
        desc = add.description.data
        loc = add.location.data
        lat = add.lat.data
        lng = add.lng.data
        table = Tables(current_user_id,name,desc,loc,lng,lat)
        db.session.add(table)
        db.session.commit()
        return redirect('/auth/myaccount')
        
    return render_template('add.html',form=add)

@login_required
@bp.route('/edit/<int:id>',methods=["POST","GET"])
def edittable(id):
    table = Tables.query.get(id)
    form = AddTable()
    if table.provider_id == current_user.id:
        if form.validate_on_submit():
            
            name= form.name.data
            desc = form.description.data
            location = form.location.data
            lat = form.lat.data
            lng = form.lng.data
            
            table.name=name
            table.desc = desc
            table.loc = location
            table.lat = lat
            table.lng = lng
            
            db.session.commit()           
            return redirect('/auth/myaccount')
        
        return render_template('khair.html',table=table,form=form)
@login_required    
@bp.route('/delete/<int:id>')
def deletetable(id):
    table = Tables.query.get(id)
    print(table.provider_id,current_user.id)
    if table.provider_id == current_user.id:
        db.session.delete(table)
        db.session.commit()
        return redirect('/auth/myaccount')
    else:
        return "ليس لك صلاحية على المائدة"

