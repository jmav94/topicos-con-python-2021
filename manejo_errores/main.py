# Captura de excepciones y manejo de errores en codigo.
"""
try:
  nombre = input("Cual es tu nombre? ")
  if len(nombre) > 1:
    nombre_usuario = f"El nombre es: {nombre}"

  print(nombre_usuario)
except:
  print("Ha ocurriedo un error, introduce bien el nombre")
else:
  print("El programa funciona correctamente")
finally:
  print("fin de la ejecucion.")
  """

# Exepciones multiples

"""
try:
  numero = int(input("Numero para elevarlo al cuadrado: "))
  print("El cuadrado del numero es " + numero*numero)

except TypeError:
  print("Debes convertir tus enteros a cadenas en el codigo")
except ValueError:
  print("Introduce un numero correcto")
except Exception as e:
  print(type(e))
  print("Ha ocurrido un errr", type(e).__name__)
"""
# Excepciones perzonalizadas
try:
  nombre = input("Introduce tu nombre: ")
  edad = int(input("introduce tu edad: "))

  if edad < 5 or edad > 110:
    raise ValueError("La edad introducida no es esta dentro del rango permitido.")
  elif  len(nombre) <= 1 :
    raise ValueError("El nombre no es correcto.")
  else:
    print(f"Bienvenido {nombre} !!")

except ValueError:
  print("Introduce los datos correctamente.")
  raise
except Exception as e:
  print("Existe un error: ", e)
  raise