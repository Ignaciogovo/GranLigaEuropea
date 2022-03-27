<?php
    include_once('functionClub.php');
    $jornada=calculoJornada();
    $temporadaPartidos = calculoTemporada();
    $temporadatabla = calculotablaTemporada();
    if ($jornada == 1 and $temporadatabla == 0){ //Condicion para la temporada 1
        $temporadatabla = 1;
        if ($temporadaPartidos == $temporadatabla){ //Con esta condicion comprobamos que no se creen más de una temporada a la vez.
            creacionTemporada($temporadatabla);
            echo "Generandose la temporada número:  $temporadatabla";
        }else{
            echo  "Ya se ha iniciado la temporada anteriormente ñljñjñlj";
        }
    }elseif($jornada > 30){ //Condicion al finalizar una temporada
        if ($temporadaPartidos == $temporadatabla){ //Con esta condicion comprobamos que no se creen más de una temporada a la vez.
            $temporadatabla++;
            creacionTemporada($temporadatabla);
            echo "Generandose la temporada número:  $temporadatabla";
        }else{
            echo  "Ya se ha iniciado la temporada anteriormente";
        }
    }else{
        echo "Debe terminar la temporada";
    }
    echo "<a href='index.php'>Vuelta al inicio</a>";   
?>