from flask import render_template, Blueprint, redirect
from docker import DockerClient

docker = Blueprint("docker_routes", __name__, url_prefix="/docker")
con = DockerClient("tcp://127.0.0.1:2376")

@docker.route("")
def get_containers():
    containers = con.containers.list(all=True)
    return render_template("docker.html", ctrs=containers)

#TODAS AS ROTAS DESTE PREFIXO COMECAM COM "/docker", LOGO A ROTA ABAIXO É PARA /docker/start
@docker.route("/start/<short_id>")
def start_containers(short_id):
    con.containers.get(short_id).start()
    return redirect("/docker")

@docker.route("/stop/<short_id>")
def stop_containers(short_id):
    con.containers.get(short_id).stop()
    return redirect("/docker")