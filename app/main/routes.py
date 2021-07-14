from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.main import bp_main
# from app.auth.forms import LoginForm, RegistrationForm, \
#     ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
# from app.auth.form import loginForm, signUpForm

#--------------------------------------------------------
@bp_main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
