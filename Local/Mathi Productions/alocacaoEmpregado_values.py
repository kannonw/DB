import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mathi_productions"
)
mycursor = mydb.cursor()

emp = []

for id in range(10):

    for i in range(5):
        empregado = r.randint(1,50)

        while empregado in emp and len(emp) < 50:
            empregado = r.randint(1,50)
        emp.append(empregado)


        mycursor.execute(f"select dataDeAdmissao_emp from empregados where matricula_emp = {empregado};")
        data = mycursor.fetchall()
        data = str(data[0][0])

        dia = r.randint(1, 30); mes = r.randint(1, 12); ano = r.randint(int(data[0:4]), 2022)

        # Caso a ano/mês de manutenção seja o mesmo que o de admissão
        if ano == 2022:
            mes = r.randint(int(data[5:7]), 12)
            if mes == 12:
                dia = r.randint(int(data[8:10]), 30)


        mycursor.execute(f"""insert into alocacaoEmpregado (id_proj, id_emp, dataDeAlocacao)
        values ({id+1}, {empregado}, '{ano}-{mes}-{dia}');""")
        mydb.commit()

        print(f"values( {id+1}, '{empregado}', '{ano}-{mes}-{dia}')")