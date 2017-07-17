#!/usr/bin/env python
#coding=<UTF-8>

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from departamento import *
from database import *

#Clase que define la ventana principal de la aplicacion
class VistaPrincipal():
	#Constructor. Define parámetros generales de la ventana, adquiere la información de la base
	#y despliega la ventana con todo lo definido.
	def __init__(self):
		self.ventanaPrincipal = Tk() #Inicializando Tk
		self.ventanaPrincipal.title("Departamentos Vista Hermosa")
		self.ventanaPrincipal.resizable(width=False,height=False)
		Label(self.ventanaPrincipal, text = "Depto.:\t", font = "Default 14 bold").grid(row = 0, column = 0)
		Label(self.ventanaPrincipal, text = "Estado actual\t", font = "Default 14 bold").grid(row = 0, column = 1)
		Label(self.ventanaPrincipal, text = "Opciones", font = "Default 14 bold").grid(row = 0, column = 2)
		self.actualizarInformacion()
		self.ventanaPrincipal.mainloop()

	#Método que toma los valores de los departamentos desde la base de datos y los coloca en la GUI
	def actualizarInformacion(self):
		for i in range (0, 12):
			nuevoDepartamento = Departamento(i+1)
			self.desplegarDatos(nuevoDepartamento)

	#Método que enlista y muestra los datos adquiridos de la base de datos
	def desplegarDatos(self, departamento):
		Label(self.ventanaPrincipal, text = departamento.numeroDepto, font = "Default 14").grid(row = departamento.numeroDepto, column = 0)
		Label(self.ventanaPrincipal, text = "Se renta el: DD/MM/YY", font = "Default 14").grid(row = departamento.numeroDepto, column = 1)
		ttk.Button(self.ventanaPrincipal, text = 'Historial', command = lambda: self.historial(departamento.numeroDepto)).grid(row = departamento.numeroDepto, column = 2)
		#if departamento.ocupado:
			#Button(self.raiz, text='Terminar contrato')
		#else:
		ttk.Button(self.ventanaPrincipal, text = 'Rentar', command = lambda: self.rentar(departamento.numeroDepto)).grid(row = departamento.numeroDepto, column = 3)
	
	#Método para lanzar la ventana de rentar un departamento
	def rentar(self, numeroDepto):
		self.ventanaPrincipal.destroy()
		VistaRentar(numeroDepto) 

	#Método para lanzar la ventana con el historial de un departamento
	def historial(self, numeroDepto):
		self.ventanaPrincipal.destroy()
		VistaHistorial(numeroDepto) 



#Clase que define la ventana para rentar un departamento
class VistaRentar():
	#Constructor. Se definen todos los elementos de la ventana
	def __init__(self, numeroDepto):
		self.numeroDepto = numeroDepto
		self.ventanaRentar = Tk() #Inicializando Tk
		self.ventanaRentar.title("Departamentos Vista Hermosa")
		self.ventanaRentar.resizable(width=False,height=False)
		Label(self.ventanaRentar, text = "Rentando departamento " + str(self.numeroDepto), font = "Default 16 bold").grid(row = 0, column = 1)
		Label(self.ventanaRentar, text = "Nombre: ", font = "Default 14").grid(row = 1, column = 0)
		NombreCT = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 40).grid(row = 1, column = 1)
		Label(self.ventanaRentar, text = "Teléfono: ", font = "Default 14").grid(row = 2, column = 0)
		TelefonoCT = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 40).grid(row = 2, column = 1)
		Label(self.ventanaRentar, text = "Procedencia: ", font = "Default 14").grid(row = 3, column = 0)
		TelefonoCT = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 40).grid(row = 3, column = 1)
		ttk.Button(self.ventanaRentar, text = 'Regresar', command = self.regresar).grid(row = 12, column = 0)
		ttk.Button(self.ventanaRentar, text = 'Rentar', command = self.guardarDatos).grid(row = 12, column = 1)
		#AQUÍ VAN UN CHINGO DE CUADROS DE TEXTO Y MENÚS DESPLEGABLES PARA ALMACENAR EN LA BASE.
		self.ventanaRentar.mainloop()

	#Método para regresar al menú principal
	def regresar(self):
		self.ventanaRentar.destroy()
		VistaPrincipal()

	#Método que adquiere todos los valores de los cuadros de texto y los almacena en la base de datos.
	def guardarDatos(self):
		self.ventanaRentar.destroy()
		#Poner los leido de los cuadros de texto (NombreCT.get())
		VistaPrincipal()


#Clase que define la ventana para ver el historial un departamento
class VistaHistorial():
	#Constructor. Define parámetros generales de la ventana, adquiere la información de la base
	#y despliega la ventana con todo lo definido.
	def __init__(self, numeroDepto):
		self.numeroDepto = numeroDepto
		self.ventanaHistorial = Tk() #Inicializando Tk
		self.ventanaHistorial.title("Departamentos Vista Hermosa")
		self.ventanaHistorial.resizable(width=False,height=False)
		ttk.Button(self.ventanaHistorial, text = 'Regresar', command = self.regresar).grid(row = 0, column = 0)
		Label(self.ventanaHistorial, text = "Historial del departamento " + str(self.numeroDepto), font = "Default 14 bold").grid(row = 0, column = 2)
		Label(self.ventanaHistorial, text = "Nombre", font = "Default 12 bold").grid(row = 1, column = 0)
		Label(self.ventanaHistorial, text = "Teléfono", font = "Default 12 bold").grid(row = 1, column = 1)
		Label(self.ventanaHistorial, text = "Procedencia", font = "Default 12 bold").grid(row = 1, column = 2)
		Label(self.ventanaHistorial, text = "ID", font = "Default 12 bold").grid(row = 1, column = 3)
		Label(self.ventanaHistorial, text = "Personas", font = "Default 12 bold").grid(row = 1, column = 4)
		Label(self.ventanaHistorial, text = "Costo", font = "Default 12 bold").grid(row = 1, column = 5)
		Label(self.ventanaHistorial, text = "Tipo Res.", font = "Default 12 bold").grid(row = 1, column = 6)
		Label(self.ventanaHistorial, text = "Depósito", font = "Default 12 bold").grid(row = 1, column = 7)
		self.ventanaHistorial.mainloop()
	
	#Método para lanzar la ventana principal
	def regresar(self):
		self.ventanaHistorial.destroy()
		VistaPrincipal()
		

#Se inicializa la base y se lanza la interfaz principal
def main():
	inicializarBase()
	VistaPrincipal()

if __name__ == "__main__":
    main()

		