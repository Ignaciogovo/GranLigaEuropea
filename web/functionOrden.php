<?php
    function desplazamiento($array1,$array2){ // Desplazamiento de dos arrays. el ultimo valor del primer array pasa a ser ultimo del segundo y el primer valor del segundo array pasa a ser primero del primer array
        $last = array_pop($array1);
        $first = array_shift($array2);
        array_unshift($array1, $first);
        array_push($array2,$last);
        $arrays = [$array1,$array2];
        return($arrays);
    }
    function planificacionjornadas($participantes,$mitad,$array1,$array2,$jornada){
        include_once('C:\xampp\htdocs\ProyectoLiga\ConexionRemota\web\funciones.php');
        $jornadaBDD = selectJornada();
        $tiempo = 1;
        if ($jornada >1){
            while ($tiempo <=$jornada){ //Bucle para el número de jornadas siendo el número de jornadas igual al número de participantes.
                $arrays=desplazamiento($array1,$array2);
                $array1 = $arrays[0];
                $array2 = $arrays[1];
                    $tiempo ++;
                }

        }
        if ($mitad%2==0) {  // Si la mitad de la temporada fuera impar algunos equipos jugarian más partidos en casa que de visitante y viceversa.
            if ($tiempo%2==0){
            echo "<h4>Jornada ".$jornada."</h4>";
            echo "<br>";
            echo "<h5>visitante vs Local</h5>";
            echo "<br>";
            $v2 = 0;
                if ($jornada <= $jornadaBDD){
                    // Para que el equipo 1 siempre esté fijo, fuera del bucle de orden de los partidos.
                    sacarResultados($array2[$v2],1);
                    while ( $v2 < $mitad-1){  //Bucle para orden de los partidos.
                        $local = $array2[$v2+1];
                        $visitante = $array1[$v2];
                        sacarResultados($local,$visitante);
                        $v2++;
                    }
                }else{
                    // Para que el equipo 1 siempre esté fijo, fuera del bucle de orden de los partidos.
                    sacarClubs($array2[$v2],1);
                    while ( $v2 < $mitad-1){  //Bucle para orden de los partidos.
                        $local = $array2[$v2+1];
                        $visitante = $array1[$v2];
                        sacarClubs($local,$visitante);
                        $v2++;
                    }
                }


        }else{
            echo "<h4>Jornada ".$jornada."</h4>";
            echo "<br>";
            echo "<h5>Local vs visitante</h5>";
            echo "<br>";
            $v2 = 0;
            if ($jornada <= $jornadaBDD){
                // Para que el equipo 1 siempre esté fijo, fuera del bucle de orden de los partidos.
                sacarResultados(1,$array2[$v2]);
                while ( $v2 < $mitad-1){  //Bucle para orden de los partidos.
                    $local = $array1[$v2];
                    $visitante = $array2[$v2+1];
                    sacarResultados($local,$visitante);
                    $v2++;
                }
            }else{
                // Para que el equipo 1 siempre esté fijo, fuera del bucle de orden de los partidos.
                sacarClubs(1,$array2[$v2]);
                while ( $v2 < $mitad-1){  //Bucle para orden de los partidos.
                    $local = $array1[$v2];
                    $visitante = $array2[$v2+1];
                    sacarClubs($local,$visitante);
                    $v2++;
                }
            }
        }
        }

    }
    function sacarResultados($local,$visitante){
        include_once('C:\xampp\htdocs\ProyectoLiga\ConexionRemota\web\funciones.php');
        print($local);
        $goles = selectgoles($local,$visitante);
        $local =  SelectNombreClub($local);
        $visitante = SelectNombreClub($visitante);
        echo $local . " ".$goles[0]." --vs-- ".$goles[1]." ". $visitante;
        echo "<br>";
    }
    function sacarClubs($local,$visitante){
        include_once('C:\xampp\htdocs\ProyectoLiga\ConexionRemota\web\funciones.php');
        $local =  SelectNombreClub($local);
        $visitante = SelectNombreClub($visitante);
        echo $local . " --vs-- ". $visitante;
        echo "<br>";
    }

    function intermedio($jornada){
        $participantes = 20;
        $i=0;
        $primeros=$participantes/2;
        $equipos1= array(2);
        $v1=3;
        while ($v1<=$primeros){    // Ampliación equipos1
            array_push($equipos1,$v1);
            $v1++;
        }
        $equipos2= array($primeros+1);
        $v1=$primeros+2;
        while ($v1<=$participantes){ //Ampliación equipos2
            array_push($equipos2,$v1);
            $v1++;
        }
        planificacionjornadas($participantes,$primeros,$equipos1,$equipos2,$jornada);
    }

?>