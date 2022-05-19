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


USE liga;
DROP TABLE IF EXISTS estadios;

CREATE TABLE estadios(
id int primary key auto_increment,
nombre varchar(100) not null unique,
ciudad varchar(100) null,
capacidad int null
)AUTO_INCREMENT=1; 

DROP TABLE IF EXISTS club;
CREATE TABLE club (
  id int unsigned NOT NULL auto_increment,
  nombre varchar(100) UNIQUE,
  pais varchar(100),
  nJugadores int,
  ValorTotal int,
  activo int default 0,
  id_estadio int NULL,
  PRIMARY KEY (id),
  CONSTRAINT FK_estadio FOREIGN KEY (id_estadio) REFERENCES estadios(id)
) AUTO_INCREMENT=1;


DROP TABLE IF EXISTS jugadores;
CREATE TABLE jugadores (
  id int unsigned NOT NULL auto_increment,
  nombre  varchar(100) UNIQUE,
  id_club int unsigned,
  posicion varchar(100),
  peso varchar(100),
  altura varchar(100),
  nacionalidad varchar(100),
  valor int unsigned,
  FechaNacimiento Date,
  activo int DEFAULT 0,
   PRIMARY KEY (id),
  FOREIGN KEY (id_club) REFERENCES club(id)
)AUTO_INCREMENT=1;

DROP TABLE IF EXISTS arbitros;
CREATE TABLE arbitros(
id int not null auto_increment primary key,
nombre varchar(120) unique,
nacionalidad varchar(120) null,
FechaNacimiento date null
)AUTO_INCREMENT=1;

DROP TABLE IF EXISTS temporada;
CREATE TABLE temporada(
id int not null auto_increment primary key,
fecha_inicio DATE,
fecha_final DATE
)AUTO_INCREMENT=1;

DROP TABLE IF EXISTS partidos;
CREATE TABLE partidos(
id int not null auto_increment primary key,
id_local int unsigned,
id_visitante int unsigned,
goles_local int,
goles_visitante int,
id_arbitro int,
aforo varchar(10),
jornada int,
temporada int,
  CONSTRAINT FK_partidos_id_arbitro
    FOREIGN KEY (id_arbitro)
      REFERENCES arbitros(id),
  CONSTRAINT FK_partidos_ID_LOCAL
    FOREIGN KEY (id_local)
      REFERENCES club(id),
  CONSTRAINT FK_partidos_id_visitante
    FOREIGN KEY (id_visitante)
      REFERENCES club(id),
  CONSTRAINT FK_partidos_temporada
      FOREIGN KEY (temporada) 
      REFERENCES temporada(id)
)
DROP TABLE IF EXISTS clasificacion;
CREATE TABLE clasificacion(
id_club int unsigned primary key,
puntos INT DEFAULT 0,
golesAfavor INT DEFAULT 0,
golesEncontra INT DEFAULT 0,
partidosGanados INT DEFAULT 0,
partidosEmpatados  INT DEFAULT 0,
partidosPerdidos INT DEFAULT 0,
  CONSTRAINT FK_clasificacion_ID_club
    FOREIGN KEY (id_club)
      REFERENCES club(id)
);
DROP TABLE IF EXISTS estadisticas_partido;
CREATE TABLE estadisticas_partido(
id int PRIMARY KEY auto_increment,
id_jugador int unsigned not null,
id_partido int not null,
goles INT DEFAULT 0,
asistencias INT DEFAULT 0,
amarillas INT DEFAULT 0,
rojas INT DEFAULT 0,
titular int DEFAULT 0,
  CONSTRAINT FK_estadisticas_partido_id_jugador
    FOREIGN KEY (id_jugador)
      REFERENCES jugadores(id),
  CONSTRAINT FK_estadisticas_partido_id_partido
    FOREIGN KEY (id_partido)
      REFERENCES partidos(id)
)AUTO_INCREMENT=1;