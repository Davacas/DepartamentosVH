#!/usr/bin/env python
#coding=<UTF-8>
#Archivo con la definición de todas las clases de GUIS
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from departamento import *
from database import *
import datetime

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
		self.eNombre = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		self.eNombre.grid(row = 1, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar teléfono.
		Label(self.ventanaRentar, text = "Teléfono: ", font = "Default 14").grid(row = 2, column = 0, sticky="e")
		self.eTelefono = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		self.eTelefono.grid(row = 2, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar procedencia.
		Label(self.ventanaRentar, text = "Procedencia: ", font = "Default 14").grid(row = 3, column = 0, sticky="e")
		self.eProcedencia = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		self.eProcedencia.grid(row = 3, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar tipo de identificación.
		Label(self.ventanaRentar, text = "Identificación: ", font = "Default 14").grid(row = 4, column = 0, sticky="e")
		self.eIdentificacion = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		self.eIdentificacion.grid(row = 4, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar cantidad de personas.
		Label(self.ventanaRentar, text = "Personas: ", font = "Default 14").grid(row = 5, column = 0, sticky="e")
		self.ePersonas = Spinbox(self.ventanaRentar, from_ = 1, to = 10, font = "Default 12", width = 5)
		self.ePersonas.grid(row = 5, column = 1, columnspan = 6, padx=(0,10), sticky="W")

		#Widgets para ingresar costo.
		Label(self.ventanaRentar, text = "Costo: ", font = "Default 14").grid(row = 6, column = 0, sticky="e")
		self.eCosto = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		self.eCosto.grid(row = 6, column = 1, columnspan = 5, padx=(0,10), sticky="EW")
		Label(self.ventanaRentar, text = "MXN", font = "Default 14").grid(row = 6, column = 6, sticky="w")

		#Widgets para ingresar tipo de reservación.
		Label(self.ventanaRentar, text = "Reservación por: ", font = "Default 14").grid(row = 7, column = 0, sticky="e")
		self.eTipoReservacion = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 10)
		self.eTipoReservacion["values"] = ["Día", "Semana", "Mes"]
		self.eTipoReservacion.grid(row = 7, column = 1, columnspan = 6, padx=(0,10), sticky="W")
		self.eTipoReservacion.current(0)

		#Widgets para ingresar cantidad del depósito.
		Label(self.ventanaRentar, text = "Depósito: ", font = "Default 14").grid(row = 8, column = 0, sticky="e")
		self.eDeposito = ttk.Entry(self.ventanaRentar, font = "Default 12", width = 8)
		self.eDeposito.grid(row = 8, column = 1, columnspan = 6, padx=(0,10), sticky="EW")

		#Widgets para ingresar si el inquilino paga su luz.
		Label(self.ventanaRentar, text = "¿Paga su luz? ", font = "Default 14").grid(row = 9, column = 0, sticky="e")
		self.ePagaLuz = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		self.ePagaLuz["values"] = ["No", "Sí"]
		self.ePagaLuz.grid(row = 9, column = 1, columnspan = 6, padx=(0,10), sticky="W")
		self.ePagaLuz.current(0)

		#Widgets para ingresar fecha de entrada del inquilino.
		Label(self.ventanaRentar, text = "Fecha de entrada: ", font = "Default 14").grid(row = 10, column = 0, sticky="e")
		Label(self.ventanaRentar, text = "Día: ", font = "Default 12").grid(row = 10, column = 1, sticky="e")
		self.eDiaEntrada = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		self.eDiaEntrada["values"] = list(range(1, 31))
		self.eDiaEntrada.grid(row = 10, column = 2, columnspan = 1, padx=(0,10), sticky="W")
		self.eDiaEntrada.current(17)
		Label(self.ventanaRentar, text = "Mes: ", font = "Default 12").grid(row = 10, column = 3, sticky="e")
		self.eMesEntrada = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		self.eMesEntrada["values"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
		self.eMesEntrada.grid(row = 10, column = 4, columnspan = 1, padx=(0,10), sticky="W")
		self.eMesEntrada.current(0)
		Label(self.ventanaRentar, text = "Año: ", font = "Default 12").grid(row = 10, column = 5, sticky="e")
		self.eAnioEntrada = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		self.eAnioEntrada["values"] = list(range(2000, 2100))
		self.eAnioEntrada.grid(row = 10, column = 6, columnspan = 1, padx=(0,10), sticky="W")
		self.eAnioEntrada.current(17)

		#Widgets para ingresar fecha de salida del inquilino.
		Label(self.ventanaRentar, text = "Fecha de Salida: ", font = "Default 14").grid(row = 11, column = 0, sticky="e")
		Label(self.ventanaRentar, text = "Día: ", font = "Default 12").grid(row = 11, column = 1, sticky="e")
		self.eDiaSalida = Spinbox(self.ventanaRentar, from_ = 1, to = 31, font = "Default 12", width = 5)
		self.eDiaSalida.grid(row = 11, column = 2, sticky="w", padx=(0,10))
		Label(self.ventanaRentar, text = "Mes: ", font = "Default 12").grid(row = 11, column = 3, sticky="e")
		self.eMesSalida = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		self.eMesSalida["values"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
		self.eMesSalida.grid(row = 11, column = 4, columnspan = 1, padx=(0,10), sticky="W")
		self.eMesSalida.current(0)
		Label(self.ventanaRentar, text = "Año: ", font = "Default 12").grid(row = 11, column = 5, sticky="e")
		self.eAnioSalida = ttk.Combobox(self.ventanaRentar, state="readonly", font = "Default 12", width = 5)
		self.eAnioSalida["values"] = list(range(2000, 2100))
		self.eAnioSalida.grid(row = 11, column = 6, columnspan = 1, padx=(0,10), sticky="W")
		self.eAnioSalida.current(17)

		#Widgets para ingresar observaciones.
		Label(self.ventanaRentar, text = "Observaciones: ", font = "Default 14").grid(row = 12, column = 0, sticky="e")
		self.eObservaciones = Text(self.ventanaRentar, height = 3, width = 8, font = "Default 12")
		self.eObservaciones.grid(row = 12, column = 1, columnspan = 6, padx=(0,10), sticky="EW")
		scroll = Scrollbar(self.ventanaRentar, command=self.eObservaciones.yview)
		scroll.grid(row = 12, column = 1, columnspan = 6, padx=(0,10), sticky="E")
		self.eObservaciones['yscrollcommand'] = scroll.set

		#Botones de control
		ttk.Button(self.ventanaRentar, text = 'Regresar', command = self.regresar).grid(row = 13, column = 2, sticky="e")
		ttk.Button(self.ventanaRentar, text = 'Rentar', command = self.guardarDatos).grid(row = 13, column = 4, padx=(0,10))
		centrarVentana(self.ventanaRentar)
		self.ventanaRentar.mainloop()

	#Método para regresar al menú principal
	def regresar(self):
		self.ventanaRentar.destroy()
		VistaPrincipal()

	def guardarDatos(self):
		# conexion = sqlite3.connect("departamentosVH.db")
		# cursor = conexion.cursor()
		fechaEntrada = self.eAnioEntrada.get() + "-" + str(self.eMesEntrada.current() + 1).zfill(2) + "-" + self.eDiaEntrada.get()
		fechaSalida = self.eAnioSalida.get() + "-" + str(self.eMesSalida.current() + 1).zfill(2) + "-" + self.eDiaSalida.get()
		print(fechaEntrada)
		print(fechaSalida)		

		try:
			Database().insertarRenta(
				self.numeroDepto,
				self.eNombre.get(), 
				int(self.eTelefono.get()), 
				self.eProcedencia.get(), 
				self.eIdentificacion.get(),
				int(self.ePersonas.get()),
				float(self.eCosto.get()),
				self.eTipoReservacion.get(), 
				float(self.eDeposito.get()),
				int(self.ePagaLuz.current()),
				fechaEntrada,
				fechaSalida,
				"Blablabla"
				)
			# cursor.execute("""INSERT INTO departamento%d 
			# 	VALUES(NULL, '%s', %d, '%s', '%s', %d, %f, '%s', %f, %d, '%s', '%s', %d, '%s')""" %(
			# 		self.numeroDepto,
			# 		self.eNombre.get(), 
			# 		int(self.eTelefono.get()), 
			# 		self.eProcedencia.get(), 
			# 		self.eIdentificacion.get(),
			# 		int(self.ePersonas.get()),
			# 		float(self.eCosto.get()),
			# 		self.eTipoReservacion.get(), 
			# 		float(self.eDeposito.get()),
			# 		int(self.ePagaLuz.current()),
			# 		fechaEntrada,
			# 		fechaSalida,
			# 		1, 
			# 		"Blablabla")
			# 	)
			# conexion.commit()
			# conexion.close()
		except Exception as ex:
			print("Ocurrió el siguiente error al guardar en la base de datos:")
			print(ex)
			#conexion.rollback()

		self.ventanaRentar.destroy()
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
		#Se inicializa el widget para desplegar historial
		self.wHistorial = Text(self.ventanaHistorial, height = 20, width = 8, font = "Default 12")
		self.wHistorial.grid(row = 2, column = 0, columnspan = 8, padx=(0,10), sticky="EW")
		scroll = Scrollbar(self.ventanaHistorial, command=self.wHistorial.yview)
		scroll.grid(row = 2, column = 1, columnspan = 8, padx=(0,10), sticky="NSE")
		self.wHistorial['yscrollcommand'] = scroll.set
		#Se leen los datos de la base de datos
		conexion = sqlite3.connect("departamentosVH.db")
		cursor = conexion.cursor()
		try:
			cursor.execute("SELECT * FROM Renta_Depto%d ORDER BY numeroRenta DESC" %(self.numeroDepto)) 
			historial = str(cursor.fetchall())
		except Exception as ex:
			print("Ocurrió el siguiente error al leer de la base de dat:")
			print(ex)
			conexion.rollback()
		else: #Si se pudo leer, se pone en el widget de texto.
			#HAY QUE DARLE MAS FORMATO A ESTA IMPRESION
			self.wHistorial.insert(INSERT, historial)
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