from flask import Flask, render_template, Blueprint
from modulos.dockerm import docker

app = Flask(__name__)
app.register_blueprint(docker)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)