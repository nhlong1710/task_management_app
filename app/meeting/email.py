from flask_mail import Message
from app import mail
from flask import render_template, current_app

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_meeting_email(user, meeting):
    token = user.get_meeting_confirmation_token()
    meetingId = meeting.id
    send_email('Thư mời thầy/cô tham gia cuộc họp ' + meeting.meeting_name + ' vào ngày ' + str(meeting.meeting_date),
               sender="nhlong.study@gmail.com",
               recipients=[user.email],
               # text_body=render_template('email/reset_password.txt',
               #                           user=user, token=token),
               text_body="",
               html_body=render_template('meeting_invatation.html',
                                         user=user, meeting = meeting, meetingId=meetingId, token=token))
