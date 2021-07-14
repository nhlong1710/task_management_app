from flask import Blueprint

bp_meeting = Blueprint("meeting", __name__, static_folder = "static", template_folder ="templates")

from app.meeting import routes
