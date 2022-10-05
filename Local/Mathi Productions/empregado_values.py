import mysql.connector
import random as r  

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mathi_productions"
)
mycursor = mydb.cursor()

nome = ["Miguel", "Sophia",	"Davi",	"Alice", "Arthur",	"Julia",	"Pedro",	"Isabella",	"Gabriel",	"Manuela",	"Bernardo",	"Laura",	"Lucas",	"Luiza",	"Matheus",	"Valentina",	"Rafael",	"Giovanna",	"Heitor",	"Maria" ,"Eduarda",	"Enzo",	"Helena", "Guilherme",	"Beatriz",	"Nicolas",	"Maria Luiza",	"Lorenzo",	"Lara",	"Gustavo",	"Mariana",	"Felipe",	"Nicole",	"Samuel",	"Rafaela",	"João Pedro",	"Heloísa",	"Daniel",	"Isadora",	"Vitor"	,"Lívia",	"Leonardo",	"Maria Clara",	"Henrique",	"Ana Clara",	"Theo",	"Lorena",	"Murilo",	"Gabriela",	"Eduardo",	"Yasmin",	"Pedro",	"Isabelly",	"Pietro", "Play Osu Game", "Jorge Gameplays555", "Piton", "Onichan", "Henrique"]

sobrenome = [ "Almeida", "Azevedo", "Braga", "Barros", "Bahiense", "Campos", "Cardoso", "Correia", "Castro", "Costa", "Fontes" , "Guimarães" , "Magalhães" , "Macedo", "Matos", "Pedreira", "Queirós", "Ribeiro", "Rocha", "Siqueira", "Serra", "Souza", "Teixeira", "Valle"]

telefone = ["(64)279-19270", "(63)490-45299", "(61)031-74545", "(62)152-68969", "(61)869-40855", "(63)844-74792", "(62)467-58274", "(61)700-69654", "(63)493-88726", "(62)954-10185", "(62)124-20526", "(64)928-77805", "(63)882-08859", "(61)684-60712", "(62)654-05782", "(61)630-32862", "(63)586-45581", "(62)527-38379", "(61)571-94597", "(63)740-49813", "(62)615-26890", "(62)386-13332", "(64)826-69064", "(63)562-83345", "(61)251-98950", "(62)945-83749", "(61)461-31860", "(63)047-17227", "(62)122-42690", "(61)659-39553", "(63)307-50131", "(62)546-76990", "(62)592-56849", "(64)051-78144", "(63)674-53810", "(61)005-26551", "(62)360-16523", "(61)489-64709", "(63)911-41294", "(62)400-53664", "(61)277-71568", "(63)499-59073", "(62)937-77773", "(62)405-73350", "(64)073-01307", "(63)145-43820", "(61)980-02160", "(62)954-56287", "(61) 281-49504", "(63)906-15846", "(62)4002-8922"]

dic = {
"Animação": ["animador"],
"Direção": ["diretor", "supervisionador", "vice-diretor", "diretor de arte"],
"Storybording": ["diretor", "vice-diretor", "diretor de episódio"],
"Edição": ["editor"],
"Música": ["compositor"],
"Efeitos Sonoros": ["compositor"],
"Design": ["animador", "diretor de arte"],
"Colorização": ["editor"],
"Revisão": ["diretor", "vice-diretor", "diretor de episódio"],
"Roteirização": ["roteirista"]
}

dependente = []

for id in range(1, 51):
    
    num = r.choice(telefone)
    telefone.remove(num)

    dia = r.randint(1, 30); mes = r.randint(1, 12); ano = r.randint(2000, 2020)

    n = r.choice(nome)
    s = r.choice(sobrenome)
    sexo = r.sample(('FM'), 1)

    # Escolhe o cargo apartir de um departamento aleatório
    dep = r.randint(1, 10)
    mycursor.execute(f"select nome_dep from departamento where id_dep = {dep};")
    cargo = mycursor.fetchall()
    c = r.choice(dic[cargo[0][0]])

    # Encolhe um depente que seja diferente do próprio id e que já não tenha sido usado
    depen = r.randint(1, 50)
    while True:
        if depen == id or depen in dependente:
            depen = r.randint(1, 50)
        else:
            break
    dependente.append(depen)

    mycursor.execute(f"""insert into empregados (matricula_emp, nome_emp, sexo_emp, telefone_emp, dependente_emp, dataDeAdmissao_emp, cargo_emp, departamento_emp)
    values ({id}, '{n} {s}', '{sexo[0]}', '{num}', {depen}, '{ano}-{mes}-{dia}', '{c}', {dep});""")
    mydb.commit()

    print(f"values( {id}, '{n} {s}', '{sexo[0]}', '{num}', {depen}, '{ano}-{mes}-{dia}', '{c}', {dep})")