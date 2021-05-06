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