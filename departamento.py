#!/usr/bin/env python
# coding=<UTF-8>

class Departamento():
	def __init__(self, numeroDepto):
		self.numeroDepto = numeroDepto
		self.nombreInquilino = None
		self.telefonoInquilino = None
		self.procedenciaInquilino = None
		self.tipoIdentificacion = None
		self.numeroPersonas = None
		self.costo = None
		self.tipoReservacion = None			#Por dia, semana o mes
		self.depositoReservacion = None 	#Cuanto (solo si es por día o semana)
		self.depositoGarantia = None		#Cuanto (solo si es por mes)
		self.pagaLuz = None					#boolean
		self.fechaEntrada = None
		self.fechaSalida = None
		self.ocupado = None 				#boolean
		self.observaciones = None
		self.obtenerDatos()

	def modificarDatos(self):
		#Método para modificar los datos de un departamento en reservaciones, por ejemplo
		pass

	def obtenerDatos(self):
		#Método para leer los datos de la base y ponerlos en los atributos del objeto.
		pass
	