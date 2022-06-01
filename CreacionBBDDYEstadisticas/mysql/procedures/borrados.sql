
select nombre, pais,nJugadores, ValorTotal, round((ValorTotal/nJugadores),3) as valorMedio  from club 
order by valorMedio,ValorTotal+0 desc; -- Con el +0 Convierte en int para que el orden sea correcto
-- inner join jugadores y club
select jugadores.nombre, club.nombre, posicion,nacionalidad, valor 
from jugadores inner join club 
on jugadores.id_club=club.id 
order by valor desc;
-- Borrar clasificacion:
delete  from clasificacion where id_club > 0;
insert into clasificacion(id_club,temporada) select 
id,(select max(id) from temporada) as temporada from club;
alter table clasificacion AUTO_INCREMENT=1;
-- Borrar estadisticas partido
delete from estadisticas_partido where id > 0 ;
alter table estadisticas_partido AUTO_INCREMENT=1;
-- Borrar partidos.
delete  from partidos where id > 0;
alter table  partidos AUTO_INCREMENT=1;

-- Borrar Temporadas.
delete  from temporada where id > 0;
alter table  temporada AUTO_INCREMENT=1;
-- Borrar jugadores
delete from jugadores where id_club > 0 ;
alter table jugadores AUTO_INCREMENT=1;
-- Borrar club
delete from club where id > 0;
alter table club AUTO_INCREMENT=1;
-- Borrar arbitros:
delete  from arbitros where id > 0;
alter table  arbitros AUTO_INCREMENT=1;










drop procedure BorrarUltimaTemporada;
-- procedure de estadisticas de un partido en concreto 
	delimiter //
	create procedure BorrarUltimaTemporada()
	begin
    set @temporada = (select max(id) from temporada);
	SET SQL_SAFE_UPDATES = 0;
    -- Borrar Estadisticas de partido
    delete  from estadisticas_partido where id_partido in (select id from partidos where temporada = @temporada);
    alter table  estadisticas_partido AUTO_INCREMENT=1;
    -- Borramos partidos
    delete  from partidos where id  in (select id from (select id from partidos  where temporada = @temporada) as EliminarPartidos);
    alter table  partidos AUTO_INCREMENT=1;
-- Borrar clasificacion:
	delete  from clasificacion where id_club > 0 and temporada = @temporada;
    alter table  clasificacion AUTO_INCREMENT=1;
    delete from temporada where id = @temporada;
    alter table  temporada AUTO_INCREMENT=1;
    SET SQL_SAFE_UPDATES = 1;
    select "Temporada Borrada, Hay que iniciar temporada";
    -- select max(id) from temporada;
	-- -- alter table  temporada AUTO_INCREMENT= VALOR;
	-- select max(id) from estadisticas_partido;
	-- -- alter table  estadisticas_partido AUTO_INCREMENT= VALOR;
	-- select max(id) from partidos;
	-- -- alter table  partidos AUTO_INCREMENT=VALOR;
	end //
	delimiter ;
    call BorrarUltimaTemporada();








drop procedure BorrarTodasTemporadas;
-- procedure de borrar temporadas 
	delimiter //
	create procedure BorrarTodasTemporadas()
	begin

    -- Borrar Estadisticas de partido
    delete  from estadisticas_partido where id >0;
    alter table  estadisticas_partido AUTO_INCREMENT= 1;
    -- Borramos partidos
    delete  from partidos where id  >0;
    alter table  partidos AUTO_INCREMENT=1;
-- Borrar clasificacion:
	delete  from clasificacion where id_club > 0;
    alter table clasificacion  AUTO_INCREMENT= 1;
    delete from temporada where id> 0;
    alter table temporada  AUTO_INCREMENT= 1;
	end //
	delimiter ;




