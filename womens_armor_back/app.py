from flask import Flask, jsonify, request
import os, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return jsonify({"message": "bienvenido Pablo a nuestra API :)"})


@app.route('/api/v1/forms', methods=['GET'])
def ver_consultas():
    path = os.path.join("static", "forms.json")

    if os.path.exists(path):
        with open(path, "r") as file:
            forms = json.load(file)  # convert json object to python object
            return jsonify({"consultas": forms, "message": "Consultas realizadas", "status": "200"})

    return jsonify({"consultas": None, "message": "No se han realizado consultas", "status": "204"})


@app.route('/api/v1/forms', methods=['POST'])
def new_consulta():
    path = os.path.join("static", "forms.json")
    new_form = request.json

    if not os.path.exists(path):
        with open(path, "w") as file:
            forms = list()
            forms.append(new_form)
            json.dump(forms, file, indent=4)  # python dic to json file
            return jsonify({"form": new_form, "message": "Form successfully registered", "status": "201"})

    else:
        with open(path, "r+") as file:
            forms = json.load(file)  # load read JSON FILE to dict. #loads read JSON STRING to dict

            forms.append(new_form)
            file.seek(0)
            json.dump(forms, file, indent=4)  # dump write dic in json file. #dumps convert dic to json string
            return jsonify({"form": new_form, "message": "Form successfully registered", "status": "201"})


@app.route('/api/v1/suscripcion', methods=['POST'])
def new_suscripcion():
    path = os.path.join("static", "suscripciones.json")
    new_form = request.json

    if not os.path.exists(path):
        with open(path, "w") as file:
            forms = list()
            forms.append(new_form)
            json.dump(forms, file, indent=4)  # python dic to json file
            return jsonify({"form": new_form, "message": "Subscription successfully registered", "status": "201"})

    else:
        with open(path, "r+") as file:
            forms = json.load(file)  # load read JSON FILE to dict. #loads read JSON STRING to dict

            forms.append(new_form)
            file.seek(0)
            json.dump(forms, file, indent=4)  # dump write dic in json file. #dumps convert dic to json string
            return jsonify({"form": new_form, "message": "Subscription successfully registered", "status": "201"})

if __name__ == '__main__':
    app.run()

