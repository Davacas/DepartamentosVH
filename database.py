import sqlite3

def inicializarBase():
	conexion = sqlite3.connect('departamentosVH.db')
	cursor = conexion.cursor()
	try:
	    cursor.execute('''CREATE TABLE departamento (
	    			numeroDepto 		integer primary key, 
	                nombreInquilino 	text, 
	                telefonoInquilino 	integer, 
	                procedenciaInquilino text,
	                tipoIdentificacion 	text,
	                numeroPersonas 		integer,
	                costo 				real,
	                tipoReservacion 	text,
	                depositoReservacion	real,
	                depositoGarantia	real,
	                pagaLuz				integer, 	#Convertir a booleano
	                fechaEntrada		text,		#Convertir a fecha
	                fechaSalida			text,		#Convertir a fecha
	                ocupado				integer,	#Convertir a booleano
	                observaciones		text
	                )''')
	except:
	    print("No fue necesario recrear la base.")
	conexion.close()