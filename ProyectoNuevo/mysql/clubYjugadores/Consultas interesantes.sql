
-- Indica las goleadas de los locales y visitantes cuando el aforo es mayor que 80
CREATE VIEW goleadasMayor80 AS 
SELECT (select nombre from club where club.id=id_local) as local, null as visitante, count(*) goleadasLocal, null goleadasVisitante
from 
partidos where
(goles_local >=3 and convert(replace(aforo,'%',''),decimal)>=80)
group by id_local
union
select null,(select nombre from club where club.id=id_visitante), null, count(*)
from partidos
where (goles_visitante >=3 and convert(replace(aforo,'%',''),decimal)>=80)
group by id_visitante
;
select * from goleadasMayor80
order by goleadasLocal desc, goleadasVisitante desc


-- Jugadores que cumplen cumpleaños el mismo dia:
select j.*, ju.cuenta
from jugadores as j
inner join
(select FechaNacimiento, count(*) as cuenta
	from jugadores 
	group by FechaNacimiento) as ju
on j.FechaNacimiento=ju.FechaNacimiento
where ju.cuenta > 1
order by FechaNacimiento desc;

-- Comprobar que no hay más goles y asistencias en las estadisticas de los jugadores que en el partido:
(select id_partido as partido, sum(goles) as goles ,sum(asistencias) as asistencias from estadisticas_partido
group by id_partido

)
UNION -- ALL
(select partidos.id as partido, sum(goles_local+goles_visitante), null from partidos
group by partidos.id
) order by partido;



-- Media de goles Por partido:

SELECT AVG(goles_local+goles_visitante) as mediaGoles, count(id) as total_Partidos 
FROM partidos;





-- Comprobar estadisticas de un jugador por jornada

select estadisticas_partido.*, jornada from estadisticas_partido 
inner join partidos
on id_partido = partidos.id
where id_jugador = 466
order by jornada desc;