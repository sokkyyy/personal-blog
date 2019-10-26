from flask import render_template,redirect,url_for,flash,request
from . import auth
from .forms import RegistrationForm,LoginForm
from .. import db
from ..models import User,Role
from flask_login import login_user,logout_user,login_required





@auth.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            if user.role.name == "admin":
                return redirect(url_for('admin.index'))
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password.')

    title = "Login"
    return render_template('auth/login.html',title=title,form=form)


@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #choose roles
        if form.email.data == "myemail@gmail.com":
            role= Role(name="admin")
        else:
            role=Role(name="user")

        user = User(username=form.username.data,email=form.email.data,password=form.password.data,role=role)
        user.save_user()

        return redirect(url_for('auth.login'))
    
    title = "Registration"
    return render_template('auth/register.html',title=title,form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))