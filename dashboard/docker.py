from flask import Flask, render_template
from modulos.dockerm import docker
from docker import DockerClient

docker = Blueprint("docker_routes", __name__, url_prefix="/docker")
con = DockerClient("tcp://127.0.0.1:2376")

@docker.route("")
def get_containers();
    containers = con.containers.list(all=True)
    print(containers)
    return render_template("docker.html")