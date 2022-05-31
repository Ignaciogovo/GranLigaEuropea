-- PROCEDURE PARA ACTUALIZAR clubes
USE liga;
drop procedure if exists ActualizarValoresCLUB;
delimiter //
create procedure ActualizarValoresCLUB( numclub int)
begin
	update club set nJugadores = (
		SELECT count(*) FROM jugadores where id_club = numclub and activo = 1
        ),
    ValorTotal = (
		SELECT sum(valor) FROM jugadores where id_club = numclub and activo = 1)
        where id = numclub;
end //
DELIMITER ;
--call ActualizarValoresCLUB(8);