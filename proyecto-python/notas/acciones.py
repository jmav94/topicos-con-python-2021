import notas.nota as modelo

class Acciones:
  def crear(self,usuario):
    print(f"ok {usuario[1]}, Captura los datos de tu nueva nota.")

    titulo = input("Introduce el titulo de tu nota: ")
    descripcion = input("Captura el contenido de tu nota: ")

    nota= modelo.Nota(usuario[0], titulo, descripcion)
    guardar = nota.guardar()

    if guardar[0] >=1:
      print(f"Bien, tu nota {nota.titulo} se ha guardado correctamente. ")

    else:
      print(f"Tu nota no se pudo guardar, intenta nuevamente.")

  def mostrar(self, usuario):
    print(f"Aqui estan tus notas {usuario[1]}:")

    nota = modelo.Nota(usuario[0])
    notas = nota.listar()

    for nota in notas:
      print("\n************************")
      print(nota[2])
      print(nota[3])
      print("************************")

  def borrar(self,usuario):
    print(f"{usuario[1]} estas apunto de eliminar una nota.")
    titulo = input("Introduce el titulo de la nota que deseas borrar:")

    nota = modelo.Nota(usuario[0],titulo)
    eliminar = nota.eliminar()

    if eliminar[0] >= 1:
      print(f"Listo {usuario[1]} tu nota se ha eliminado correctamente.")

    else: print("Hubieron problemas para borrar tu nota, intenta de nuevo.")