-- clasificación view    vista mas legible de la clasificacion:
CREATE VIEW `clasificacionview` AS
select ROW_NUMBER() over (order by puntos desc,(golesAfavor-golesEncontra) desc) as puesto,club.nombre, puntos,golesAfavor,golesEncontra,(golesAfavor-golesEncontra) as diferenciaGoles,partidosGanados,partidosEmpatados,partidosPerdidos, id_club 
from clasificacion inner join club
on clasificacion.id_club=club.id
where temporada = (select max(id) from temporada)
order by puesto

-- procedure de estadisticas de un partido en concreto 
	delimiter //
	create procedure P_EstadisticasPartido(variable1 int)
	begin
	select j.nombre, goles, asistencias, amarillas, rojas, j.posicion as posicion,
				case when j.valor >1000000 then concat(round((j.valor / 1000000),2),'M')
					when j.valor <1000000 then concat(round((j.valor / 1000),2),'K')
					when j.valor =1000000 then '1M'
					end as valor,
			club.nombre as club, j.id
	from estadisticas_partido
	inner join jugadores as j
	on j.id=estadisticas_partido.id_jugador
	inner join club 
	on club.id = j.id_club
	where estadisticas_partido.id_partido = variable1
	order by goles desc, asistencias desc,amarillas desc, rojas desc;
	end //
	delimiter ;


	-- Procedure de estadisticas de un equipo:
	delimiter //
    create procedure EstadisticasEquipo(variable1 int)
	begin
		if variable1 = 0 then
			select j.id,j.nombre,goles,asistencias,amarillas,rojas,vecesTitular,es.partidosTotales,j.posicion,
			case when j.valor >1000000 then concat(round((j.valor / 1000000),2),'M')
				when j.valor <1000000 then concat(round((j.valor / 1000),2),'K')
				when j.valor =1000000 then '1M'
				end as valor
			from estadisticas_totales as es
			right join jugadores as j
			on es.nombre = j.nombre
			order by field(j.posicion, 'Portero','Defensa','Centrocampista','Delantero'),goles desc,asistencias desc;
        else
			select j.id,j.nombre,goles,asistencias,amarillas,rojas,vecesTitular,es.partidosTotales,j.posicion,
				case when j.valor >1000000 then concat(round((j.valor / 1000000),2),'M')
				when j.valor <1000000 then concat(round((j.valor / 1000),2),'K')
				when j.valor =1000000 then '1M'
				end as valor
			from estadisticas_totales as es
			right join jugadores as j
			on es.nombre = j.nombre
			where j.id_club = variable1
			order by field(j.posicion, 'Portero','Defensa','Centrocampista','Delantero'),goles desc,asistencias desc;
		end if;
    	end //
delimiter ;
call EstadisticasEquipo(12)

-- VIEW PARTIDOS

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




