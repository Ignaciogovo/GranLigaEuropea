<?php 
function calculovalor($E){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
        $consulta="select (convert(int,ValorTotal)/nJugadores) as valorm from club where id=?";
        $valormedio=$conexion->prepare($consulta, [   //Obtener datos a partir de un cursor.
            PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL,
        ]);
        $valormedio->execute([$E]);
        $v =$valormedio->fetchObject();
        $v =$v->valorm;
        return $v;
 
        
    }
function calculoJornada(){
    error_reporting(0); //para desactivar los errores
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->query("select jornada from prueba_partidos order by id desc");
    $jornadas = $sentencia->fetchAll(PDO::FETCH_OBJ);
    $jornada = $jornadas[0]->jornada;   //Obtencion de la jornada a partir de un array de objetos¿?
    if(empty($jornada)){
        $jornada=0;
    }
    $jornada++;
    return $jornada;
}
function calculoTemporada(){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->query("select temporada from prueba_partidos order by id desc");
    $temporadas = $sentencia->fetchAll(PDO::FETCH_OBJ);
    $temporada = $temporadas[0]->temporada;   //Obtencion de la temporada a partir de un array de objetos¿?
        if(empty($temporada)){
            $temporada=1;
            
        }

    return $temporada;
      
}
function creacionTemporada($temporada){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->prepare("INSERT INTO prueba_temporadas(id, Fecha_inicio) VALUES (?, ?);");
    $fecha_inicio = date("Y-m-d H:i:s"); //Formato DATETIME de sql.
    $resultado = $sentencia->execute([$temporada, $fecha_inicio]);

}
function partidosinempates($E1,$E2,$jornada){
    $V1=calculovalor($E1);
    $V2=calculovalor($E2);
    $diferencia=$V2-$V1;
    $diferencia = abs($diferencia);
    $final = 0;
    while($final < 1){
        //Elavoración del número aleatorio, tendrán ventaja si el valor es mayor.
        if ( $V1 < $V2 ){  
            if($diferencia < 100000){
                $potencial2= 1.15*rand(0,8);
                $potencial1= rand(0,8);
                //echo " Se produce la diferencia x1.15 ";
            }elseif ($diferencia >= 100000 AND $diferencia < 500000) {
                $potencial2= 1.25* rand(0,8);
                $potencial1= rand(0,8);
                //echo " Se produce la diferencia x1.25 ";
            }elseif ($diferencia >= 500000 AND $diferencia <=1000000) {
                $potencial2= 1.5*rand(0,8);
                $potencial1= rand(0,8);
                //echo " Se produce la diferencia x1.5 ";
            }elseif ($diferencia >=1000000){
                $potencial2= 1.8* rand(0,8);
                $potencial1= rand(0,8);
                //echo " Se produce la diferencia x1.8 limitado";
            }               
        }elseif( $V1 > $V2){
            if($diferencia < 100000){
                $potencial1= 1.25* rand(0,8);
                $potencial2= rand(0,8);
                //echo " Se produce la diferencia x1.15 ";
            }elseif ($diferencia >= 100000 AND $diferencia <500000) {
                $potencial1= 1.25* rand(0,8);
                $potencial2= rand(0,8);
                //echo " Se produce la diferencia x1.25 ";
            }
            elseif ($diferencia >= 500000 AND $diferencia <=1000000) {
                $potencial1= 1.5* rand(0,8);
                $potencial2= rand(0,8);
                //echo " Se produce la diferencia x1.5 ";
            }elseif ($diferencia >=1000000){
                $potencial1= 1.8* rand(0,8);
                $potencial2= rand(0,8);
                //echo " Se produce la diferencia x1.8";
            }           
        }elseif($V1 == $V2){
            $potencial2= rand(0,8);
            $potencial1= rand(0,8);
        };
        //Ventaja Local
        if($jornada%2==0){
            $potencial2=$potencial2*1.15;
            //echo " local el de la derecha";
        }else{
            $potencial1=$potencial1*1.15;
            //echo " local el de la izquierda";


        }
        //Asignación del equipo ganador
        if ($potencial1 < $potencial2){
            $gol1=($potencial1/2.5);
            $gol2=($potencial2/2.5);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($gol1==$gol2){
                $gol2++;
            }
            if($jornada%2==0){
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada);
            
                //echo " local el de la derecha";
            }else{
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada);
                //echo " local el de la izquierda";
            }
            echo " Gana Equipo $E2 con un $potencial2  con goles: $gol2<br>";
            echo " Pierde Equipo $E1 con un $potencial1 con goles: $gol1<br>";
            $final = 1;
        }elseif ($potencial1 > $potencial2){
            $gol1=($potencial1/2.5);
            $gol2=($potencial2/2.5);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($gol1==$gol2){
                $gol1++;
            }
            if($jornada%2==0){
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada);
            
                //echo " local el de la derecha";
            }else{
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada);
                //echo " local el de la izquierda";
            }
            echo " Gana Equipo $E1 con un $potencial1 con goles: $gol1<br>";
            echo " Pierde Equipo $E2 con un $potencial2 con goles: $gol2<br>";
            $final = 1;
        }
    }
}
function partido($E1,$E2,$jornada){
    $V1=calculovalor($E1);
    $V2=calculovalor($E2);
    $diferencia=$V2-$V1;
    $diferencia = abs($diferencia); //Valor absoluto.
        //Elavoración del número aleatorio, tendrán ventaja si el valor es mayor.
        if ( $V1 < $V2 ){  
            if($diferencia < 150000){
                $potencial2= rand(0,8);
                $potencial1= rand(0,8);
                $aforo= rand(70,100);
                //echo " Se produce la diferencia x1.15 ";
            }elseif ($diferencia >= 150000 AND $diferencia < 500000) {
                $potencial2= 1.25* rand(0,8);
                $potencial1= rand(0,8);
                $aforo = rand(60,95);
                //echo " Se produce la diferencia x1.25 ";
            }elseif ($diferencia >= 500000 AND $diferencia <=1000000) {
                $potencial2= 1.5*rand(0,8);
                $potencial1= rand(0,8);
                $aforo = rand(60,90);
                //echo " Se produce la diferencia x1.5 ";
            }elseif ($diferencia >=1000000){
                $potencial2= 1.75* rand(0,8);
                $potencial1= rand(0,8);
                $aforo = rand(65,100);
                //echo " Se produce la diferencia x1.75";
            }               
        }elseif( $V1 > $V2){
            if($diferencia < 150000){
                $potencial1= rand(0,8);
                $potencial2= rand(0,8);
                $aforo= rand(70,100);
                //echo " Se produce la diferencia x1.15 ";
            }elseif ($diferencia >= 150000 AND $diferencia <500000) {
                $potencial1= 1.25* rand(0,8);
                $potencial2= rand(0,8);
                $aforo = rand(60,95);
                //echo " Se produce la diferencia x1.25 ";
            }
            elseif ($diferencia >= 500000 AND $diferencia <=1000000) {
                $potencial1= 1.5* rand(0,8);
                $potencial2= rand(0,8);
                $aforo = rand(60,90);
                //echo " Se produce la diferencia x1.5 ";
            }elseif ($diferencia >=1000000){
                $potencial1= 1.75* rand(0,8);
                $potencial2= rand(0,8);
                $aforo = rand(65,100);
                //echo " Se produce la diferencia x1.75";
            }           
        }elseif($V1 == $V2){
            $potencial2= rand(0,8);
            $potencial1= rand(0,8);
            $aforo = rand(70,100);
        };
        //Ventaja Local
        if ($aforo > 80){
            if($jornada%2==0){
                $potencial2=$potencial2*1.15;
                //echo " local el de la derecha";
            }else{
                $potencial1=$potencial1*1.15;
                //echo " local el de la izquierda";
            }
        }
        //convirtiendo la variable aforo en varchar
        $aforo = "$aforo%";
        //Asignación del equipo ganador
        if ($potencial1 < $potencial2){
            $gol1=($potencial1/2.5);
            $gol2=($potencial2/2.5);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($gol1==$gol2){
                $gol2++;
            }
            if($jornada%2==0){
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada,$aforo);
            
            }else{
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada,$aforo);
            }
            echo " Gana Equipo $E2 con un $potencial2  con goles: $gol2<br>";
            echo " Pierde Equipo $E1 con un $potencial1 con goles: $gol1<br>";
        }elseif ($potencial1 > $potencial2){
            $gol1=($potencial1/2.5);
            $gol2=($potencial2/2.5);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($gol1==$gol2){
                $gol1++;
            }
            if($jornada%2==0){
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada,$aforo);
            
                //echo " local el de la derecha";
            }else{
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada,$aforo);
                //echo " local el de la izquierda";
            }
            echo " Gana Equipo $E1 con un $potencial1 con goles: $gol1<br>";
            echo " Pierde Equipo $E2 con un $potencial2 con goles: $gol2<br>";
        }elseif($potencial1=$potencial2){
            $gol1=($potencial1/2.5);
            $gol2=($potencial2/2.5);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($jornada%2==0){
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada,$aforo);
            
                //echo " local el de la derecha";
            }else{
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada,$aforo);
                //echo " local el de la izquierda";
            }
            echo "Se produce un empate";
        }
        echo "se produce un aforo de: $aforo";
    
}
function elavoracionDatospartido($id_local,$id_visitante,$goles_local,$goles_visitante,$jornada,$aforo){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->prepare("INSERT INTO prueba_partidos(id_local,id_visitante,goles_local,goles_visitante,id_arbitro,aforo,jornada,temporada) VALUES (?, ?, ?, ?, ?, ?, ?, ?);");
    $id_arbitro = rand(1,15);
    $temporada = calculoTemporada();
    $resultado = $sentencia->execute([$id_local,$id_visitante,$goles_local,$goles_visitante,$id_arbitro,$aforo,$jornada,$temporada]);
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
    while ($tiempo <$jornada){ //Bucle para escoger la jornada. Cuando la variable $tiempo sea igual a la variable $jornada termina bucle con los equipos.
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
        partido(1,$array2[$v2],$jornada);
        echo "<br>";
        while ( $v2 < 7){  //Bucle para orden de los partidos.
        echo $array1[$v2] . " --vs-- " . $array2[$v2+1];
        partido($array1[$v2],$array2[$v2+1],$jornada);
        echo "<br>";
        $v2++;
    }
}

    ?>