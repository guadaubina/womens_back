import csv


def save_new_consulta(consulta):
    with open("./forms.csv", "a") as my_file:
        header = ["nombre", "dni", "telefono", "mail", "dia", "hora", "sucesos"]
        wr = csv.DictWriter(my_file, fieldnames=header)

        if my_file.tell() == 0:
            wr.writeheader()

        wr.writerows(consulta)



#def all_consultas():
 #   try:
  #      consultas = []
   #     with open('db/consultas.csv', 'r') as consultas_file:
    #        rows = csv.DictReader(consultas_file)

     #       for row in rows:
      #          consultas.append()

       #     return consultas
    #except:
     #   return "No pudimos obtener las consultas"