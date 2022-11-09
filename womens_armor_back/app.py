from flask import Flask, jsonify, request
import os, json
from flask_cors import CORS
from db.db_manager import save_new_consulta, all_consultas


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return jsonify({"message": "Welcome to xxx API!!"})


@app.route('/api/v1/forms', methods=['POST'])
def new_consulta():
    path = os.path.join("static", "forms.json")

    if request.method == "GET":
        if os.path.exists(path):
            with open(path, "r") as file:
                forms = json.load(file)  # convert json object to python object
                return jsonify({"users": forms, "message": "Users database loaded successfully", "status": "200"})

        return jsonify({"users": None, "message": "Users database empity", "status": "204"})


    if request.method == "POST":
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




@app.route("/forms", methods=["GET"])
def show_consultas():
    data = all_consultas()
    return data


if __name__ == '__main__':
    app.run()

