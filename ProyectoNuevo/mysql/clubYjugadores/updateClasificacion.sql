delimiter $$
create procedure actualizarClasificacion(id_local int, gol_local int, id_visitante int, gol_visitante int, id_temporada int)
begin
update clasificacion set golesAfavor=golesAfavor+gol_local where id_club = id_local and temporada = id_temporada;
update clasificacion set golesAfavor=golesAfavor+gol_visitante,temporada = id_temporada where id_club = id_visitante;
if gol_local < gol_visitante then
	update clasificacion set partidosPerdidos=partidosPerdidos+1 where id_club = id_local and temporada = id_temporada;
    update clasificacion set puntos=puntos+3, partidosPerdidos=partidosGanados+1 where id_club = id_visitante  and temporada = id_temporada;
elseif gol_local > gol_visitante then
		update clasificacion set partidosPerdidos=partidosPerdidos+1 where id_club = id_visitante and temporada = id_temporada;
    update clasificacion set puntos=puntos+3, partidosPerdidos=partidosGanados+1, temporada = id_temporada where id_club = id_local;
elseif gol_local = gol_visitante then
	update clasificacion set puntos=puntos+1, partidosEmpatados=partidosEmpatados+1 where id_club = id_visitante and temporada = id_temporada;
    update clasificacion set puntos=puntos+1, partidosEmpatados=partidosEmpatados+1 where id_club = id_local and temporada = id_temporada;
end if;
end$$
delimiter ;