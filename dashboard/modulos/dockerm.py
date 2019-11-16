from flask import render_template, Blueprint, redirect
from docker import DockerClient

# NESTE EXEMPLO NOS JA DECLARAMOS O url_prefix, POR ISSO O PARAMETRO DO @docker.route() está vazio
docker = Blueprint("docker_routes", __name__, url_prefix="/docker")
# CHANGE TO DOCKER ENGINE MACHINE DNS/IP
con = DockerClient("tcp://localhost:2376")

# ESTA ROTA JA TEM A RAIZ PADRAO COMO /docker (DECLARADO ACIMA)
@docker.route("")
# NOME DA FUNCAO
def get_containers():
    # OBTEM A LISTA DE CONTAINERS NO OBJETO containers (ESTE OBJETO POSSUI FUNCOES PROPRIAS DO MODULO DOCKER, E SERAO USADOS NA PAGINA docker.html)
    containers = con.containers.list(all=True)
    # ENVIA O RESULTADO PARA A PAGINA docker.html NA FORMA DA VARIAVEL ctrs
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