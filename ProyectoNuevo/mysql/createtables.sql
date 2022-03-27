--club(id PK,nombre,ciudad,nJugadores,nExtranjeros,ValorTotal)
--Jugadores(id PK, nombre, id_club FK, posicion, peso, Altura, Nacionalidad,edad, valor)
--partidos(id PK, id_local FK, id_visitante FK,gol_local,gol_visitante,id_arbitro FK,aforo, jornada, temporada FK)
--temporadas(id PK,fecha_inicio,fecha_final)
--Estadisticas_partido(id PK, id_jugador FK, id_partido FK,goles,asistencias, amarillas, roja, titularidad)
--EstadisticasTotales(id_jugador PK FK, goles,asistencias, amarillas, rojas, partidos_titular)
--arbitros(id PK, nombre, nacionalidad, edad)
--clasificacion (id_equipo PK FK, puntos, goles)
--ClasificacionTemporadas(id PK, id_club FK, puntos, golesAfavor,golesEncontra, temporada FK)
--estadios(nombre, id_equipo PK FK,capacidad)


DROP TABLE IF EXISTS club;
CREATE TABLE club (
  id int unsigned NOT NULL auto_increment,
  nombre varchar(100) UNIQUE,
  pais varchar(100),
  nJugadores int,
  nExtranjeros int,
  ValorTotal varchar(100),
  PRIMARY KEY (id)
) AUTO_INCREMENT=1;

DROP TABLE IF EXISTS jugadores;
CREATE TABLE jugadores (
  id int unsigned NOT NULL auto_increment,
  nombre varchar(100),
  id_club int unsigned,
  posicion varchar(100),
  peso varchar(100),
  altura varchar(100),
  nacionalidad varchar(100),
  valor int unsigned,
  FechaNacimiento Date,
   PRIMARY KEY (id),
  FOREIGN KEY (id_club) REFERENCES club(id)
)AUTO_INCREMENT=1;
