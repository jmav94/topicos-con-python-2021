class Auto:
  # Constructor
  def __init__(self, color, marca, modelo, velocidad, cilindros):
    self.color = color
    self.marca = marca
    self.modelo = modelo
    self.velocidad = velocidad
    self.cilindros = cilindros
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


  def __frenar(self):
    self.velocidad -= 20


  def getVelocidad(self):
    return self.velocidad

  def getInfo(self):
    info = "-------- Detalles del Auto ---------"
    info += f"\n Color: {self.getColor()}"
    info += f"\n Marca: {self.getMarca()}"
    info += f"\n Modelo: {self.getModelo()}"
    info += f"\n Velocidad: {self.getVelocidad()}"
    return info

  def __str__(self):
    return """\
      Color: {}
      Marca: {}
      """.format(self.color,self.marca)