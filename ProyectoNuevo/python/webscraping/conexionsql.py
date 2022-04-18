# Abre conexion con la base de datos
import sys
from turtle import update

from colorama import Cursor
sys.path.append('ProyectoLiga')
import conexionpython as cp
# Insertar clubes
def insertarclub(nombre,pais):
	db = cp.bbddliga()
	##################################################
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#INSERT:
	sql = "INSERT INTO club(nombre, pais, activo) VALUES (%s,%s,1)" # --> Activo indica que este equipo va a participar este año 
	valores = (nombre,pais)
	cursor.execute(sql,valores)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro insertado")
	# desconecta del servidor
	db.close()

# Insertar Jugadores
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

# Actualizar datos club
def updateclub(id_club):
	db = cp.bbddliga()
	cursor = db.cursor()
	sql="call ActualizarValoresCLUB(%s);"
	cursor.execute(sql,id_club)
	# Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro actualizado")
	db.close()




# Consultas


# Seleccionar club a partir del nombre
def SelectClub(nombre):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select id from club where nombre = %s"
	cursor.execute(sql,nombre)
	dato = cursor.fetchone()
	id_club = dato[0]
	db.close()
	return(id_club)

def selectValorClub(id_club):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select ValorTotal from club where id = %s"
	cursor.execute(sql,id_club)
	dato = cursor.fetchone()
	ValorTotal = int(dato[0])
	db.close()
	return(ValorTotal)

# Devuelve en una lista el id de los equipos que van a jugar la temporada
def selectActivoClub():
	db = cp.bbddliga()
	cursor = db.cursor()
	sql = "select id from club where activo = 1"
	cursor.execute(sql)
	datos = cursor.fetchall()
	db.close()
	clubes = []
	for row in datos:
		clubes.append(row[0])
	return(clubes)
