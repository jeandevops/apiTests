from flask import Flask, jsonify, request
from pymongo import MongoClient, errors

app = Flask(__name__)
con = MongoClient()
db = con['4linux']

@app.route('/cadastro/<nome>', methods=['POST'])
def index(nome):
    return jsonify({"api":nome}), 202

@app.route('/pessoas/<int:id>', methods=['GET','DELETE','PUT'])
#@app.route('/usuarios/<int:id>', methods=['GET','DELETE']) DARIA PRA ADICINONAR DUAS ROTAS PARA UMA FUNCTION
def adm_pessoa_p_id(id):
    if request.method == "GET":
        pessoa = db.pessoas.find_one({"_id": id})
        if pessoa:
            return jsonify(pessoa), 200
        else:
            return jsonify({}), 404
    elif request.method == "DELETE":
        #NECESSARIO PRA SABER COMO EH A RESPOSTA DO MONGO (o que não estiver entre aspas eh inteiro):
        #print(db.pessos.find_one({"_id": id}))
        delete = db.pessoas.remove({"_id": id})
        # Colocar o retorno do comando em variável, permite coisas legais tipo:
        if delete["n"]:
            return jsonify({"delete": "ok"}), 200
        else:
            return jsonify({"delete": "fail"}), 404
    elif request.method == "PUT":
        raw_data = request.get_json()
        update = db.pessoas.update({"_id": id}, {"$set": raw_data})
        #print(update)    #gerou a ideia de tratamento abaixo:
        if update["n"]:
            return jsonify({"update": "ok"}), 200
        else:
            return jsonify({"update": "fail"}), 404

@app.route('/pessoas', methods=['GET','POST'])
def get_and_reg_pessoas():
    if request.method == "GET":
        pessoas = list(db.pessoas.find())
        return jsonify(pessoas)
    elif request.method == "POST":
        try:
            raw_data = request.get_json()
            db.pessoas.insert(raw_data)
            return jsonify({"register": "ok"}), 201
        except errors.DuplicateKeyError:
            return jsonify({"register": "fail", "error": "DuplicateKeyError"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)