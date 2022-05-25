

-- Actualizar Clasificacion:
CREATE DEFINER=`pollito`@`%` PROCEDURE `actualizarClasificacion`(id_local int, gol_local int, id_visitante int, gol_visitante int, id_temporada int)
begin
-- Asignamos los goles a favor y encontra de cada Equipo
update clasificacion set golesAfavor=golesAfavor+gol_local, golesEncontra=golesEncontra+gol_visitante where id_club = id_local and temporada = id_temporada;
update clasificacion set golesAfavor=golesAfavor+gol_visitante, golesEncontra=golesEncontra+gol_local where id_club = id_visitante and temporada = id_temporada;
-- Si visitante gana:
if gol_local < gol_visitante then
	update clasificacion set partidosPerdidos=partidosPerdidos+1 where id_club = id_local and temporada = id_temporada;
    update clasificacion set puntos=puntos+3, partidosGanados=partidosGanados+1 where id_club = id_visitante  and temporada = id_temporada;
-- Si local gana:
elseif gol_local > gol_visitante then
		update clasificacion set partidosPerdidos=partidosPerdidos+1 where id_club = id_visitante and temporada = id_temporada;
    update clasificacion set puntos=puntos+3, partidosGanados=partidosGanados+1 where id_club = id_local and temporada = id_temporada;
-- Si se produce un empate
elseif gol_local = gol_visitante then
	update clasificacion set puntos=puntos+1, partidosEmpatados=partidosEmpatados+1 where id_club = id_visitante and temporada = id_temporada;
    update clasificacion set puntos=puntos+1, partidosEmpatados=partidosEmpatados+1 where id_club = id_local and temporada = id_temporada;
end if;
end