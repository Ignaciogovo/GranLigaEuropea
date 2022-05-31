

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


-- Procedure que indica todas las jornadas que ha participado un jugador:
	delimiter //
create procedure JornadasJugador(jugador int)
BEGIN
	SELECT 
    e.*, p.jornada
FROM
    estadisticas_partido AS e
        RIGHT JOIN
    partidos AS p ON e.id_partido = p.id
WHERE
    e.id_jugador = jugador
        AND e.id_partido IN (SELECT 
            par.id
        FROM
            partidos AS par
        WHERE
            par.temporada = (SELECT 
                    MAX(id)
                FROM
                    temporada))
ORDER BY jornada DESC;
END
delimiter ;

