import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mathi_productions"
)
mycursor = mydb.cursor()

proj = ["Turma da Mônica 2", "Naruto Adulto Dublado", "Carrinhos", "Benio", "Meninos Superpoderosos", "Shrek 6", "Little stuart, bad ending", "7", "8", "9"]


for id in range(10):

    mycursor.execute(f"""insert into projetos (id_proj, titulo, horasPrevistas_proj)
    values ({id+1}, '{proj[id]}', {r.choice([500, 600, 700, 800])});""")
    mydb.commit()

    print(f"values( {id+1}, '{proj[id]}', {r.choice([500, 600, 700, 800])}")