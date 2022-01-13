--Borrado de los datos

--Datos de estadisticas partido
DECLARE @b as INT;
declare @t as int;
set @t = 1;
select @b = max(id) FROM prueba_partidos;
while @t <= @b
begin
delete from prueba_Estadisticas_partido where id_partido = @t;
set @t = @t+1;
end
go
--Datos partido
declare @i as int;
set @i = 1;
declare @a as int;
select @a = max(jornada) from prueba_partidos;
while @i <= @a
begin
delete from prueba_clasificacion where id_club = @i;
delete from prueba_partidos where jornada = @i;
set @i = @i+1;
end
go
--Datos estadisticas_locales
 declare @a as int;
  select @a = max(id) from jugadores;
  declare @i as int;
  set @i = 1;
  declare @jugador as int;
  while  @i<= @a
  begin
  select @jugador = id from jugadores where id = @i;
  delete from prueba_estadisticasTotales where id_jugador = @jugador;
  set @i= @i +1;
  end

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

