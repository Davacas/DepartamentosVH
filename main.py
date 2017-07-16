#!/usr/bin/env python

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from departamento import *
from database import *

#Clase que define la ventana principal de la aplicacion
class VistaPrincipal():
	def __init__(self):
		self.ventanaPrincipal = Tk() #Inicializando Tk
		self.ventanaPrincipal.title("Departamentos Vista Hermosa")
		Label(self.ventanaPrincipal, text = "No.\t", font = "Helvetica 14 bold").grid(row = 0, column = 0)
		Label(self.ventanaPrincipal, text = "Estado actual\t", font = "Helvetica 14 bold").grid(row = 0, column = 1)
		Label(self.ventanaPrincipal, text = "Opciones", font = "Helvetica 14 bold").grid(row = 0, column = 2)

	def desplegarDatos(self, departamento):
		Label(self.ventanaPrincipal, text = departamento.numeroDepto, font = "Helvetica 14").grid(row = departamento.numeroDepto, column = 0)
		Label(self.ventanaPrincipal, text = "asdf2.\t", font = "Helvetica 14").grid(row = departamento.numeroDepto, column = 1)
		Label(self.ventanaPrincipal, text = "asdf3", font = "Helvetica 14").grid(row = departamento.numeroDepto, column = 2)

	def mostrarGUI(self):
		self.ventanaPrincipal.mainloop()


def main():
	inicializarBase()
	departamento = []
	vistaPrincipal = VistaPrincipal();

	for i in range (0, 12):
		nuevoDepartamento = Departamento(i+1)
		vistaPrincipal.desplegarDatos(nuevoDepartamento)
		departamento.append(nuevoDepartamento)

	vistaPrincipal.mostrarGUI();

if __name__ == "__main__":
    main()

		