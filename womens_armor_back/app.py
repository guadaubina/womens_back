from flask import Flask, jsonify, request
import os
import json
from flask_cors import CORS
import random
# import uuid
from db.db_manager import save_new_consulta

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
            return forms

    return "No se han realizado consultas"


@app.route('/api/v1/forms', methods=['POST'])
def new_consulta():
    path = os.path.join("static", "forms.json")
    new_form = request.json

    if not os.path.exists(path):
        with open(path, "w") as file:
            forms = list()
            forms.append(new_form)
            json.dump(forms, file, indent=4)  # python dic to json file
            save_new_consulta(forms)
            return "El formulario ha sido creado de forma exitosa"
    else:
        with open(path, "r+") as file:
            forms = json.load(file)  # load read JSON FILE to dict. #loads read JSON STRING to dict
            forms.append(new_form)
            file.seek(0)
            json.dump(forms, file, indent=4)  # dump write dic in json file. #dumps convert dic to json string
            save_new_consulta(forms)
            return "El formulario ha sido completado de forma exitosa"


    # with open(path_csv, "w") as my_file:
     # wr = csv.DictWriter(my_file, fieldnames=new_form)
      #  wr.writeheader()
       # wr.writerows(forms_csv)
        #return jsonify({"form": new_form, "message": "FUNCIONA", "status": "201"})

        # with open(path_csv, "w") as my_file:
         #   wr = csv.DictWriter(my_file, fieldnames=new_form)
          #  wr.writeheader()
           # wr.writerows(forms)


@app.route('/api/v1/suscripcion', methods=['POST'])
def new_suscripcion():
    path = os.path.join("static", "suscripciones.json")
    new_form = request.json
    suscripcion_id = random.randint(1, 100)
    new_form["suscripcion_id"]=suscripcion_id

    if not os.path.exists(path):
        with open(path, "w") as file:
            forms = list()
            forms.append(new_form)
            json.dump(forms, file, indent=4)  # python dic to json file
            return "la suscripción ha sido creada de forma exitosa"

    else:
        with open(path, "r+") as file:
            forms = json.load(file)  # load read JSON FILE to dict. #loads read JSON STRING to dict

            forms.append(new_form)
            file.seek(0)
            json.dump(forms, file, indent=4)  # dump write dic in json file. #dumps convert dic to json string
            return "la suscripción ha sido realizada de forma exitosa"


@app.route('/api/v1/suscripcion', methods=['GET'])
def ver_suscripciones():
    path = os.path.join("static", "suscripciones.json")

    if os.path.exists(path):
        with open(path, "r") as file:
            suscripciones = json.load(file)  # convert json object to python object
            return suscripciones

    return "No se ha realizado ninguna suscripcion"


@app.route('/api/v1/suscripcion/<mail>', methods=['DELETE'])
def delete(mail):
    mail_user = mail
    path = os.path.join("static", "suscripciones.json")
    with open(path, "r+") as file:
        suscripciones = json.load(file)
        for suscripcion in suscripciones:
            if suscripcion["mailA"] == mail_user:
                suscripciones.remove(suscripcion)
                with open(path, "w") as file2:
                    file2.write(json.dumps(suscripciones, indent=4))
                    return "tu mail ha sido eliminado"

if __name__ == '__main__':
    app.run()

