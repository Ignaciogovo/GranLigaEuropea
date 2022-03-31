# Abre conexion con la base de datos
import sys
sys.path.append('ProyectoLiga')
import conexionpython as cp
def insertarclub(nombre,pais):
	db = cp.bbddliga()
	##################################################
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#INSERT:
	sql = "INSERT INTO club(nombre, pais) VALUES (%s,%s)"
	valores = (nombre,pais)
	cursor.execute(sql,valores)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro insertado")
	# desconecta del servidor
	db.close()

def insertarjugador(datos_jugadores):
	# print(datos_jugadores)
	db = cp.bbddliga()
	##################################################

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#INSERT:
	sql = "INSERT INTO jugadores(nombre,id_club,posicion,peso,altura,nacionalidad,valor,FechaNacimiento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	cursor.execute(sql,datos_jugadores)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro insertado")
	# desconecta del servidor
	db.close()


def SelectClub(nombre):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select id from club where nombre = %s"
	cursor.execute(sql,nombre)
	dato = cursor.fetchone()
	id_club = dato[0]
	return(id_club)