class Persona:
  """
  nombre
  apellidos
  edad
  sexo
  """

  def setNombre(self, nombre):
    self.nombre = nombre

  def getNombre(self):
    return self.nombre

  def getApellidos(self):
    return self.apellidos

  def getEdad(self):
    return self.edad

  def getSexo(self):
    return self.sexo



  def setApellidos(self, apellidos):
    self.apellidos = apellidos

  def setEdad(self,edad):
    self.edad = edad

  def setSexo(self,sexo):
    self.sexo = sexo

class Estudiante(Persona):
  """
  carrera
  numControl
  """
  def __init__(self):
    self.__carrera = "ISC"
    self.__numControl = 21100101

  def getCarrera(self):
    return self.__carrera

  def estudiar(self,materias):
    self.materias = materias
    return self.materias

class Empleado(Persona):
  def __init__(self):
    super().__init__()
    self.departamento = 'Sistemas'
    self.sueldo = 15000

  def aumento(self,aumento):
    self.sueldo += aumento
    return self.sueldo

class Gerente(Empleado):
  def __init__(self):
    super().__init__()
    self.jefeDirecto = 'CEO'
    self.sueldo = 20000

  def moverGerente(self,jefeDirecto):
    self.jefeDirecto = jefeDirecto
    return self.jefeDirecto

