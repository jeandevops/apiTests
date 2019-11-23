#ESTE É O SCRIPT QUE STARTA A APLICAÇÃO WEB (EM FLASK)

from flask import (Flask, render_template, Blueprint,
                   request, redirect, session)
# IMPORTA O BLUEPRINT DECLARADO EM ./modulos/dockerm.py (MESMA IDEIA PARA OS OUTROS)
from modulos.dockerm import docker

from modulos.gitlabm import gitlab

from modulos.jenkinsm import jenkins

import logging

from os import urandom

from ldap3 import Server, Connection

server = Server("ldap://localhost:389")

app = Flask(__name__)

# USAMOS BLUEPRINT PARA CHAMAR OUTROS MODULOS (ESTA E A FORMA QUE O FLASK MODULARIZA)
app.register_blueprint(docker)

app.register_blueprint(gitlab)

app.register_blueprint(jenkins)

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s ] %(name)s\n" +
    "[ %(funcName)s ] [%(filename)s, %(lineno)s ] %(message)s",
    datefmt="[ %d-%m-%y-%H-%M-%S]"
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        con = Connection(server, "uid={},dc=dexter,dc=com".format(email), password)
        #@TODO TRATAR SESSÃO VALIDANDO O DISPOSITIVO!!!
        if not con.bind():
            session["auth"] = False
            return redirect("/")
        else:
            session["auth"] = True
            return redirect("/docker")

@app.route("/logout")
def logout_dashboard():
    session["auth"] = False
    return redirect("/")

if __name__ == "__main__":
    # TO PROTECT THE SESSION
    app.secret_key = urandom(12)
    app.run(debug=True, host="0.0.0.0")