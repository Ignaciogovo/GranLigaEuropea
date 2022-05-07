delimiter $$
create procedure actualizarClasificacion(id_local int, gol_local int, id_visitante int, gol_visitante int)
begin
update clasificacion set golesAfavor=golesAfavor+gol_local where id_club = id_local;
update clasificacion set golesAfavor=golesAfavor+gol_visitante where id_club = id_visitante;
if gol_local < gol_visitante then
	update clasificacion set partidosPerdidos=partidosPerdidos+1 where id_club = id_local;
    update clasificacion set puntos=puntos+3, partidosPerdidos=partidosGanados+1 where id_club = id_visitante;
elseif gol_local > gol_visitante then
		update clasificacion set partidosPerdidos=partidosPerdidos+1 where id_club = id_visitante;
    update clasificacion set puntos=puntos+3, partidosPerdidos=partidosGanados+1 where id_club = id_local;
elseif gol_local = gol_visitante then
	update clasificacion set puntos=puntos+1, partidosEmpatados=partidosEmpatados+1 where id_club = id_visitante;
    update clasificacion set puntos=puntos+1, partidosEmpatados=partidosEmpatados+1 where id_club = id_local;
end if;
end$$
delimiter ;