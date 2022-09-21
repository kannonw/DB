import random as r
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hospital_veterinario"
)
mycursor = mydb.cursor()

cliente = []
preco = [100, 200, 250, 350, 400]

for i in range(1, 101):
    c = r.randint(1, 50)

    while True:
        if c in cliente:
            if len(cliente) == 50:
                cliente.clear()
            else:
                c = r.randint(1,50)
        else:
            cliente.append(c)
            break


    dia = r.randint(1, 30); mes = r.randint(1, 12); ano = r.randint(2018, 2022)

    mycursor.execute(f"""insert into consulta (codigo_consulta, codigo_cliente, codigo_veterinario, preco_consulta, data_consulta)
    values ({i}, {c}, {r.randint(1, 15)}, {r.choice(preco)}, '{ano}-{mes}-{dia}');""")
    mydb.commit()