from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from app.models import User

class signUpForm(FlaskForm):
    # userId = StringField('User Id', validators=[DataRequired(), Length(min=5, message=('Your id is too short.'))])
    staffId = StringField('Staff Id', validators=[DataRequired()])
    title = SelectField('title', choices = ['KS', 'THS', 'TS', 'PGS.TS', 'GS.TS' ], validators = [DataRequired()])
    fullName = StringField('Full Name', validators=[DataRequired()])
    password = PasswordField('Password',  validators=[DataRequired(), Length(min=8, message=('Your password is too short.'))])
    rePassword = PasswordField('reType Password',  validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    email = StringField('Email',  validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_userId(self, userId):
        userId = User.query.filter_by(id=userId.data).first()
        if userId is not None:
            raise ValidationError('username has been already used! Please use a different username.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('email has been already used! Please use a different email.')

class loginForm(FlaskForm):
    staffId = StringField('STAFF ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
