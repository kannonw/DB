from ast import While
from curses.ascii import *
from doctest import register_optionflag
from sys import excepthook
import mysql.connector  

mydb = mysql.connector.connect(
    host = "relational.fit.cvut.cz",
    user = "guest",
    password = "relational",
    database = "northwind"
)
myCursor = mydb.cursor()

###################################
# Funções
def select(listSearch, type, boolUserChoice):
    if type == "table":
        if boolUserChoice:
            myCursor.execute(f"SELECT * FROM `{listSearch[0]}`")
            db = myCursor.fetchall()
            printDB(db)
            exit()
        else:
            myCursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{listSearch[0]}' AND TABLE_SCHEMA = 'northwind'")
            db = myCursor.fetchall()
            printDB(db)
            return db
    elif type == "column":
        if boolUserChoice:
            myCursor.execute(f"SELECT {listSearch[1]} from `{listSearch[0]}`")
            db = myCursor.fetchall()
            printDB(db)
            exit()
        else:
            myCursor.execute(f"SELECT {listSearch[1]} from `{listSearch[0]}`")
            db = myCursor.fetchall()
            printDB(db)
            return db
    elif type == "attr":
            myCursor.execute(f"SELECT * from {listSearch[0]} where `{listSearch[1]}` like '{listSearch[2]}'")
            db = myCursor.fetchall()
            printDB(db)
            return db

def printDB(db):
    n = 0
    
    if len(db) == 0:
        input("\nEssa lista está vazia.")
        exit()
    else:
        input(f"\nForam encontrados {len(db)} resultados. Pressione 'enter' para listar: ")

    for registro in db:
        print(f"{n+1} - {registro}")
        n += 1
        if n % 20 == 0:
            continueList = input("\nAperte 'enter' para continuar a listagem.\nPara encerrar a listagem aperte 'e': ")
            if continueList == 'e' or continueList == 'E':
                break

def inputUser(var, itExists):
    n = 0
    var = var.strip()
    for registro in db:
        if var == registro[0] or str(n+1) == var:
            var = registro[0]
            itExists = True
            return var, itExists
        n += 1
    # if var.isDigit():
    #     n = int(var)
    #     var = db[n-1][0]
    # Usado anteriormente

    if itExists == False:
        print(f"Erro! Valor '{var}' não é válido")
        return var, itExists

def booleanUserList(toList):
    while True:
        if toList == 's' or toList == 'S':
            boolUserChoice = True
            return boolUserChoice
        elif toList == 'n' or toList == 'N':
            boolUserChoice = False
            return boolUserChoice
        else:
            toList = input("Insira um valor válido (s/n): ")

def which(type):
    itExists = False
    while itExists == False:
        var = input(f"\nDigite o número ou o nome da {type}: ")
        inputDB = inputUser(var, itExists)
        itExists = inputDB[1]
    type = inputDB[0]
    return type

###################################
# Tabela
myCursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='northwind'")
db = myCursor.fetchall()
i=1
for registro in db:
    print(f"{i} - {registro[0]}")
    i += 1

# Requisita o usuário o número ou o nome da tabela
table = "tabela"
table = which(table)

# Lista para armazenar os inputs do usuário e facilitar no método select()
listSearch = []
listSearch.append(table)
toList = input(f"\nGostaria de listar tudo da tabela {table}? (s/n) \nOBS: O programa irá se encerrar caso escolha 's': ")

# Verifica se o usuário deseja imprimir os dados
boolUserChoice = booleanUserList(toList)
# Faz o select
db = select(listSearch, "table", boolUserChoice)

###################################
# Coluna
# Requisita o usuário o número ou o nome da coluna
columnString = "coluna"
column = which(columnString)

toList = input("\nDeseja adicionar colunas a pesquisa? \nOBS: O programa se encerrará após ter escolhido e listado as colunas (s/n) ")
addColumn = booleanUserList(toList)

if addColumn == True:
    while True:
        b = which(columnString)
        column = column + ", " + b
        toList = input("\nDeseja continuar? (s/n) ")
        toList = booleanUserList(toList)

        if toList == False:
            listSearch.append(column)
            myCursor.execute(f"SELECT {listSearch[1]} from `{listSearch[0]}`")
            db = myCursor.fetchall()
            printDB(db)
            exit()

listSearch.append(column)
toList = input(f"\nGostaria de listar tudo da coluna {column}? (s/n) \nOBS: O programa irá se encerrar caso escolha 's': ")

# Verifica se o usuário deseja imprimir os dados
boolUserChoice = booleanUserList(toList)
# Faz o select
db = select(listSearch, "column", boolUserChoice)

###################################
# Atributo
# Requisita o usuário o número ou o nome do atributo
attr = "atributo"
attr = which(attr)

listSearch.append(attr)
# Faz o select
db = select(listSearch, "attr", boolUserChoice)