from flask import Blueprint, render_template

docker = Blueprint("docker_routes", __name__,url_prefix="/docker")

@docker.route("")
def get_containers():
    return render_template("docker.html")