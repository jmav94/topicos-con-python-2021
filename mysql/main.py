import mysql.connector

# Conexion

database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "python_db"
)

# Validar conexion
#print(database)

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

"""
cursor.execute("SHOW TABLES")

for table in cursor:
  print (table)
"""

# Insert
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Honda', 'Accord', 30000)")
"""
autos = [
  ('Honda', 'Civic', 28000),
  ('Audi', 'A4', 60000),
  ('BMW','X7', 50000),
  ('Kia','Sorento', 40000)
]

cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)", autos)

database.commit();
"""

# Listar/ Mostrar

cursor.execute("SELECT * FROM vehiculos")

resultado = cursor.fetchall()

print("--- Todos los autos ---")
for auto in resultado:
  print(auto[0],auto[1],auto[2],auto[3])

"""
cursor.execute("SELECT * FROM vehiculos")
auto = cursor.fetchone()
print(auto)
"""

# Borrar / DELETE
"""
cursor.execute("DELETE FROM vehiculos")
database.commit()
"""

# Actualizar / Update
cursor.execute("UPDATE vehiculos SET modelo='a7 sport' WHERE marca = 'Audi'")
database.commit()

print("---- Actualizacion de Datos ----")
print(cursor.rowcount, "Dato actualizado")