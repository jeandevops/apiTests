from flask import render_template, Blueprint

jenkins = Blueprint("jenkins_routes", __name__, url_prefix="/jenkins")

@jenkins.route("")
def index():
    return render_template("jenkins.html")

@jenkins.route("/update/<string:name>")
def jenkins_update(name):
    return render_template("jenkins_update.html")