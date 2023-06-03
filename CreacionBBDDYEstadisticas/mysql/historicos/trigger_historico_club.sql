





--- TRIGGER PARA UPDATE 
DROP TRIGGER IF EXISTS update_historicoClub;
DELIMITER //

CREATE TRIGGER update_historicoClub
BEFORE UPDATE ON club
FOR EACH ROW
BEGIN
	DECLARE temporada_id INT;
	SELECT MAX(id) INTO temporada_id
	FROM temporada;
	IF NEW.nJugadores <> OLD.nJugadores  THEN
		INSERT INTO historico_club (id_club, nombre, nJugadores, ValorTotal, temporada)
		VALUES (OLD.id, OLD.nombre, OLD.nJugadores, OLD.ValorTotal, temporada_id);
	ELSE
		IF NEW.ValorTotal <> OLD.ValorTotal  THEN
			INSERT INTO historico_club (id_club, nombre, nJugadores, ValorTotal, temporada)
			VALUES (OLD.id, OLD.nombre, OLD.nJugadores, OLD.ValorTotal, temporada_id);
		END IF;
	END IF;

END //

DELIMITER ;



------ TRIGGER PARA DELETE
DELIMITER //

CREATE TRIGGER delete_historicoClub
AFTER DELETE ON club
FOR EACH ROW
BEGIN
declare temporada_id int;
select max(id) into temporada_id
from temporada;
  INSERT INTO historico_club(id_club,nombre,nJugadores,ValorTotal,temporada)
  VALUES (OLD.id,old.nombre,old.nJugadores,old.ValorTotal,temporada_id);
END //

DELIMITER ;
