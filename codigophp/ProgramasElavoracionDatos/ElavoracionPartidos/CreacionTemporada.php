<?php
    include_once('functionClub.php');
    $jornada=calculoJornada();
    $temporadaPartidos = calculoTemporada();
    $temporadatabla = calculotablaTemporada();
    if ($jornada == 1 and $temporadatabla == 0){
        $temporadatabla = 1;
        if ($temporadaPartidos == $temporadatabla){
            creacionTemporada($temporadatabla);
            echo "Generandose la temporada número:  $temporadatabla";
        }else{
            echo  "Ya se ha iniciado la temporada anteriormente ñljñjñlj";
        }
    }elseif($jornada > 30){
        if ($temporadaPartidos == $temporadatabla){
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