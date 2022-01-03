CREATE OR ALTER TRIGGER añadidosHistoricoCLub
on club
for UPDATE
as
BEGIN 
SET NOCOUNT ON;
if UPDATE(ValorTotal)
BEGIN
INSERT INTO HistoricoClub
select id,nJugadores,nExtranjeros,ValorTotal,getdate()
FROM deleted
end
END
