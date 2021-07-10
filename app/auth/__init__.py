from flask import Blueprint, render_template

bp_auth = Blueprint("auth", __name__, static_folder = "static", template_folder ="templates")

from app.auth import routes
