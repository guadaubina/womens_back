import csv


def save_new_consulta(consulta):
    with open("./forms.csv", "a") as my_file:
        header = ["nombre", "dni", "telefono", "mail", "dia", "hora", "sucesos"]
        wr = csv.DictWriter(my_file, fieldnames=header)

        if my_file.tell() == 0:
            wr.writeheader()

        wr.writerows(consulta)
