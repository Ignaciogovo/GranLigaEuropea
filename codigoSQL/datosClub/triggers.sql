-- TRIGGER para modificar el valor del club si se modifica el valor de un jugador
CREATE OR ALTER TRIGGER modificador_club
on jugadores
for update
as
begin
if update(valor)
begin
declare @club as int;
select @club = id_club from inserted
exec rellenoclub @club;
end;
end;
GO


-- Trigger valor club tras un insert
CREATE OR ALTER TRIGGER modificador2_club 
on jugadores
for insert
as
begin
declare @club as int;
select @club = id_club from inserted --Los inserted con muchos datos solo cogen el ultimo por lo tanto se tiene que hacer de otra forma aunque sea más lenta.
exec rellenoclub @club;
end;
go

--Version 2 trigger valor club tras un insert
--Esta opcion esta desactivada a menos que metamos en un insert varios id_club
CREATE OR ALTER TRIGGER modificador2_club 
on jugadores
for insert
as
declare @a as int;
set @a = 1;
while @a < 17
begin
exec rellenoClub @a
set @a = @a+1;
end;
go
-- Trigger valor club tras un delete
CREATE OR ALTER TRIGGER modificador3_club
on jugadores
for delete
as
begin
declare @club as int;
select @club = id_club from deleted
exec rellenoclub @club;
end;