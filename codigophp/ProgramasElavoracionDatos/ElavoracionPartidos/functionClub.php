<?php
//FUNCIONES PARA SACAR DATOS DE LA BASE.
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
}function calculotablaTemporada(){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->query("select max(id) from prueba_temporadas");
    $temporadas = $sentencia->fetch();
    $temporada = $temporadas[0];   //Obtencion de la temporada a partir de un array de objetos¿?
        if(empty($temporada)){
            $temporada=0;
        }
    return $temporada;
}
function calculoPartido(){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->query("select id from prueba_partidos order by id desc");
    $datos = $sentencia->fetchAll(PDO::FETCH_OBJ);
    $id_partido = $datos[0]->id;   //Obtencion del id a partir de un array de objetos¿?
    return $id_partido;
}
//FUNCIONES PARA INTROUDCIR DATOS  EN LA BASE A PARTIR DE LO OBTENIDO.
function finalizarTemporada($temporada){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->prepare("update prueba_temporadas set fecha_final=? where id=?;");
    $fecha_final = date("Y-m-d H:i:s"); //Formato DATETIME de sql.
    $resultado = $sentencia->execute([$fecha_final,$temporada]);
}
function creacionTemporada($temporada){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->prepare("INSERT INTO prueba_temporadas(id, Fecha_inicio) VALUES (?, ?);");
    $fecha_inicio = date("Y-m-d H:i:s"); //Formato DATETIME de sql.
    $resultado = $sentencia->execute([$temporada, $fecha_inicio]);
}
function elavoracionDatospartido($id_local,$id_visitante,$goles_local,$goles_visitante,$jornada,$aforo){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->prepare("INSERT INTO prueba_partidos(id_local,id_visitante,goles_local,goles_visitante,id_arbitro,aforo,jornada,temporada) VALUES (?, ?, ?, ?, ?, ?, ?, ?);");
    $id_arbitro = rand(1,15);
    $temporada = calculotablaTemporada();
    $resultado = $sentencia->execute([$id_local,$id_visitante,$goles_local,$goles_visitante,$id_arbitro,$aforo,$jornada,$temporada]);
}
// FUNCIONES PARA EL DESPLAZAMIENTO DE LOS ARRAYS QUE ORGANIZAN LAS JORNADAS.
function desplazamiento(){ // Desplazamiento de dos arrays. el ultimo valor del primer array pasa a ser ultimo del segundo y el primer valor del segundo array pasa a ser primero del primer array
    global $array1; 
    global $array2;
    $last = array_pop($array1);
    $first = array_shift($array2);
        array_unshift($array1, $first);
        array_push($array2,$last);
}
//Conexión con funciones de jugadores
function jugadores($club,$goles){
    include_once('functionJugadores.php');
    $id_partido = calculoPartido();
    EjecutarEstadisticas($club,$goles,$id_partido);
}
//FUNCIONES PARA LA ELAVORACIÓN DEL PARTIDO


//Funcion en desuso
function partidosinempates($E1,$E2,$jornada){
    $V1=calculovalor($E1);
    $V2=calculovalor($E2);
    $diferencia=$V2-$V1;
    $diferencia = abs($diferencia);
    $final = 0;
    while($final < 1){
        //Elavoración del número aleatorio, tendrán ventaja si el valor es mayor.
        if ( $V1 < $V2 ){  
            if($diferencia < 150000){
                $potencial2= rand(0,8);
                $potencial1= rand(0,8);
                $aforo= rand(70,100);
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
            if($jornada%2==0){ //local el de la derecha
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada,$aforo);
            }else{ //local el de la izquierda
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada,$aforo);
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
            if($jornada%2==0){ //local el de la derecha
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada,$aforo);
                        }else{ //local el de la izquierda
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada,$aforo);
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
            if($jornada%2==0){ //local el de la derecha
                $potencial2=$potencial2*1.15;
            }else{ //local el de la izquierda
                $potencial1=$potencial1*1.15;
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
            if($jornada%2==0){ //local el de la derecha
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada,$aforo);
                jugadores($E1,$gol1);
                jugadores($E2,$gol2);
            
            }else{ //local el de la izquierda
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada,$aforo);
                jugadores($E1,$gol1);
                jugadores($E2,$gol2);
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
            if($jornada%2==0){ //local el de la derecha
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada,$aforo);
                jugadores($E1,$gol1);
                jugadores($E2,$gol2);
            }else{ //local el de la izquierda
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada,$aforo);
                jugadores($E1,$gol1);
                jugadores($E2,$gol2);
            }
            echo " Gana Equipo $E1 con un $potencial1 con goles: $gol1<br>";
            echo " Pierde Equipo $E2 con un $potencial2 con goles: $gol2<br>";
        }elseif($potencial1=$potencial2){
            $gol1=($potencial1/2.5);
            $gol2=($potencial2/2.5);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($jornada%2==0){ //local el de la derecha
                elavoracionDatospartido($E2,$E1,$gol2,$gol1,$jornada,$aforo);
                jugadores($E1,$gol1);
                jugadores($E2,$gol2);
            }else{ //local el de la izquierda
                elavoracionDatospartido($E1,$E2,$gol1,$gol2,$jornada,$aforo);
                jugadores($E1,$gol1);
                jugadores($E2,$gol2);
            }
            echo "Se produce un empate";
        }
        echo "se produce un aforo de: $aforo";
    
}
 //Funcion que ejecuta cada partido y organiza la jornada.
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