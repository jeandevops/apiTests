from flask import render_template, Blueprint, redirect, request
from jenkins import Jenkins as jenkins_con
from time import sleep

jenkins = Blueprint("jenkins_routes", __name__, url_prefix="/jenkins")
con = jenkins_con('http://localhost:8080/', username='jenkins', password='jenkins')

@jenkins.route("")
def index():
    #CHANGE TO JENKINS MACHINE NAME/IP
    jobs = con.get_all_jobs()
    return render_template("jenkins.html", jobs=jobs)

@jenkins.route("/build/<string:name>")
def jenkins_build(name):
    con.build_job(name)
    logging.info("update build {}".format(name))
    sleep(5)
    return redirect("/jenkins")

@jenkins.route("/update/<string:name>")
def jenkins_update(name):
    xml = con.get_job_config(name)
    return render_template("jenkins_update.html", job_name=name, xml=xml)

@jenkins.route("/reconfig/<string:name>", methods=["POST"])
def jenkins_reconfigure(name):
    con.reconfig_job(name, request.form["xml"])
    return redirect("/jenkins")