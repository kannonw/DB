import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "locadora_de_veiculos"
)
mycursor = mydb.cursor()

string = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num = ("0123456789")

cor = ["azul", "vermelho", "preto", "prata", "branco", "amarelo", "roxo", "verde", "rosa", "cinza"]

carro = [
    # marca, modelo, combustivel
    ["Chevrolet", "Camaro 6.2 SS", "Gasolina"],
    ["Volkswagen", "Gol 1.6", "Flex"],
    ["FIAT", "Fiat Argo", "Flex"],
    ["Chevrolet", "Celta LT 1.0", "Flex"],
    ["Peugeot", "208 1.0", "Flex"],
    ["Toyota", "Corolla", "Flex"],
    ["Honda", "Civic 2.0", "Flex"],
    ["Toyota", "Hilux", "Diesel"],
    ["Nissan", "Frontier", "Diesel"],
    ["Hyundai", "HB20", "Flex"],
    ["Volkswagen", "T-Cross 1.0 200 TSI (Aut)", "Flex"]
]


for i in range(1, 51):

    index = r.randint(0, len(carro)-1)
    marca = carro[index][0]
    modelo = carro[index][1]
    combustivel = carro[index][2]

    placa0 = "".join(r.sample(string, 3))
    placa1 = "".join(r.sample(num,2))
    placa = placa0 + r.choice(num) + r.choice(string) + placa1

    mycursor.execute(f"""insert into veiculo (placa, marca, modelo, cor, combustivel)
    values ("{placa}", "{marca}", "{modelo}", "{r.choice(cor)}", "{combustivel}");""")
    mydb.commit()

    # print(f"{placa}, {marca}, {modelo}, {r.choice(cor)}, {combustivel});")