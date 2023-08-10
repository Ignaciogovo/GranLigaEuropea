<?php
include_once('funciones.php');
$calendario_array=select_calendario(1,2);
foreach ($calendario_array as $jornada) {
    echo "Jornada: " . $jornada['jornada'] . "<br>";
    echo "Local: " . $jornada['local'] . " (ID: " . $jornada['id_local'] . ")<br>";
    echo "Visitante: " . $jornada['visitante'] . " (ID: " . $jornada['id_visitante'] . ")<br>";
    echo "<br>";
}


?>