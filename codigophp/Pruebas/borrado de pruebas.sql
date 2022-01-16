--Borrado de los datos

--Datos de estadisticas partido
delete from prueba_Estadisticas_partido
--Datos partido
delete from prueba_clasificacion;;
delete from prueba_partidos;
--Datos estadisticas_locales
  delete from prueba_estadisticasTotales;
 -- Temporadas
 delete from prueba_Temporadas

--Regeneari�n datos clasificacion
INSERT INTO [prueba_clasificacion] (id_club,puntos,golesAfavor,golesEncontra)
VALUES
  (1,0,0,0),
  (2,0,0,0),
  (3,0,0,0),
  (4,0,0,0),
  (5,0,0,0),
  (6,0,0,0),
  (7,0,0,0),
  (8,0,0,0),
  (9,0,0,0),
  (10,0,0,0);
  go
INSERT INTO [prueba_clasificacion] (id_club,puntos,golesAfavor,golesEncontra)
VALUES
  (11,0,0,0),
  (12,0,0,0),
  (13,0,0,0),
  (14,0,0,0),
  (15,0,0,0),
  (16,0,0,0);

go
   --prueba_estadisticasTotales
  declare @a as int;
  select @a = max(id) from jugadores;
  declare @i as int;
  set @i = 1;
  declare @jugador as int;
  while  @i<= @a
  begin
  select @jugador = id from jugadores where id = @i;
  INSERT INTO [prueba_estadisticasTotales] (id_jugador,goles,amarillas,rojas,Partidos_titular)
  VALUES
  (@jugador,0,0,0,0);
  set @i= @i +1;
  end
  go

