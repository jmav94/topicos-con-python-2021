import usuarios.usuario as modelo
# import notas.acciones

class Acciones:
  def registro(self):
    print("\nBienvenido, vamos a registrarte en el sistema.")

    nombre = input("Captura tu nombre:")
    apellidos = input("Captura tus apellidos:")
    email = input("Captura tu email:")
    password = input("Captura tu constaseña:")

    usuario = modelo.Usuario(nombre,apellidos,email,password)
    registro = usuario.registrar()

    if registro[0] >= 1:
      print(f"\n Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
    else:
      print("Tu registro no fue existoso.")

  def login(self):
    print("\nIdentificate con tus crdenciales.")

    try:
      email = input("Introduce tu email: ")
      password = input("Introduce tu contraseña: ")

      usuario = modelo.Ususario('','',email,password)
      login = usuario.identificar()

      if email == login[3]:
        print(f"Bienvenido {login[1]} te has identificado correctamente {login[5]}.")
        self.proximasAcciones(login)

    except Exception as e:
      print(type(e))
      print(type(e).__name__)
      print(f"Identificacion fallida, intentalo mas tarde.")

  def proximasAcciones(self,usuario):
    print("""
      Acciones disponibles:
      - Crear notas (CREATE)
      - Mostrar notas (SELECT)
      - Eliminar nota(s) (DELETE)
      - Salir (SALIR)
      """)

    accion = input("¿Que accion deseas realizar?")
    #realizar = notas.acciones.Acciones()

    if accion == "CREATE":
      #realizar.crear(usuario)
      self.proximasAcciones(usuario)

    elif accion == "SELECT":
      #realizar.mostrar(usuario)
      self.proximasAciones(usuario)

    elif accion == "DELETE":
      #realizar.borrar(usuario)
      self.proximasAcciones(usuario)

    elif accion == "SALIR":
      print(f"hasta pronto {usuario[1]}")
      exit()
