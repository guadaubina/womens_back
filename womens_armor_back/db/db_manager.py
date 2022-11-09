import csv


def save_new_consulta(consulta):
    with open('src/db/consultas.csv', 'a') as orders_file:
        header = ["consulta_id", "nombre", "telefono"]

        writer = csv.DictWriter(orders_file, fieldnames=header)

        if orders_file.tell() == 0:
            writer.writeheader()

        writer.writerow(consulta)


def all_consultas():
    try:
        consultas = []
        with open('db/consultas.csv', 'r') as consultas_file:
            rows = csv.DictReader(consultas_file)

            for row in rows:
                consultas.append()

            return consultas
    except:
        return "No pudimos obtener las consultas"