import mysql.connector

def conectar():
  database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "proyecto_python",
    port = 3306
  )

  cursor = database.cursor(buffered=True)
  cursor = database.cursor()

  return [database, cursor]
