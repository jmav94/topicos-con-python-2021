def holamundo(nombre):
  return f"Hola {nombre}, como estas?"

def calculadora(numero1,numero2, basicas = False):
  suma = numero1 + numero2
  resta = numero1 - numero2
  multiplicacion = numero1 * numero2
  division = numero1 / numero2

  cadena = ""

  if basicas != False:
    #cadena += f"Suma: {str(suma)} \nResta: {str{resta}} \n"
    cadena += "Suma: "+ str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
  else:
    cadena += "Multiplicacion: " + str(multiplicacion)
    cadena += "\n"
    cadena += "Division: " + str(division)
    cadena += "\n"

  return cadena
