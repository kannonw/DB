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
# Tabela
myTables = []
myCursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='northwind'")
db = myCursor.fetchall()

n = 0
for registro in db:
    print(f"{n+1} - {registro[0]}")
    myTables.insert(n, registro[0])
    n += 1
    if n % 20 == 0:
        input("Aperte 'enter' para continuar a listagem.")

table = input("\nDigite o número ou o nome da tabela: ")

if table.isdigit():
    n = int(table)
    table = myTables[n-1]

listar = input(f"\nGostaria de listar tudo da tabela {table}? (s/n) ")

n = 0
if (listar == 's'):
    try:
        myCursor.execute(f"SELECT * FROM `{table}`")
        dbTable = myCursor.fetchall()
    except:
        print(f"O valor {table} é inválido!")
        
    for registro in dbTable:
        print(registro)
        n += 1
        if n % 20 == 0:
            input("Aperte 'enter' para continuar a listagem.")
    exit()

###################################
# Coluna
myColumns = []
try:
    myCursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = `{table}` AND TABLE_SCHEMA = 'northwind'")
    db = myCursor.fetchall()
except:
    print(f"O valor {table} é inválido!")

n = 0
for registro in db:
    print(f"{n+1} - {registro[0]}")
    myColumns.insert(n, registro[0])
    n += 1
    if n % 20 == 0:
        input("Aperte 'enter' para continuar a listagem.")

column = input("\nDigite o número ou o nome da coluna: ")

if column.isdigit():
    n = int(column)
    column = myColumns[n-1]

listar = input(f"\nGostaria de listar tudo da coluna {column}? (s/n) ")

n = 0
if listar == 's':
    try:
        myCursor.execute(f"SELECT `{column}` FROM `{table}`")
        dbColumn = myCursor.fetchall()
    except:
        print(f"O valor {column} é inválido!")
    for registro in dbColumn:
        print(registro)
        n += 1
        if n % 20 == 0:
            input("Aperte 'enter' para continuar a listagem.")
    exit()

###################################
# Atributo
myAttr = []
try:
    myCursor.execute(f"SELECT `{column}` from `{table}`")
    db = myCursor.fetchall()
except:
    print(f"O valor {column} é inválido!")

n = 0
for registro in db:
    print(f"{n+1} - {registro[0]}")
    myAttr.insert(n, registro[0])
    n += 1
    if n % 20 == 0:
        input("Aperte 'enter' para continuar a listagem.")

attr = input("\nDigite o número ou o nome do atributo: ")

if attr.isdigit():
    n = int(attr)
    attr = myAttr[n-1]

n = 0
myCursor.execute(f"SELECT * from `{table}` where `{column}` like '%{attr}%'")
dbAttr = myCursor.fetchall()
for registro in dbAttr:
    print(registro)
    n += 1
    if n % 20 == 0:
        input("Aperte 'enter' para continuar a listagem.")