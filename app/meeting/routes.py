from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.meeting import bp_meeting
# from app.auth.forms import LoginForm, RegistrationForm, \
#     ResetPasswordRequestForm, ResetPasswordForm
from app.models import *
from app.meeting.form import *
from app.meeting.email import *
from sqlalchemy import and_

#--------------------------------------------------------
@bp_meeting.route("/create_meeting", methods=["GET", "POST"])
def create_meeting():
    form = createMeetingForm()
    if form.validate_on_submit():
        # add data to meeting table
        meetingName = form.meetingName.data
        meetingDescription = form.meetingDescription.data
        meetingDate = form.meetingDate.data
        meetingStart =  form.meetingStart.data
        meetingEnd = form.meetingEnd.data
        NewMetting= Meeting(meeting_name = meetingName, meeting_description=meetingDescription, meeting_date=meetingDate, meeting_start=meetingStart, meeting_end=meetingEnd)
        db.session.add(NewMetting)

        #add data to meeting_user table and send email
        users = User.query.all()
        for user in users:
            send_meeting_email(user, NewMetting)
            newMeetingUser = Meeting_user(user_id=user.id, meeting_id = NewMetting.id)
            db.session.add(newMeetingUser)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template("create_meeting.html", form=form)

#--------Meeting confirmation------------------------------------------------
@bp_meeting.route('/meeting_confirmation/<meetingId>/<token>', methods=['GET', 'POST'])
def meeting_confirmation(token, meetingId):
    user = User.verify_meeting_confirmation_token(token)

    if not user:
        return redirect(url_for('main.index'))
    form = meetingConfirmationForm()
    meetingUser = Meeting_user.query.filter(and_(Meeting_user.user_id == user.id, Meeting_user.meeting_id == meetingId)).first()
    meeting = Meeting.query.get(meetingId)

    if form.validate_on_submit():
        meetingUser.is_responded = True
        meetingUser.is_attended = bool(form.isAttended.data)
        meetingUser.response_date = datetime.now()
        numberOfResponses = Meeting_user.query.filter(and_(Meeting_user.is_responded == True, Meeting_user.meeting_id == meetingId)).count()
        meeting.number_of_responses = numberOfResponses
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('meeting_confirmation.html', form=form, meetingUser=meetingUser, meeting=meeting)

#--------View all meetings------------------------------------------------
@bp_meeting.route('/view_all_meetings', methods=['GET', 'POST'])
def view_all_meetings():
    meetings = Meeting.query.order_by(Meeting.meeting_date.desc()).all()
    return render_template('view_all_meetings.html', meetings=meetings)

#--------View all meetings------------------------------------------------
@bp_meeting.route('/edit_meeting_details/<meetingId>', methods=['GET', 'POST'])
def edit_meeting_details(meetingId):
    meeting = Meeting.query.get(meetingId)
    form = editMeetingForm(meetingDescription = meeting.meeting_description, meetingNote = meeting.meeting_note)
    return render_template('edit_meeting_details.html', meeting=meeting, form = form)
