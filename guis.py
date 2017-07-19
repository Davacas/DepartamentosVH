#!/usr/bin/env python
#coding=<UTF-8>
#Archivo con la definición de todas las clases de GUIS
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
		Label(self.ventanaPrincipal, text = "Depto.:\t", font = "Default 14 bold").grid(row = 0, column = 0, sticky="nesw")
		Label(self.ventanaPrincipal, text = "Estado actual\t", font = "Default 14 bold").grid(row = 0, column = 1, sticky="nesw")
		Label(self.ventanaPrincipal, text = "Opciones", font = "Default 14 bold").grid(row = 0, column = 2, sticky="nesw")
		self.actualizarInformacion()
		centrarVentana(self.ventanaPrincipal)
		self.ventanaPrincipal.mainloop()

	#Método que toma los valores de los departamentos desde la base de datos y los coloca en la GUI
	def actualizarInformacion(self):
		for i in range (1, 14):
			if (i == 2 or i == 4):
				continue
			else:
				nuevoDepartamento = Departamento(i)
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
		titulo = Label(self.ventanaRentar, text = "Rentando departamento " + str(self.numeroDepto), font = "Default 16 bold")
		titulo.grid(row = 0, column = 1, columnspan = 6, padx=(0,10), sticky="W")

		#Widgets para ingresar nombre.
		Label(self.ventanaRentar, text = "Nombre: ", font = "Default 14", anchor="nw").grid(row = 1, column = 0, sticky="e")
		eNombre = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		eNombre.grid(row = 1, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar teléfono.
		Label(self.ventanaRentar, text = "Teléfono: ", font = "Default 14").grid(row = 2, column = 0, sticky="e")
		eTelefono = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		eTelefono.grid(row = 2, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar procedencia.
		Label(self.ventanaRentar, text = "Procedencia: ", font = "Default 14").grid(row = 3, column = 0, sticky="e")
		eProcedencia = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		eProcedencia.grid(row = 3, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar tipo de identificación.
		Label(self.ventanaRentar, text = "Identificación: ", font = "Default 14").grid(row = 4, column = 0, sticky="e")
		eIdentificacion = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		eIdentificacion.grid(row = 4, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar cantidad de personas.
		Label(self.ventanaRentar, text = "Personas: ", font = "Default 14").grid(row = 5, column = 0, sticky="e")
		ePersonas = Spinbox(self.ventanaRentar, from_ = 1, to = 10, font = "Default 12", width = 5)
		ePersonas.grid(row = 5, column = 1, columnspan = 6, padx=(0,10), sticky="W")

		#Widgets para ingresar costo.
		Label(self.ventanaRentar, text = "Costo: ", font = "Default 14").grid(row = 6, column = 0, sticky="e")
		eCosto = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		eCosto.grid(row = 6, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar tipo de reservación.
		Label(self.ventanaRentar, text = "Reservación por: ", font = "Default 14").grid(row = 7, column = 0, sticky="e")
		eTipoReservacion = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 10)
		eTipoReservacion["values"] = ["Día", "Semana", "Mes"]
		eTipoReservacion.grid(row = 7, column = 1, columnspan = 6, padx=(0,10), sticky="W")
		eTipoReservacion.current(0)

		#Widgets para ingresar cantidad del depósito.
		Label(self.ventanaRentar, text = "Depósito: ", font = "Default 14").grid(row = 8, column = 0, sticky="e")
		eDeposito = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		eDeposito.grid(row = 8, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar si el inquilino paga su luz.
		Label(self.ventanaRentar, text = "¿Paga su luz? ", font = "Default 14").grid(row = 9, column = 0, sticky="e")
		ePagaLuz = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		ePagaLuz["values"] = ["No", "Sí"]
		ePagaLuz.grid(row = 9, column = 1, columnspan = 6, padx=(0,10), sticky="W")
		ePagaLuz.current(0)

		#Widgets para ingresar fecha de entrada del inquilino.
		Label(self.ventanaRentar, text = "Fecha de entrada: ", font = "Default 14").grid(row = 10, column = 0, sticky="e")
		Label(self.ventanaRentar, text = "Día: ", font = "Default 12").grid(row = 10, column = 1, sticky="e")
		eDiaEntrada = Spinbox(self.ventanaRentar, from_ = 1, to = 31, font = "Default 12", width = 5)
		eDiaEntrada.grid(row = 10, column = 2, sticky="w", padx=(0,10))
		Label(self.ventanaRentar, text = "Mes: ", font = "Default 12").grid(row = 10, column = 3, sticky="e")
		eMesEntrada = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		eMesEntrada["values"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
		eMesEntrada.grid(row = 10, column = 4, columnspan = 1, padx=(0,10), sticky="W")
		eMesEntrada.current(0)
		Label(self.ventanaRentar, text = "Año: ", font = "Default 12").grid(row = 10, column = 5, sticky="e")
		eAnioEntrada = Spinbox(self.ventanaRentar, from_ = 2017, to = 2100, font = "Default 12", width = 5)
		eAnioEntrada.grid(row = 10, column = 6, sticky="w", padx=(0,10))

		#Widgets para ingresar fecha de salida del inquilino.
		Label(self.ventanaRentar, text = "Fecha de Salida: ", font = "Default 14").grid(row = 11, column = 0, sticky="e")
		Label(self.ventanaRentar, text = "Día: ", font = "Default 12").grid(row = 11, column = 1, sticky="e")
		eDiaEntrada = Spinbox(self.ventanaRentar, from_ = 1, to = 31, font = "Default 12", width = 5)
		eDiaEntrada.grid(row = 11, column = 2, sticky="w", padx=(0,10))
		Label(self.ventanaRentar, text = "Mes: ", font = "Default 12").grid(row = 11, column = 3, sticky="e")
		eMesEntrada = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		eMesEntrada["values"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
		eMesEntrada.grid(row = 11, column = 4, columnspan = 1, padx=(0,10), sticky="W")
		eMesEntrada.current(0)
		Label(self.ventanaRentar, text = "Año: ", font = "Default 12").grid(row = 11, column = 5, sticky="e")
		eAnioEntrada = Spinbox(self.ventanaRentar, from_ = 2017, to = 2100, font = "Default 12", width = 5)
		eAnioEntrada.grid(row = 11, column = 6, sticky="w", padx=(0,10))

		#Widgets para ingresar observaciones.
		Label(self.ventanaRentar, text = "Observaciones: ", font = "Default 14").grid(row = 12, column = 0, sticky="e")
		eObservaciones = Text(self.ventanaRentar, height = 3, width = 8, font = "Default 12")
		eObservaciones.grid(row = 12, column = 1, columnspan = 6, padx=(0,10), sticky="EW")
		scroll = Scrollbar(self.ventanaRentar, command=eObservaciones.yview)
		scroll.grid(row = 12, column = 1, columnspan = 6, padx=(0,10), sticky="E")
		eObservaciones['yscrollcommand'] = scroll.set

		#Botones de control
		ttk.Button(self.ventanaRentar, text = 'Regresar', command = self.regresar).grid(row = 13, column = 2, sticky="e")
		ttk.Button(self.ventanaRentar, text = 'Rentar', command = self.guardarDatos).grid(row = 13, column = 4, padx=(0,10))
		centrarVentana(self.ventanaRentar)
		self.ventanaRentar.mainloop()

	#Método para regresar al menú principal
	def regresar(self):
		self.ventanaRentar.destroy()
		VistaPrincipal()

	#Método que adquiere todos los valores de los widgets y los almacena en la base de datos.
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
		centrarVentana(self.ventanaHistorial)
		self.ventanaHistorial.mainloop()
	
	#Método para lanzar la ventana principal
	def regresar(self):
		self.ventanaHistorial.destroy()
		VistaPrincipal()

#Función para centrar ventanas tomada de https://bbs.archlinux.org/viewtopic.php?id=149559
def centrarVentana(ventana):
	ventana.withdraw()
	ventana.update_idletasks()
	x = (ventana.winfo_screenwidth() - ventana.winfo_reqwidth()) / 2	
	y = (ventana.winfo_screenheight() - ventana.winfo_reqheight()) / 2
	ventana.geometry("+%d+%d" % (x, y))

	ventana.deiconify()