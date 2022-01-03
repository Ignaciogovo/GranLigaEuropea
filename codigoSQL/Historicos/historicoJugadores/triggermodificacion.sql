CREATE OR ALTER TRIGGER insertarHistoricos
on jugadores
for UPDATE
as
BEGIN 
SET NOCOUNT ON;
if UPDATE(Valor)
BEGIN
INSERT into historicoJugadores
select id, id_club,valor, GETDATE() FROM deleted
end
if UPDATE(id_club)
BEGIN
INSERT into historicoJugadores
select id, id_club,valor, GETDATE() FROM deleted
end
END