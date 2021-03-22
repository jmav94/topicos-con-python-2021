#nombre = 3
nombre = "Juan Perez"

print(type(nombre))

comprobacion = isinstance(nombre,str)
if comprobacion:
  print(f"{nombre} es una variable de tipo string")
else:
  print(f"{nombre} no es una cadena")

if not isinstance(nombre,int):
  print(f"La variable nombre no es un entero")

# Quitar espacios en blanco
frase = "    Hola, bienvenidos    "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2021
print(year)

del year
#year= "2020"
#print(year)

# Comprobar longitud de una variable
texto = " Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.      "
#texto= ""
#print(len(texto))

if len(texto) <= 0:
  print("La variable esta vacia")
else:
  print(f"La variable tiene una longitud de {len(texto)}")

# Encontrar un valor enviado como parametro.
print(texto.find(" Ipsum"))

# Remplazar cadenas en una variable

otraFrase = frase.replace("bienvenidos", "hasta luego")
#print(frase)
print(otraFrase)

# Mayusculas y minusculas
print(nombre)
print(nombre.upper())