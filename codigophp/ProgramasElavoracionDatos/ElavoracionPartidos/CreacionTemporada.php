<?php
    include_once('functionClub.php');
    $jornada=calculoJornada();
    if ($jornada < 31){
        echo "Debe terminar la temporada";
    }else{
        $temporadaPartidos = calculoTemporada();
        $temporadatabla = calculotablaTemporada();
        if ($temporadaPartidos == $temporadatabla){
            $temporadatabla++;
            creacionTemporada($temporadatabla);
            echo "Generandose la temporada número:  $temporadatabla";
        }else{
            echo  "Ya se ha iniciado la temporada anteriormente";
        }
    }
    echo "<a href='index.php'>Vuelta al inicio</a>";   
?>