import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "locadora_de_veiculos"
)
mycursor = mydb.cursor()

mycursor.execute("select placa from veiculo;")
placa = mycursor.fetchall()

custo = [400, 500, 600, 1000, 1500, 2000, 2500, 3500]

for i in range (1, 21):
    index = r.randint(0, 49)

    mycursor.execute(f"select data_contrato from contrato where placa_do_veiculo = '{placa[index][0]}';")
    data = mycursor.fetchall()
    data = str(data[0][0])
    # print(data)

    dia = r.randint(1, 30); mes = r.randint(1, 12); ano = r.randint(int(data[0:4]), 2022)

    # Caso a ano/mês de manutenção seja o mesmo que o do contrato
    if ano == 2022:
        mes = r.randint(int(data[5:7]), 12)
        if mes == 12:
            dia = r.randint(int(data[8:10]), 30)


    mycursor.execute(f"""insert into manutencao (id_manutencao, placa_do_veiculo, custo_medio_mensal, data_manutencao)
    values ({i}, "{placa[index][0]}", {r.choice(custo)}, '{ano}-{mes}-{dia}');""")
    mydb.commit()

    # print(f"{i}, {placa[index][0]}, {r.choice(custo)}, '{ano}-{mes}-{dia}'")