DROP PROCEDURE IF EXISTS `database`.insert_historico_jugadores;

DELIMITER $$
$$
CREATE PROCEDURE `database`.insert_historico_jugadores()
BEGIN
	 DECLARE max_temporada INT;
    
    -- Obtener el valor máximo de la temporada desde la tabla 'temporada'
    SELECT MAX(id) INTO max_temporada FROM temporada;
    
    -- Realizar la inserción en la tabla 'historico_jugadores' con los datos de 'jugadores' y la temporada máxima
    INSERT INTO historico_jugadores (id_jugador, nombre, id_club, posicion, peso, altura, nacionalidad, valor, FechaNacimiento, temporada)
    SELECT id, nombre, id_club, posicion, peso, altura, nacionalidad, valor, FechaNacimiento, max_temporada
    FROM jugadores;
END$$
DELIMITER ;
