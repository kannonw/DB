import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hospital_veterinario"
)
mycursor = mydb.cursor()

esp = ["cachorro", "gato", "cavalo", "papagaio", "tartaruga", "peixe", "periquito", "lontra", "zebra"]

nomeM = ["Miau", "Auau", "Trovão", "Rex", "Nemo", "Louro", "Solstice", "Charlie", "Terry", "Banana", "Lucky", "Hulk", "Charles", "Merlin", "Harry", "Tarzan", "Troy", "Danny", "Speed", "Stitch"]

nomeF = ["Sandy","Lola", "Melzinha", "Luna",  "Pandora", "Bella", "Joy", "Filipa", "Pedrita", "Tina", "Alegria", "Patty", "Penny", "Bonnie", "Alice", "Dalila", "Natasha"]

enfermidade = ["Língua Azul", "Febre Aftosa", "Encefalomielite Equina", "Encefalopatias Espongiformes Transmissíveis", "Enfermidade Debilitante Crônica", "Erliquiose Bovina","Estomatite Vesicular","Febre Aftosa", "Febre Catarral Maligna","Febre Efêmera Bovina", "Febre Q", "Febres Hemorrágicas por Arenavírus", "Hantavirus", "Hendra", "Infecção pelo Vírus do Nilo Ocidental", "Infecção pelo Virus Menangle"]


for i in range(1, 51):
    n = r.randint(1,2)
    dono = r.randint(1,50)

    if n == 2:
        nome = r.choice(nomeM)
        gen = 'M'
    else:
        nome = r.choice(nomeF)
        gen = 'F'


    mycursor.execute(f"select distinct codigo_cliente from cliente where cliente.pet_cliente = {i};")
    dono_pet = mycursor.fetchall()

    # print(dono_pet[0][0])

    mycursor.execute(f"""insert into pet (codigo_pet, nome_pet, sexo_pet, enfermidade, dono_pet, especie)
    values ({i}, "{nome}", '{gen}', "{r.choice(enfermidade)}", {int(dono_pet[0][0])}, "{r.choice(esp)}");""")
    mydb.commit()

    # print(f"values ({i}, '{nome}'', '{gen}', '{r.choice(enfermidade)}', {dono}, '{r.choice(esp)}')")