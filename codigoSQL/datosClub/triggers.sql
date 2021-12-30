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



-- Trigger valor club tras un insert
CREATE OR ALTER TRIGGER modificador2_club
on jugadores
for insert
as
begin
declare @club as int;
select @club = id_club from inserted
exec rellenoclub @club;
end;
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