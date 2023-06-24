# Abre conexion con la base de datos
from datetime import date
import conexionpython as cp
###Insert y updates:
# Insertar clubes
def insertarclub(nombre, pais, id_estadio):
    db = cp.bbddliga()
    cursor = db.cursor()

    # Verificar si el nombre del club ya existe en la tabla
    sql_select = "SELECT nombre FROM club WHERE nombre = %s"
    cursor.execute(sql_select, (nombre,))
    existing_row = cursor.fetchone()

    if existing_row:
        # Si el nombre del club existe, realizar una actualización
        sql_update = "UPDATE club SET activo = 1 WHERE nombre = %s"
        cursor.execute(sql_update, (nombre,))
    else:
        # Si el nombre del club no existe, realizar una inserción
        sql_insert = "INSERT INTO club(nombre, pais, activo, id_estadio) VALUES (%s, %s, 1, %s)"
        valores = (nombre, pais, id_estadio)
        cursor.execute(sql_insert, valores)

    db.commit()
    # print(cursor.rowcount, "registro insertado")

    db.close()

# Insertar Jugadores
def insertarjugador(datos_jugadores):
    db = cp.bbddliga()
    cursor = db.cursor()

    # Verificar si el nombre ya existe en la tabla
    nombre = datos_jugadores[0]
    sql_select = "SELECT nombre FROM jugadores WHERE nombre = %s"
    cursor.execute(sql_select, (nombre,))
    existing_row = cursor.fetchone()

    if existing_row:
        # Si el nombre existe, realizar una actualización
        sql_update = "UPDATE jugadores SET id_club = %s, posicion = %s, peso = %s, altura = %s, nacionalidad = %s, valor = %s, activo = 1 WHERE nombre = %s"
        cursor.execute(sql_update, datos_jugadores + (nombre,))
    else:
        # Si el nombre no existe, realizar una inserción
        sql_insert = "INSERT INTO jugadores(nombre, id_club, posicion, peso, altura, nacionalidad, valor, FechaNacimiento, activo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 1)"
        cursor.execute(sql_insert, datos_jugadores)

    db.commit()
    # print(cursor.rowcount, "registro insertado")

    db.close()
# Insertar arbitros:
def insertarArbitros(datos):
    db = cp.bbddliga()
    cursor = db.cursor()

    # Verificar si el nombre del árbitro ya existe en la tabla
    sql_select = "SELECT nombre FROM arbitros WHERE nombre = %s"
    cursor.execute(sql_select, (datos[0],))
    existing_row = cursor.fetchone()

    if existing_row:
        # Si el nombre del árbitro existe, realizar una actualización
        sql_update = "UPDATE arbitros SET activo = 1 WHERE nombre = %s"
        cursor.execute(sql_update, (datos[0],))
    else:
        # Si el nombre del árbitro no existe, realizar una inserción
        sql_insert = "INSERT INTO arbitros(nombre, nacionalidad, FechaNacimiento, activo) VALUES (%s, %s, %s, 1)"
        cursor.execute(sql_insert, datos)

    db.commit()
    # print(cursor.rowcount, "registro insertado")

    db.close()

# Insertar Estadios
def insertarEstadios(estadio):
    db = cp.bbddliga()
    cursor = db.cursor()

    # Verificar si el nombre del estadio ya existe en la tabla
    sql_select = "SELECT nombre FROM estadios WHERE nombre = %s"
    cursor.execute(sql_select, (estadio,))
    existing_row = cursor.fetchone()

    if existing_row:
        # Si el nombre del estadio existe, realizar una actualización
        sql_update = "UPDATE estadios SET nombre = %s WHERE nombre = %s"
        cursor.execute(sql_update, (estadio, estadio))
    else:
        # Si el nombre del estadio no existe, realizar una inserción
        sql_insert = "INSERT INTO estadios(nombre) VALUES (%s)"
        cursor.execute(sql_insert, (estadio,))

    db.commit()
    # print(cursor.rowcount, "registro insertado")

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
	# print(cursor.rowcount, "registro insertado")
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
	# print(cursor.rowcount, "registro insertado")
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

def insertarClasificacion():
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#INSERT:
	sql = "	insert into clasificacion(id_club,temporada) select id,(select max(id) from temporada) as temporada from club where activo = 1;"
	cursor.execute(sql)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro insertado")
	# desconecta del servidor
	db.close()

def finalizarTemporada():
	fecha_final = date.today()
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#UPDATE:
	sql = "UPDATE temporada set fecha_final = %s where id = (select id from(select max(id) from temporada) as tablaTemporal);"
	cursor.execute(sql,fecha_final)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registro actualizado")
	# desconecta del servidor
	db.close()
def AnularActivoClub():
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#UPDATE:
	sql = "UPDATE club set activo = 0 where id > 0;"
	cursor.execute(sql)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registros actualizados")
	# desconecta del servidor
	db.close()
def AnularActivoJugadores():
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# ejecuta el SQL query usando el metodo execute().

	#UPDATE:
	sql = "UPDATE jugadores set activo = 0 where id > 0;"
	cursor.execute(sql)

	   # Commit your changes in the database
	db.commit()
	print(cursor.rowcount, "registros actualizados")
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

def updateclasificacion(id_local,gol_local,id_visitante, gol_visitante,temporada):
	datos =  [id_local,gol_local,id_visitante, gol_visitante,temporada]
	db = cp.bbddliga()
	cursor = db.cursor()
	sql="call actualizarClasificacion(%s,%s,%s,%s,%s);"
	cursor.execute(sql,datos)
	# Commit your changes in the database
	db.commit()
	# print(cursor.rowcount, "registro actualizado")
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

def SelectEstadio(nombre):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select id from estadios where nombre = %s"
	cursor.execute(sql,nombre)
	dato = cursor.fetchone()
	id_estadio = dato[0]
	db.close()
	return(id_estadio)


def selectNombreClub(id_club):
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
	sql = "select id,posicion, valor from jugadores where id_club = %s and activo = 1 order by valor desc;"
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
	temporada = selectTemporada()
	if temporada == 0:
		jornada = 0
	else:
		db = cp.bbddliga()
		cursor = db.cursor()
		sql = "select jornada from partidos where temporada = %s order by jornada desc;"
		cursor.execute(sql,temporada)
		dato = cursor.fetchone()
		if dato:
			jornada = (int(dato[0])+1)
		else:
			jornada = 1
		db.close()
	return int(jornada)

def selectJornadaSinSuma():
	temporada = selectTemporada()
	if temporada == 0:
		jornada = 0
	else:
		db = cp.bbddliga()
		cursor = db.cursor()
		sql = "select jornada from partidos where temporada = %s order by jornada desc;"
		cursor.execute(sql,temporada)
		dato = cursor.fetchone()
		if dato:
			jornada = (int(dato[0]))
		else:
			jornada = 1
		db.close()
	return int(jornada)
def selectTemporada():
	db = cp.bbddliga()
	cursor = db.cursor()
	sql = "select id from temporada order by id desc;"
	cursor.execute(sql)
	dato = cursor.fetchone()
	if dato:
		temporada = int(dato[0])
	else:
		temporada = 0
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

# Partido anterior a la jornada actual
def selectIdPartidoClub(id_club):
	db = cp.bbddliga()
	cursor = db.cursor()
	sql = "select id from partidos where (id_local = %s or id_visitante = %s) and temporada = (select max(id) from temporada) order by jornada desc limit 1,1;" # limit 1,1 para escoger el penultimo partido(ya que el partido es insertando antes que las estadisticas de los jugadores)
	cursor.execute(sql,(id_club,id_club))
	dato = cursor.fetchone()
	if dato:
		partido = int(dato[0])
	else:
		partido = 0
	db.close()
	return int(partido)

def selectRojasAmarillas(id_jugador, id_partido):
	if id_partido == 0:
			amarillas = 0
			rojas = 0 
	else:
		db = cp.bbddliga()
		cursor = db.cursor()
		sql = "select amarillas,rojas from estadisticas_partido where id_jugador = %s and id_partido = %s  order by id desc;"
		cursor.execute(sql,(id_jugador,id_partido))
		dato = cursor.fetchone()
		if dato:
			amarillas = int(dato[0])
			rojas = int(dato[1])
		else:
			amarillas = 0
			rojas = 0
		db.close()
	tarjetas = [amarillas,rojas]
	return (tarjetas)

def SelectClub_Jugadores(id_jugador):
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select id_club from jugadores where id = %s"
	cursor.execute(sql,id_jugador)
	dato = cursor.fetchone()
	id_club = dato[0]
	db.close()
	return(id_club)


# Escoger campeon de liga:
def selectCampeonLiga():
	db = cp.bbddliga()
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "select nombre from clasificacionview where puesto = 1"
	cursor.execute(sql)
	dato = cursor.fetchone()
	id_club = dato[0]
	db.close()
	return(id_club)





print(selectCampeonLiga())