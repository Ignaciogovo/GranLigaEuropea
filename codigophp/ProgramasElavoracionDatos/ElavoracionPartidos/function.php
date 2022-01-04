<?php 
include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
function calculovalor($E){
    global $conexion;
        $consulta="select (convert(int,ValorTotal)/nJugadores) as valorm from club where id=?";
        $valormedio=$conexion->prepare($consulta, [   //Obtener datos a partir de un cursor.
            PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL,
        ]);
        $valormedio->execute([$E]);
        $v =$valormedio->fetchObject();
        $v =$v->valorm;
        return $v;
 
        
    }
function probabilidadVictoria($E1,$E2,$jornada){
    $v1=calculovalor($E1);
    $v2=calculovalor($E2);
    echo " $v1,$v2";
    $final = 0;
    while($final < 1){
        global $V1;
        global $V2;
        //Elavoración del número aleatorio, tendrán ventaja si el valor es mayor.
        if ( $V1 < $V2){        
            $diferencia=($V2-$V1);
            if($diferencia < 6){
                $potencial2= 1.25*rand(0,10);
                $potencial1= rand(0,10);
            }elseif ($diferencia >= 6) {
                $potencial2= 1.5*rand(0,10);
                $potencial1= rand(0,10);
            }            
        }elseif( $V1 > $V2){
            $diferencia = ($V1-$V2);
            if($diferencia < 6){
                $potencial1= 1.25* rand(0,10);
                $potencial2= rand(0,10);
            }elseif ($diferencia >= 6) {
                $potencial1= 1.5* rand(0,10);
                $potencial2= rand(0,10);
            }            
        }elseif($V1 ==$V2){
            $potencial2= rand(0,10);
            $potencial1= rand(0,10);
        };
        //Ventaja Local
        if($jornada%2==0){
            $potencial2=$potencial2*1.15;
            echo loca
        }else{
            $potencial1=$potencial1*1.15;

        }
        //Asignación del equipo ganador
        if ($potencial1 < $potencial2){
            $gol1=($potencial1/2.8);
            $gol2=($potencial2/2.8);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($gol1==$gol2){
                $gol2++;
            }
            echo "gana Equipo $E2 con un $potencial2  con goles: $gol2<br>";
            echo "pierde Equipo $E1 con un $potencial1 con goles: $gol1<br>";
            $final = 1;
        }elseif ($potencial1 > $potencial2){
            $gol1=($potencial1/2.8);
            $gol2=($potencial2/2.8);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($gol1==$gol2){
                $gol1++;
            }
            echo "gana Equipo $E1 con un $potencial1 con goles: $gol1<br>";
            echo "pierde Equipo $E2 con un $potencial2 con goles: $gol2<br>";
            $final = 1;
        }
    }
}
function desplazamiento(){ // Desplazamiento de dos arrays. el ultimo valor del primer array pasa a ser ultimo del segundo y el primer valor del segundo array pasa a ser primero del primer array
    global $array1; 
    global $array2;
    $last = array_pop($array1);
    $first = array_shift($array2);
        array_unshift($array1, $first);
        array_push($array2,$last);
}
function planificacionjornadasParaliga($jornada,$array1,$array2){
    $tiempo = 1;
    while ($tiempo <=$jornada){ //Bucle para el número de jornadas siendo el número de jornadas igual al número de participantes.
    global $array1;
    global $array2;
    desplazamiento();
        $tiempo ++;
    }
    echo " Jornada $jornada <br>";
        if ($jornada == 16){
            echo " Comienzo de la mitad de la temporada<br>";
        }
        if ($jornada%2==0){
            echo "<FONT SIZE=2>visitante vs Local</font>";
            echo "<br>";
        }else{
            echo "<FONT SIZE=2>Local vs visitante</font>";
            echo "<br>";
        }
        $v2 = 0;
        echo 1 . " --vs-- " . $array2[$v2]; // Para que el equipo 1 siempre esté fijo, fuera del bucle de orden de los partidos.
        probabilidadVictoria(1,$array2[$v2],$jornada);
        echo "<br>";
        while ( $v2 < 7){  //Bucle para orden de los partidos.
        echo $array1[$v2] . " --vs-- " . $array2[$v2+1];
        probabilidadVictoria($array1[$v2],$array2[$v2+1],$jornada);
        echo "<br>";
        $v2++;
    }
}

    ?>