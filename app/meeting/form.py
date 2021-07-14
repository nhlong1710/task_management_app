from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, TimeField, DateField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from app.models import *
from datetime import datetime, timedelta, date
from wtforms.fields.html5 import DateField, TimeField

class MeetingForm(FlaskForm):

    meetingName = StringField('Meeting Name', validators=[DataRequired()])
    meetingDescription = TextAreaField('Description', validators = [DataRequired()])
    meetingDate = DateField(label='Meeting Date',format='%Y-%m-%d', default = date.today,validators = [DataRequired('please select date')])
    meetingStart = TimeField('Starting Time',format='%H:%M')
    meetingEnd = TimeField('Ending Time',format='%H:%M')


class createMeetingForm(MeetingForm):

    submit = SubmitField('Create and send email')

class meetingConfirmationForm(FlaskForm):

    isAttended = SelectField('Trả lời', choices = [(True, "Tham gia"), (False, "Không tham gia được")])
    submit = SubmitField('Confirm')

class editMeetingForm(MeetingForm):

    meetingNote = TextAreaField('Note', validators = [DataRequired()])
    submit = SubmitField('Update')
