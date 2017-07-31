#!/usr/bin/env python
# coding=<UTF-8>

import sqlite3
from departamento import *

class Database:

	def __init__(self):
		"Something something"
		self.database = 'departamentosVH.db'

	def inicializarBase(self):
		conexion = sqlite3.connect(self.database)
		cursor = conexion.cursor()
		
		try:
		    for numDepto in range(1, 13):
			    if ( not (numDepto == 2 or numDepto == 4) ):
			    	nombreTabla = "Renta_Depto" + str(numDepto)
			    	command = """CREATE TABLE IF NOT EXISTS {} (
			    		numeroRenta 		INTEGER PRIMARY KEY, 
			            nombreInquilino 	TEXT, 
			            telefonoInquilino 	INTEGER, 
			            procedenciaInquilino TEXT,
			            tipoIdentificacion 	TEXT,
			            numeroPersonas 		INTEGER,
			            costo 				REAL,
			            tipoReservacion 	TEXT,
			            deposito			REAL,
			            pagaLuz				INTEGER, 	
			            fechaEntrada		TEXT,		
			            fechaSalida			TEXT,	
			            observaciones		TEXT
			            )""".format( nombreTabla )
			    	cursor.execute( command )

		except Exception as ex:
		    print( "Ocurrio el siguiente error al crear la base: {}".format( ex ) )

		conexion.close()

	def insertarRenta(self, 
					numDepto,
					nombreInquilino,
					telefonoInquilino, 
					procedenciaInquilino,
					tipoIdentificacion,
					numeroPersonas,
					costo,
					tipoReservacion,
					deposito,
					pagaLuz, 	
					fechaEntrada,		
					fechaSalida,	
					observaciones ):
		"Insertar una renta en un depto dado"

		conexion = sqlite3.connect(self.database)
		cursor = conexion.cursor()
		
		try:
			nombreTabla = "Renta_Depto" + str(numDepto)
			command = """INSERT INTO {}
				VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, date(?), date(?), ?)""".format(
					nombreTabla )
			cursor.execute( command, 
					( 
					nombreInquilino,
					telefonoInquilino, 
					procedenciaInquilino,
					tipoIdentificacion,
					numeroPersonas,
					costo,
					tipoReservacion,
					deposito,
					pagaLuz, 	
					fechaEntrada,		
					fechaSalida,	
					observaciones 
						)
			    )
			conexion.commit()

		except Exception as ex:
			print("Error al insertar renta en BdD: {}".format(ex))

		conexion.close()

	def obtenerRentaActual(self, numDepto):
		"Obtener el estado actual de un departamento dado el número de éste"

		# Valor de retorno
		actual = None

		conexion = sqlite3.connect(self.database)
		cursor = conexion.cursor()
		
		try:
			command = """SELECT * FROM Renta_Depto{} WHERE 
						 date('now') >= date(fechaEntrada) AND 
						 date('now') <= date(fechaSalida)""".format(numDepto)

			cursor.execute( command )
			actual = cursor.fetchone()

		except Exception as ex:
			print(ex)

		conexion.close()

		return actual

	def obtenerHistorial(self, numDepto):
		"Obtener el historial de rentas"

		# Valor de retorno
		historial = None

		conexion = sqlite3.connect(self.database)
		cursor = conexion.cursor()

		try:
			nombreTabla = "Renta_Depto" + str(numDepto)
			command = """SELECT * FROM {}""".format( nombreTabla )
			cursor.execute( command )
			historial = cursor.fetchall()

		except Exception as ex:
			print(ex)

		return historial