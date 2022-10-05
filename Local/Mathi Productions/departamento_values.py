import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mathi_productions"
)
mycursor = mydb.cursor()

chefe = []
dep = ["Animação", "Direção", "Storybording", "Roteirização", "Edição", "Música", "Efeitos Sonoros", "Design", "Colorização", "Revisão"]

for id in range(10):
    
    ch = r.randint(1,50)

    while ch in chefe:
        ch = r.randint(1,50)

    chefe.append(ch)

    sigla_dep = dep[id][:3]

    mycursor.execute(f"""insert into departamento (id_dep, nome_dep, sigla_dep, chefe_dep)
    values ({id+1}, '{dep[id]}', '{sigla_dep}', {ch});""")
    mydb.commit()

    print(f"values( {id+1}, '{dep[id]}', '{sigla_dep}', {ch})")