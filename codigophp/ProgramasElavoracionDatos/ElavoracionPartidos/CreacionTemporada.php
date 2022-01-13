<?php
    include('functionClub.php');
    $jornada=calculoJornada();
    if ($jornada < 31){
        echo "Debe terminar la temporada";
    }else{
        echo "Generandose la temporada número: ";
    }
    echo "<a href='index.php'>Vuelta al inicio</a>";   
?>