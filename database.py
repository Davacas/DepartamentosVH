#!/usr/bin/env python
# coding=<UTF-8>
import sqlite3

def inicializarBase():
	conexion = sqlite3.connect('departamentosVH.db')
	cursor = conexion.cursor()
	try:
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento1 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento3 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento5 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento6 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento7 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento8 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento9 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento10 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento11 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento12 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	    cursor.execute("""CREATE TABLE IF NOT EXISTS departamento13 (
	    			numeroDepto 		INTEGER PRIMARY KEY, 
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
	                ocupado				INTEGER,	
	                observaciones		TEXT
	                )""")
	except Exception as ex:
	    print("Ocurrio el siguiente error al crear la base:")
	    print(ex)
	conexion.close()