from flask import render_template, Blueprint
import gitlab

gl = gitlab.Gitlab('http://localhost:5001', private_token='cMTFUxSpRBptYFbeEKxQ')

gitlab = Blueprint("gitlab_routes", __name__, url_prefix="/gitlab")

@gitlab.route("")
def index():
    all_usr = gl.users.list()
    all_proj = gl.projects.list()
    return render_template("gitlab.html", users=all_usr, projs=all_proj)