def bd_connector():
    import mysql.connector
    import random as r

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "iftm"
    )
    return mydb