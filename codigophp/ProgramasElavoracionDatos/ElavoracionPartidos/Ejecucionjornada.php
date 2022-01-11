<?php
    echo "Inicio Jornada";
    include('functionClub.php');
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
    $jornada=calculoJornada();
    planificacionjornadasParaliga($jornada,$array1,$array2);
    echo "<a href='index.php'>Vuelta al inicio</a>";
    
?>