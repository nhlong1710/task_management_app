from flask import Blueprint, render_template

bp_main = Blueprint("main", __name__, static_folder = "static", template_folder ="templates")

from app.main import routes
