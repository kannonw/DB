import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "locadora_de_veiculos"
)
mycursor = mydb.cursor()

preco = [50, 100, 150, 200]
seguro = [1500, 1600, 1700, 2200, 1800, 1200, 1300, 1900]

mycursor.execute(f"select placa from veiculo;")
placa = mycursor.fetchall()

mycursor.execute(f"select cpf from cliente;")
cpf = mycursor.fetchall()

for i in range(1, 51):

    dia = r.randint(1, 30); mes = r.randint(1, 12); ano = r.randint(2010, 2022)

    mycursor.execute(f"""insert into contrato (id_contrato, data_contrato, preco_da_diaria, placa_do_veiculo, cpf_cliente, valor_do_seguro)
    values ({i}, '{ano}-{mes}-{dia}', {r.choice(preco)}, "{placa[i-1][0]}", "{cpf[i-1][0]}", {r.choice(seguro)});""")
    mydb.commit()

    # print(f"{i}, '{ano}-{mes}-{dia}', {r.choice(preco)}, {placa[i-1][0]}, {cpf[i-1][0]}, {r.choice(seguro)}")