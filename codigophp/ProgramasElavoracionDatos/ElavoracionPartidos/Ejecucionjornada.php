<?php
    include('functionClub.php');
        $jornada=calculoJornada();
        $n_temporada=calculoTemporada();
        $temporadatabla = calculotablaTemporada();
        if ($n_temporada != $temporadatabla){
            $jornada = 1;
        }
    if ($jornada > 30){
        echo "Debe esperar a una nueva temporada";
    }else{
        echo "Inicio Jornada";
        $array1= array(2);
        $v1=3;
        while ($v1<9){
            array_push($array1,$v1);
            $v1++;
        }
        echo "<br>";
        $array2= array(9);
        $v1=10;
        while ($v1<17){
            array_push($array2,$v1);
            $v1++;
        }
       
        planificacionjornadasParaliga($jornada,$array1,$array2);
    }
    echo "<a href='index.php'>Vuelta al inicio</a>";
    if ($jornada == 30){
        $temporada = calculoTemporada();
        finalizarTemporada($temporada);
    }   
?>