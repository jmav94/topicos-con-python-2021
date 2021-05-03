import mysql.connector

# Conexion

database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "python_db"
)

# Validar conexion
print(database)

# Cursor
cursor = database.cursor(buffered=True)

# Crear Base de datos

cursor.execute("CREATE DATABASE IF NOT EXISTS python_db")
"""
cursor.execute("SHOW DATABASES")

for bd in cursor:
  print(bd)
"""
# Crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
  id int(10) auto_increment not null,
  marca varchar(40) not null,
  modelo varchar(40) not null,
  precio float(10,2) not null,
  CONSTRAINT pk_vehiculo PRIMARY KEY(id)
  )
""")

cursor.execute("SHOW TABLES")

for table in cursor:
  print (table)
