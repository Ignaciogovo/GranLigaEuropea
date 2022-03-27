--Procedure para rellenar los datos desde la tabla jugadores.
CREATE OR ALTER PROCEDURE rellenoClub @club int
as
	--Declaracion Variables
	declare @njuga as int;
	select @njuga = count(*) from jugadores where id_club=@club; --Número de jugadores
	declare @valorT as int;
	select @valorT = sum(convert(int,valor)) from jugadores where id_club=@club; --Valor total de un club
	declare @nex as int;
	select @nex = count(*) from jugadores where id_club=@club and nacionalidad <>'España'; --Número de jugadores extranjeros
	--Actualizar datos
	update club set nJugadores=@njuga where id=@club;
	update club set nExtranjeros=@nex where id=@club;
	update club set ValorTotal=@valorT where id=@club;
GO
--Formula para ejecutarlo a todos los equipos.
declare @a as int;
set @a = 1;
while @a < 17
begin
exec rellenoClub @a
set @a = @a+1;
end;

