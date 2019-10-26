from flask import Flask, render_template, Blueprint
from modulos.dockerm import docker

app = Flask(__name__)
app.register_blueprint(docker)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pessoas")
def get_pessoas():
    usuarios = [
        {"nome": "jean"},
        {"nome": "ota pessoa"},
        {"nome": "mais pessoa"},
        {"nome": "jean2"},
        {"nome": "ota pessoa2"},
        {"nome": "mais pessoa2"},
        ]
    return render_template("teste2.html", context=usuarios)

if __name__ == "__main__":
    app.run(debug=True)