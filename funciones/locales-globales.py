# Variable Global
vglobal = "Esta es una variable global."

print(vglobal)

def holaMundo():
  # Cambiando valor de variable global dentro de la funcion
  vglobal = "Este es un nuevo valor"
  print("Variable global dentro de una funcion")
  print(vglobal)
  # Variable Local
  year = 2021
  print(year)

  global website

  website = "facebook.com"
  print(f"Sitio web: {website}")

holaMundo()

print(f"Variable con palabra reservada global: {website}")
