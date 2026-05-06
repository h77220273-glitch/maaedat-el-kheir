from Project.auth import bp
from flask import render_template,redirect,flash,url_for,request
from Project.auth.forms.form import form as CreateAccount
from Project.auth.forms.form import LoginForm,PasswordEditForm,EditForm
from Project.Models import User,Tables
import os
from flask_login import login_user,logout_user,login_required,current_user
from Project import app,db

@bp.route('/register',methods=["POST",'GET'])
def register():
    form = CreateAccount()
    if form.validate_on_submit():
        image = form.Image.data
        name = form.name.data
        email = form.email.data
        password=form.password.data
        if image:
            filepath = os.path.join(app.root_path,'static','userpictures')
            os.makedirs(filepath,exist_ok=True)
            file = os.path.join(filepath,image.filename)
            image.save(file)
            userobj = User(name,email,password,image.filename)
            db.session.add(userobj)
            db.session.commit()
        else:
            userobj = User(name,email,password,'no img')
            db.session.add(userobj)
            db.session.commit()
        flash("You Created Account Successfully",category='Info')
        return redirect(url_for('auth.login'))
    return render_template('create.html',form=form)

@bp.route('/login',methods=["POST","GET"])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        email = loginform.email.data
        password = loginform.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if user.checkpass(password):
                flash("لقد سجلت دخولك بنجاح",category='Login')
                login_user(user)
                next = request.args.get('next')
                if next:
                    return redirect(url_for(next))
                return redirect('/auth/myaccount')
            else:
                return 'الباسوورد خاطئ'
        else:
            return 'لا يوجد حساب مسجل لهذا الايميل'    

    return render_template('login.html',form=loginform)

@login_required
@bp.route('/myaccount',methods=["POST",'GET'])
def myaccount():
    user= User.query.get(current_user.id)
    tables = user.tables
    form = PasswordEditForm()
    if form.validate_on_submit():
        password = form.password.data
        new_pass = form.new_password.data
        if user.checkpass(password):
            user.password=new_pass
            db.session.commit()
            flash('تم تغيير الباسوورد بنجاح',category='passinfo')
            return redirect('/auth/myaccount')
        else:
            return "الباسوورد الذي ادخلته لا يطابق باسوورد حسابك"
    
    return render_template("account.html",img=user.Image,tables=tables,form=form)

@bp.route('/edit',methods=['POST','GET'])
def edit():
    edit = EditForm()
    user = User.query.get(current_user.id)
    if edit.validate_on_submit():
        name = edit.name.data
        email = edit.email.data
        image = edit.image.data
        if image:
            path = os.path.join(app.root_path,'static','userpictures')
            imagepath = os.path.join(path,image.filename)
            image.save(imagepath)
            #قولت احذف القديمة طلما هغير الصورة واحفظ الجديدة
            if user.Image != 'no img':
                os.remove(os.path.join(path,user.Image))

        else:
            image='no img'    
        user.name = name
        user.email=email
        user.Image=image.filename
        db.session.commit()
        return redirect('/auth/myaccount')
    return render_template('edit.html',form=edit)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect('/')

