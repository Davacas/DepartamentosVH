#!/usr/bin/env python
# coding=<UTF-8>

import sqlite3
from departamento import *

class Database:
	database = None

	def __init__(self):
		"Something something"
		self.database = 'departamentosVH.db'

	def inicializarBase(self):
		conexion = sqlite3.connect(database)
		cursor = conexion.cursor()
		
		try:
		    for numDepto in range(1, 13):
			    if ( not (numDepto == 2 or numDepto == 4) ):
			    	command = """CREATE TABLE IF NOT EXISTS departamento%d (
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
			            )""" %(numDepto)
			    	cursor.execute( command )

		except Exception as ex:
		    print( "Ocurrio el siguiente error al crear la base: {}".format( ex ) )

		conexion.close()

	def insertarRenta(self, numDepto, renta):
		"Insertar una renta en un depto dado"
		
		conexion = sqlite3.connect(database)
		cursor = conexion.cursor()

		command = """INSERT INTO departamento%d 
				VALUES (NULL, '%s', %d, '%s', '%s', %d, %f, '%s', %f, %d, '%s', '%s', '%s')""" %(
					numDepto, 
					)

		conexion.close()

	def obtenerRenta(self, numDepto):
		"Obtener el estado actual de un departamento dado el número de éste"
