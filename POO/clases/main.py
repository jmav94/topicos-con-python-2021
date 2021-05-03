# Programacion orientada a objetos (POO / OOP)

# Realizar la definicion de una clase (molde para crear objetos de ese tipo)
# (auto) con sus respectivas caracteristicas

class Auto:
  # Atrubutos
  color = "Gris"
  __marca = "Audi"
  __modelo = "A7"
  velocidad = 120
  cilindros = 6
  capacidad = 4

  # Metodos
  def setColor(self, color):
    self.color = color

  def getColor(self):
    return self.color

  def getMarca(self):
    return self.__marca

  def setModelo(self, modelo):
    self.modelo = modelo

  def getModelo(self):
    return self.modelo

  def acelerar(self):
    self.velocidad += 20

  def frenar(self):
    self.velocidad -= 20

  def getVelocidad(self):
    return self.velocidad
# finde la definicion de la clase

miAuto = Auto()

print("Auto 1: ")

miAuto.setColor("Rojo")
miAuto.setModelo("A1")

print(miAuto.getMarca(), miAuto.getModelo(), miAuto.getColor())
print("Valocidad: ",miAuto.getVelocidad())

miAuto.acelerar()
miAuto.acelerar()
miAuto.acelerar()
miAuto.frenar()

print("Velocidad Actual: ", miAuto.getVelocidad())

print("------------------------")

miAuto2 = Auto()
miAuto2.setColor("Amarillo")
miAuto2.setModelo("B34")

print("Auto 2")
print(miAuto2.getMarca(),miAuto2.getModelo(),miAuto2.getColor())

print(type(miAuto2))

