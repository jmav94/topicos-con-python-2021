import datetime
import haslib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Usuario:
  def __init__(self,nombre,apellidos,email,password):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.password = password

  def registrar(self):
    fecha = datetime.datetime.now()

    # Cifrar contraseña
    cifrado = haslib.sha256()
    cifrado.update(self.password.encode('utf8'))

    sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"

    usuario = (self.nombre,self.apellidos,self.email, cifrado.hezdigest(),fecha)

    try:
      cursor.execute(sql, usuario)
      database.commit()
      result = [cursor.rowcount,self]
    except:
      result = [0,self]

    return result

  def login(self):

    # Consulta para comprobar si el usuario ingresado existe
    sql = "SELECT email,password FROM usuarios WHERE email = %s AND password = %s"

    # Cifrar contraseña
    cifrado = haslib.sha256()
    cifrado.update(self.password.encode('encode'))

    # Datos para consultar
    usuario = (self.email,cifrado.hezdigest())

    cursor.execute(sql,usuario)
    result = cursor.fetchone()

    return result