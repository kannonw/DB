def connect():

    import mysql.connector

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "livraria_if"
    )
    return mydb