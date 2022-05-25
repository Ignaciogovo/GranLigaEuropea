delimiter //
    create procedure EstadisticasEquipo(variable1 int)
	begin
		select j.id,j.nombre,es.partidosJugados,goles,asistencias,amarillas,rojas,vecesTitular,j.posicion,
		case when j.valor >1000000 then concat(round((j.valor / 1000000),2),'M')
			when j.valor <1000000 then concat(round((j.valor / 1000),2),'K')
			when j.valor =1000000 then '1M'
			end as valor
		from estadisticas_totales as es
		right join jugadores as j
		on es.nombre = j.nombre
		where j.id_club = variable1
		order by field(j.posicion, 'Portero','Defensa','Centrocampista','Delantero'),goles desc,asistencias desc;
    	end //
delimiter ;
-- call EstadisticasEquipo(12)


-- clasificación view    vista mas legible de la clasificacion:
CREATE VIEW `clasificacionview` AS
select ROW_NUMBER() over (order by puntos desc,(golesAfavor-golesEncontra) desc) as puesto,club.nombre, puntos,golesAfavor,golesEncontra,(golesAfavor-golesEncontra) as diferenciaGoles,partidosGanados,partidosEmpatados,partidosPerdidos, id_club 
from clasificacion inner join club
on clasificacion.id_club=club.id
where temporada = (select max(id) from temporada)
order by puesto