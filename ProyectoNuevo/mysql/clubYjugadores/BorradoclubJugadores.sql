
select nombre, pais,nJugadores, ValorTotal, round((ValorTotal/nJugadores),3) as valorMedio  from club 
order by valorMedio,ValorTotal+0 desc; -- Con el +0 Convierte en int para que el orden sea correcto
-- inner join jugadores y club
select jugadores.nombre, club.nombre, posicion,nacionalidad, valor 
from jugadores inner join club 
on jugadores.id_club=club.id 
order by valor desc;


-- Borrar jugadores
delete from jugadores where id_club > 0 ;
alter table jugadores AUTO_INCREMENT=1;
-- Borrar club
delete from club where id > 0;
alter table club AUTO_INCREMENT=1;
-- Borrar arbitros:
delete  from arbitros where id > 0;
alter table  arbitros AUTO_INCREMENT=1;


-- Borrar partidos.
delete  from partidos where id > 0;
alter table  partidos AUTO_INCREMENT=1;
--  cantidad, club y valor total inner join
select count(*), club.nombre, sum(valor)  from jugadores inner join club on id_club=club.id
group by club.nombre
order by sum(valor) desc;




