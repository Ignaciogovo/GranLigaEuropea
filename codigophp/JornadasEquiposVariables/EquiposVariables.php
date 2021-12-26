<?php
    $participantes=$_POST["participantes"];
    $primeros=$participantes/2;
    $array1= array(2);
    $v1=3;
    while ($v1<=$primeros){
        array_push($array1,$v1);
        $v1++;
    }
    $array2= array($primeros+1);
    $v1=$primeros+2;
    while ($v1<=$participantes){
        array_push($array2,$v1);
        $v1++;
    }
    $tiempo = 1;
    while ($tiempo <=$participantes){
        echo " Jornada $tiempo <br>";
        if ($tiempo == $primeros+1){
            echo " Comienzo de la mitad de la temporada<br>";
        }
        $v2 = 0;
        echo 1 . " vs " . $array2[$v2];
        echo "<br>";
        while ( $v2 < $primeros-1){ 
        echo $array1[$v2] . " vs " . $array2[$v2+1];
        echo "<br>";
        $v2++;
    }
    echo "<br>";
    $last = array_pop($array1);
    $first = array_shift($array2);
        array_unshift($array1, $first);
        array_push($array2,$last);
        //print_r($array1);
        echo "<br>";
        $tiempo ++;
    }
    echo "<a href='index.html'>Página inicial</a>";

?>