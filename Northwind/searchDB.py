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
def select(listSearch, type, printAll):
    if type == "table":
        if printAll:
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
        if printAll:
            myCursor.execute(f"SELECT `{listSearch[1]}` from `{listSearch[0]}`")
            db = myCursor.fetchall()
            printDB(db)
            exit()
        else:
            myCursor.execute(f"SELECT `{listSearch[1]}` from `{listSearch[0]}`")
            db = myCursor.fetchall()
            printDB(db)
            return db
    elif type == "attr":
        myCursor.execute(f"SELECT * from `{listSearch[0]}` where `{listSearch[1]}` like '%{listSearch[2]}%'")
        db = myCursor.fetchall()
        printDB(db)
        return db

def printDB(db):
    n = 0
    for registro in db:
        print(f"{n+1} - {registro}")
        n += 1
        if n % 20 == 0:
            continueList = input("\nAperte 'enter' para continuar a listagem.\nParece encerrar a listagem aperte 'e': ")
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

def tolistAll(toList):
    if toList == 's' or toList == 'S':
        printAll = True
    else:
        printAll = False
    return printAll

###################################
# Tabela
myCursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='northwind'")
db = myCursor.fetchall()
printDB(db)

itExists = False
table = ""
while itExists == False:
    var = input("\nDigite o número ou o nome da tabela: ")
    inputDB = inputUser(var, itExists)
    table = inputDB[0]
    itExists = inputDB[1]

listSearch = []
listSearch.append(table)
toList = input(f"\nGostaria de listar tudo da tabela {table}? (s/n) \nOBS: O programa irá encerrar caso escolha 's': ")

printAll = tolistAll(toList)

db = select(listSearch, "table", printAll)

###################################
# Coluna
column = ""
itExists = False
while itExists == False:
    var = input("\nDigite o número ou o nome da coluna: ")
    inputDB = inputUser(var, itExists)
    column = inputDB[0]
    itExists = inputDB[1]

listSearch.append(column)
toList = input(f"\nGostaria de listar tudo da coluna {column}? (s/n) \nOBS: O programa irá encerrar caso escolha 's': ")

printAll = tolistAll(toList)

db = select(listSearch, "column", printAll)

###################################
# Atributo
attr = ""
itExists = False
while itExists == False:
    var = input("\nDigite o número ou o nome da atributo: ")
    inputDB = inputUser(var, itExists)
    attr = inputDB[0]
    itExists = inputDB[1]

listSearch.append(attr)
db = select(listSearch, "attr", printAll)