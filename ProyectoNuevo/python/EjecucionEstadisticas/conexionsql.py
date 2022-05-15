# Abre conexion con la base de datos
import re
import sys
from turtle import update
from datetime import date
from colorama import Cursor
sys.path.append('ProyectoLiga')
import conexionpython as cp


###Insert y updates:
# Insertar clubes
def insertarclub(nombre,pais):
	db = cp.bbddliga()
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
# Insertar arbitros:
def insertarAbitros(arbitro):
	# print(datos_jugadores)
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#INSERT:
	sql = "INSERT INTO arbitros(nombre) VALUES (%s)"
	cursor.execute(sql,arbitro)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro insertado")
	# desconecta del servidor
	db.close()



#Insertar partidos
def insertarPartidos(datos_partido):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#INSERT:
	sql = "INSERT INTO partidos(id_local,id_visitante,goles_local,goles_visitante,id_arbitro,aforo,jornada,temporada) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	cursor.execute(sql,datos_partido)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro insertado")
	# desconecta del servidor
	db.close()
#Insertar Estadisticas partidos
def insertarEstadisticasPartidos(estadisticas_partido):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#INSERT:
	sql = "INSERT INTO estadisticas_partido(id_jugador,id_partido,goles,asistencias,amarillas,rojas,titular) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	cursor.execute(sql,estadisticas_partido)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro insertado")
	# desconecta del servidor
	db.close()



	
#Insertar Temporada
def insertarTemporada():
	fecha_inicio = date.today()
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#INSERT:
	sql = "INSERT INTO temporada(fecha_inicio) VALUES (%s)"
	cursor.execute(sql,fecha_inicio)

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

def updateclasificacion(id_local,gol_local,id_visitante, gol_visitante):
	datos =  [id_local,gol_local,id_visitante, gol_visitante]
	db = cp.bbddliga()
	cursor = db.cursor()
	sql="call actualizarClasificacion(%s,%s,%s,%s);"
	cursor.execute(sql,datos)
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

def selectNombreClub(id_club)
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select nombre from club where id = %s;"
	cursor.execute(sql,id_club)
	dato = cursor.fetchone()
	nombre = dato[0]
	db.close()
	return(nombre)
def selectValorClub(id_club):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select ValorTotal from club where id = %s;"
	cursor.execute(sql,id_club)
	dato = cursor.fetchone()
	ValorTotal = int(dato[0])
	db.close()
	return(ValorTotal)
def selectJugadores(id_club):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select id,posicion, valor from jugadores where id_club = %s order by valor desc;"
	cursor.execute(sql,id_club)
	datos = cursor.fetchall()
	db.close()
	jugadores = []
	for row in datos:
		jugador = {}
		jugador["id"]=row[0]
		jugador["posicion"] = row[1]
		jugador["valor"] = row[2]
		jugadores.append(jugador)
	return(jugadores)
# Devuelve en una lista el id de los equipos que van a jugar la temporada
def selectActivoClub():
	db = cp.bbddliga()
	cursor = db.cursor()
	sql = "select id from club where activo = 1;"
	cursor.execute(sql)
	datos = cursor.fetchall()
	db.close()
	clubes = []
	for row in datos:
		clubes.append(row[0])
	return(clubes)

def selectJornada():
	db = cp.bbddliga()
	cursor = db.cursor()
	sql = "select jornada from partidos order by jornada desc;"
	cursor.execute(sql)
	dato = cursor.fetchone()
	if dato:
		jornada = int(dato[0])
	else:
		jornada = 0
	db.close()
	return int(jornada)+1

def selectTemporada():
	db = cp.bbddliga()
	cursor = db.cursor()
	sql = "select temporada from partidos order by temporada desc;"
	cursor.execute(sql)
	dato = cursor.fetchone()
	if dato:
		temporada = int(dato[0])
	else:
		temporada = 1
	db.close()
	return int(temporada)

def selectPartido():
	db = cp.bbddliga()
	cursor = db.cursor()
	sql = "select id from partidos order by id desc;"
	cursor.execute(sql)
	dato = cursor.fetchone()
	if dato:
		partido = int(dato[0])
	else:
		partido = 1
	db.close()
	return int(partido)

