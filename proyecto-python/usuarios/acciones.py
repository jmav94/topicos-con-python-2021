import usuarios.usuario as modelo
#import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            print("\nNo te has registrado correctamente!!!")


    def login(self):
        print("\nVale!! Identificate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has identificado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (create)
        - Mostrar tus notas (select)
        - Eliminar nota (delete)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "create":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "select":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "delete":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto!!!")
            exit()