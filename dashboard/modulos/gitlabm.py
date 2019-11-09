from flask import render_template, Blueprint

gitlab = Blueprint("gitlab_routes", __name__, url_prefix="/gitlab")

@gitlab.route("")
def index():
    return render_template("gitlab.html")