from tkinter import *

import os.path

class Programa:
  def __init__(self):
    self.titile = "Esto es una aplicacion de prueba"
    self.icon = "./imagenes/transferr.png"
    self.icon_alt = ""
    self.size = "770x470"
    self.reseizable = False

  def cargar(self):
    venta = Tk()
    self.ventana = ventana

    ventana.tittle(self.titile)

    ruta_icono = os.path.abspath(self.icon)

    if not os.path.isfile(ruta_icono):
      ruta_icono = os.path.abspath(self.icon_alt)

    ventana.iconmap(ruta_icono)


  programa = Programa()
  programa.cargar()
