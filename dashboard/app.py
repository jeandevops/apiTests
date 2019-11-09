#ESTE É O SCRIPT QUE STARTA A APLICAÇÃO WEB (EM FLASK)

from flask import Flask, render_template, Blueprint
# IMPORTA O BLUEPRINT DECLARADO EM ./modulos/dockerm.py (MESMA IDEIA PARA OS OUTROS)
from modulos.dockerm import docker

from modulos.gitlabm import gitlab

app = Flask(__name__)

# USAMOS BLUEPRINT PARA CHAMAR OUTROS MODULOS (ESTA E A FORMA QUE O FLASK MODULARIZA)
app.register_blueprint(docker)

app.register_blueprint(gitlab)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)