

-- Actualizar Clasificacion:
CREATE PROCEDURE `actualizarClasificacion`(id_local int, gol_local int, id_visitante int, gol_visitante int, id_temporada int)
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




-- Actualizar clasificación jornada todas las jornadas


CREATE PROCEDURE `insercion_clasificiacionJornada`(IN jornadaFinal INT, IN temporadaEspecifica INT)
BEGIN
declare equipo int;
declare jornadaEspecifica int;
set jornadaEspecifica = 1;

-- Creamos el loop jornada
loop_jornada: LOOP
	-- Si jornada es mayor que el total de jornadas producidas termina el loop
	if jornadaEspecifica > jornadaFinal THEN
		LEAVE loop_jornada;
	end if;
-- Borramos todos los datos de esa jornada:
DELETE from clasificacion_jornada where jornada  = jornadaEspecifica;

-- Borramos los datos de la tabla temporal o la creamos si no está creada
if (SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema = 'liga' AND table_name = 'tabla_temporal')) = 1 then
    delete from tabla_temporal;
else
    CREATE TABLE tabla_temporal (
        id_cj INT PRIMARY KEY,
        puesto INT
    );
end if;

-- Indicamos que el equipo es uno
set equipo = 1;
-- Creamos loop_equipo
	loop_equipo: LOOP
		-- Si el club es mayor al id maximo de los clubes termina el loop ( Esto hay que modificarlo cuando haya más clubes)
		if equipo > (select max(id) from club where activo = 1) then
			leave loop_equipo;
		end if;
		-- Si el equipo se encuentra en activo se inserta en la clasificacion_jornada
		if equipo in (select id from club where activo = 1) THEN 
			insert into clasificacion_jornada(id_club,puntos,golesAfavor,golesEncontra,partidosGanados,partidosEmpatados,partidosPerdidos,jornada,temporada)
			SELECT 
				equipo as id_club,
				SUM(victorias) + SUM(empates) AS puntos,
				SUM(favor) AS goles_favor,
				SUM(contra) AS goles_contra,
				floor(sum(victorias)/3) as total_victorias,
				floor(sum(empates)/3) as total_empates,
				sum(derrotas) total_derrotas,
				jornadaEspecifica,
				temporadaEspecifica as temporada
			FROM
				(SELECT 
					SUM(CASE
							WHEN goles_local > goles_visitante THEN 3
							ELSE 0
						END) victorias,
						SUM(CASE
							WHEN goles_local = goles_visitante THEN 1
							ELSE 0
						END) empates,
						SUM(CASE
							WHEN goles_local < goles_visitante THEN 1
							ELSE 0
						END) derrotas,
						sum(goles_local) AS favor,
						sum(goles_visitante) AS contra,
						'local'
				FROM
					partidos
				WHERE
					id_local = equipo AND jornada <= jornadaEspecifica
						AND temporada = temporadaEspecifica
					UNION SELECT 
					SUM(CASE
							WHEN goles_local < goles_visitante THEN 3
							ELSE 0
						END) victorias,
						SUM(CASE
							WHEN goles_local = goles_visitante THEN 1
							ELSE 0
						END) empates,
						SUM(CASE
							WHEN goles_local > goles_visitante THEN 1
							ELSE 0
						END) derrotas,
						sum(goles_visitante) AS favor,
						sum(goles_local) AS contra,
						'visitante'
				FROM
					partidos
				WHERE
					id_visitante = equipo AND jornada <= jornadaEspecifica
						AND temporada = temporadaEspecifica
					) AS prueba;
			end if;
			-- Sumamos uno más a equipo;
			set equipo = equipo + 1;
			-- Iteramos loop_equipo
			ITERATE loop_equipo;
			-- Terminamos lopp equipo
        end loop;

if (SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema = 'liga' AND table_name = 'tabla_temporal')) = 1 then
            -- Realizamos el insert en la tabla temporal
        insert into tabla_temporal(id_cj,puesto) 
		SELECT
		id,
		row_number() OVER (ORDER BY cj.puntos desc,(cj.golesAfavor - cj.golesEncontra) desc,cj.golesAfavor desc,cj.golesEncontra asc )
		as puesto
		FROM liga.clasificacion_jornada cj where jornada = jornadaEspecifica and temporada = temporadaEspecifica;
END IF;
        -- Actualizamos el puesto de la jornada
        UPDATE clasificacion_jornada cj 
        INNER JOIN tabla_temporal tt ON cj.id = tt.id_cj
        SET cj.puesto = tt.puesto;
       
		-- Sumamos uno más a la jornadaEspecifica;
		set jornadaEspecifica = jornadaEspecifica +1;
        -- iteramos loop_jornada
		ITERATE loop_jornada;
-- Terminamos el loop_jornada
END LOOP;

-- Borramos la tabla_temporal
drop table tabla_temporal;
END









-- Actualizar clasificacion jornada última jornada
CREATE PROCEDURE `insertar_clasificacion_ultima_jornada`(pJornada int,pTemporada int)
BEGIN
	DECLARE rowCount INT;
    -- Verificar la existencia de los valores en la tabla
    SELECT COUNT(*) INTO rowCount
    FROM clasificacion_jornada
    WHERE jornada = pJornada AND temporada = pTemporada;
    
    -- Devolver el resultado
    IF rowCount > 0 THEN
        SELECT 'Los valores existen en la tabla.';
    ELSE
        insert into clasificacion_jornada(
		id_club
		, puesto
		, puntos
		, golesAfavor
		, golesEncontra
		, partidosGanados
		, partidosEmpatados
		, partidosPerdidos
		, jornada
		, temporada
		)
		select
		id_club
		, puesto
		, puntos
		, golesAfavor
		, golesEncontra
		, partidosGanados
		, partidosEmpatados
		, partidosPerdidos
        ,pJornada
        ,pTemporada
		FROM liga.clasificacionview;
    END IF;
END


