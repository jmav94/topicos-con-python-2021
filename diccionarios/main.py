# Diccionario
persona = {
  "Nombre":"Juan",
  "Apellidos":"Ahumada Vazquez",
  "Correo":"juan.ahumada@gmail.com"
  }

# Imprimir diccionario
#print(persona)

print(persona["Apellidos"])

# Listas con diccionarios

contactos = [
  {
    'nombre':'Daniel',
    'correo':'daniel@gmail.com'
  },
  {
    'nombre':'Luis',
    'correo':'luis@gmail.com'
  },
  {
    'nombre':'fidel',
    'correo':'fidel@gmai.com'
  }
]

contactos[0]['nombre'] ='alejandro'
print(contactos[0]['nombre'])

for contacto in contactos:
  print(f"Nombre del contacto: {contacto['nombre']}")
  print(f"Email de contacto: {contacto['correo']}")
  print(f'----------------------------------------')