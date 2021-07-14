from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.auth import bp_auth
# from app.auth.forms import LoginForm, RegistrationForm, \
#     ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
from app.auth.form import *
from datetime import datetime, timedelta
#--------------------------------------------------------
# @bp_auth.route("/", methods=["GET", "POST"])
# def index():
#     return "HELLO"
@bp_auth.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.record_last_access()
#----------sign up ----------------
@bp_auth.route("/wtf_signUp_s1", methods=["GET", "POST"])
def wtf_signUp_s1():
    """show sign up form"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = signUpForm()
    if form.validate_on_submit():
        # userId = form.userId.data
        staffId = form.staffId.data
        title = form.title.data
        fullName =  form.fullName.data
        password = form.password.data
        email = form.email.data
        NewUser= User(staff_id = staffId, title=title, fullname=fullName, password=password, email=email)
        NewUser.set_password(form.password.data)
        db.session.add(NewUser)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template("wtf_signUp_s1.html", form=form)

#----------Login ----------------
@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(staff_id=form.staffId.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('nhap lai mat khau hoac tai khoan')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Sign In', form=form)

#---------- Logout ----------------
@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

#----------view Profile ----------------
@bp_auth.route("/view_profile", methods=["GET", "POST"])
@login_required
def view_profile():
    return render_template("view_profile.html")
#----------Edit Profile ----------------
@bp_auth.route("/edit_profile_s1", methods=["GET", "POST"])
@login_required
def edit_profile_s1():
    """show sign up form"""
    form = editProfileForm(title=current_user.title)
    if form.validate_on_submit():
        # userId = form.userId.data
        current_user.staffId = form.staffId.data
        current_user.title = form.title.data
        current_user.fullName =  form.fullName.data
        current_user.email = form.email.data
        current_user.updated_time = datetime.now()
        db.session.commit()
        flash('Your profile has been editted')
        return redirect(url_for('main.index'))
    return render_template("edit_profile_s1.html", form=form, current_user=current_user)

#---------- view all users ----------------
@bp_auth.route('/view_users')
def view_users():
    staffs = User.query.all()
    return render_template("view_users.html", staffs=staffs)
