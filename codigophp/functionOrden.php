<?php
    function desplazamiento(){ // Desplazamiento de dos arrays. el ultimo valor del primer array pasa a ser ultimo del segundo y el primer valor del segundo array pasa a ser primero del primer array
        global $array1; 
        global $array2;
        $last = array_pop($array1);
        $first = array_shift($array2);
            array_unshift($array1, $first);
            array_push($array2,$last);
    }
    function planificacionjornadas($participantes,$mitad,$array1,$array2){
        $tiempo = 1;
        while ($tiempo <=$participantes){ //Bucle para el número de jornadas siendo el número de jornadas igual al número de participantes.
            echo " Jornada $tiempo <br>";
            if ($tiempo == $mitad+1){
                echo " Comienzo de la mitad de la temporada<br>";
            }
            if ($mitad%2==0) {  // Si la mitad de la temporada fuera impar algunos equipos jugarian más partidos en casa que de visitante y viceversa.
                if ($tiempo%2==0){
                echo "<FONT SIZE=2>visitante vs Local</font>";
                echo "<br>";
            }else{
                echo "<FONT SIZE=2>Local vs visitante</font>";
                echo "<br>";
            }}
            $v2 = 0;
            echo 1 . " --vs-- " . $array2[$v2]; // Para que el equipo 1 siempre esté fijo, fuera del bucle de orden de los partidos.
            echo "<br>";
            while ( $v2 < $mitad-1){  //Bucle para orden de los partidos.
            echo $array1[$v2] . " --vs-- " . $array2[$v2+1];
            echo "<br>";
            $v2++;
        }
        echo "<br>";
        global $array1;
        global $array2;
        desplazamiento();
            $tiempo ++;
        }
    }
?>