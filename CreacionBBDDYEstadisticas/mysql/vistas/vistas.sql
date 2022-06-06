-- clasificación view    vista mas leíble de la clasificacion:
CREATE VIEW `clasificacionview` AS
select ROW_NUMBER() over (order by puntos desc,(golesAfavor-golesEncontra) desc) as puesto,club.nombre, puntos,golesAfavor,golesEncontra,(golesAfavor-golesEncontra) as diferenciaGoles,partidosGanados,partidosEmpatados,partidosPerdidos, id_club 
from clasificacion inner join club
on clasificacion.id_club=club.id
where temporada = (select max(id) from temporada)
order by puesto


-- vista más leíble
create view partidosview as
select p.id as partido, c1.nombre as local, p.goles_local as goles_local,c2.nombre as visitante, p.goles_visitante as goles_visitante, a.nombre as arbitro, aforo, jornada 
from partidos as p
inner join club as c1
on p.id_local = c1.id
inner join club as c2
on p.id_visitante = c2.id
inner join arbitros as a
on p.id_arbitro = a.id
order by jornada


-- Estadisticas_totales

drop view estadisticas_totales;
create view estadisticas_totales as
select j.nombre, sum(goles) as goles, sum(asistencias) as asistencias, sum(amarillas) as amarillas, sum(rojas) as rojas, 
		sum(titular) vecesTitular,count(estadisticas_partido.id) partidosTotales,j.posicion as posicion,j.valor as valor,
        club.nombre as club, j.id
from estadisticas_partido
inner join jugadores as j
on j.id=estadisticas_partido.id_jugador
inner join club 
on club.id = j.id_club
group by id_jugador
order by goles desc, asistencias desc,amarillas desc, rojas desc;

