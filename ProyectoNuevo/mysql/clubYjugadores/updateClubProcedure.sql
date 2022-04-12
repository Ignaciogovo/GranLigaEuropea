-- PROCEDURE PARA ACTUALIZAR clubes
USE liga;
drop procedure if exists ActualizarValoresCLUB;
delimiter //
create procedure ActualizarValoresCLUB( numclub int)
begin
	update club set nJugadores = (
		SELECT count(*) FROM jugadores where id_club = numclub
		group by id_club
        ),
    ValorTotal = (
		SELECT sum(valor) FROM jugadores where id_club = numclub
		group by id_club)
        where id = numclub;
end //
DELIMITER ;
call ActualizarValoresCLUB(8);