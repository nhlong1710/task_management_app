from app import db
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime, timedelta

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    staff_id= db.Column(db.String, nullable=False, unique=True)
    fullname = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)
    title = db.Column(db.String)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, passwordInput):
        self.password = generate_password_hash(passwordInput)

    def check_password(self, passwordInput):
        return check_password_hash(self.password, passwordInput)

class Meeting(db.Model):
    __tablename__ = "meeting"
    id = db.Column(db.Integer, primary_key=True)
    meeting_name = db.Column(db.String)
    meeting_desription = db.Column(db.String)
    meeting_date = db.Column(db.Date)
    meeting_start = db.Column(db.Float)
    meeting_end = db.Column(db.Float)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime)
    note = db.Column(db.String)

class Meeting_user(db.Model):
    __tablename__ = "meeting_user"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    meeting_id = db.Column(db.Integer, db.ForeignKey("meeting.id"), nullable=False)
    is_responded = db.Column(db.Boolean, default=False)
    response_date = db.Column(db.DateTime)
    note = db.Column(db.String) # store reason of not is_attended
    is_attended = db.Column(db.Boolean)
    is_ontime = db.Column(db.Boolean)

class Attachment(db.Model): #parrent class for attachment
    __abstract__ = True # to not generate table
    attachment_type = db.Column(db.String)
    attachment_name = db.Column(db.String)
    attachment_path = db.Column(db.String)
    attachment_note = db.Column(db.String)

class Meeting_Attachement(Attachment):
    __tablename__ = "meeting_attachement"
    id = db.Column(db.Integer, primary_key=True)
    meeting_id = db.Column(db.Integer, db.ForeignKey("meeting.id"), nullable=False)

class Task(db.Model): # task
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String)
    desription = db.Column(db.String)
    staff_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    expired_date = db.Column(db.DateTime)
    note = db.Column(db.String)

class Task_Attachement(Attachment):
    __tablename__ = "task_attachement"
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"), nullable=False)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
