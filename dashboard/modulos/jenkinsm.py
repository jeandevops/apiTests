from flask import render_template, Blueprint
from jenkins import Jenkins as jenkins_con

jenkins = Blueprint("jenkins_routes", __name__, url_prefix="/jenkins")
#CHANGE TO JENKINS MACHINE NAME/IP
con = jenkins_con('http://localhost:8080/', username='jenkins', password='jenkins')

@jenkins.route("")
def index():
    jobs = con.get_all_jobs()
    return render_template("jenkins.html", jobs=jobs)

@jenkins.route("/update/<string:name>")
def jenkins_update(name):
    return render_template("jenkins_update.html")
