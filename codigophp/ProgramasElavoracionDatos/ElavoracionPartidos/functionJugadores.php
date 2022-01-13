<?php
   function obtencionjugadores($club){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $consulta="select id,posicion, valor from jugadores where id_club = ? order by convert(int,valor) desc";//$consulta="select id, valor from jugadores where id_club = ? and posicion = ? order by convert(int,valor) desc";
    $jugadores=$conexion->prepare($consulta, [   //Obtener datos a partir de un cursor.
        PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL,
    ]);
    $jugadores->execute([$club]);
    //$delanteros->execute([$club,$posicion]);
    $v =$jugadores->fetchAll();
    return $v;
   }
   //Funciones necesarias para el partido

   //Ordena el array a partir de los valores dados.
   function ordenarasignacion($array,$key){   //Ordena De mayor a menor el valor de la key que se pida.
    for ($i=0; $i <count($array); $i++)
    {
     for($a=$i+1; $a<count($array);$a++)
     {
        $numero1 = $array[$a];
        $numero2 = $array[$i];
        if($numero1[$key]>$numero2[$key]){    //Se escoge la key 2 ya que es donde esta situado el valor asignado.
            $intermedio = $array[$a];
            $array[$a]= $array[$i];
            $array[$i]=$intermedio;
        }
     }
    }
    return($array);
   }
   //Indica el sistema de juego
   function Sistemasequipo(){
       $sistema = rand (0,3);
           switch ($sistema){
               case 0:
                    //sistema 4-4-2
                    $sistema = array(1,4,4,2);
                break;
                case 1:
                  //sistema 4-4-2   //se repite de nuevo el sistema 4-4-2 para darle mayor probabilidad al 4-4-2 ya que es el sistema más usado en el futbol.
                  $sistema = array(1,4,4,2);
                break;
                case 2:
                    //sistema 5-3-2
                    $sistema = array(1,5,3,2);
                break;
                case 3:
                    //sistema 4-3-3
                    $sistema = array(1,4,3,3);
                break;
           }
           return $sistema;
   }
   //Número de tarjetas que se jugara en el partido
   function tarjetas(){
       $amarillas = rand(0,4);
       $rojas = (rand(0,2)*rand(0,3))/2;
       if ($rojas < 1){
           $rojas = 0;
       }
       $tarjetas = array($amarillas,$rojas);
       return $tarjetas;

   }
   function asignacionesprobabilidades($array){
   for ($i=0; $i <count($array); $i++)
   {
    $ptitular = rand(0,10);
    $titular = 0;
    $pgol = rand (0,10);
    $gol = 0;
    $pamarilla = rand (0,10);
    $amarilla = 0;
    $proja = rand (0,10);
    $roja = 0;
    array_push($array[$i],$ptitular); //Key que asigna el potenicial de titularidad.    KEY 3
    array_push($array[$i],$titular); //Key que asigna el la titularidad.                KEY 4
    array_push($array[$i],$pgol); //Key que asigna el potenicial de gol.                KEY 5
    array_push($array[$i],$gol); //Key que asigna el numero de goles (Por ahora 0)      KEY 6
    array_push($array[$i],$pamarilla); //Key que asigna el potenicial de amarillas.     KEY 7
    array_push($array[$i],$amarilla);  //key que asigna el número de amarillas.         KEY 8
    array_push($array[$i],$proja); //Key que asigna el potenicial de roja.              KEY 9
    array_push($array[$i],$roja);  //key que asigna el número de goles del jugador.     KEY 10
   }
   return($array);
   } 
   function mejorapotencial($array,$opcion){ // se mejora el número asignado según su valor;
    //multiplicadores
    switch ($opcion){
        case 3:
            $multiplicador= array(20,30,30,30);
        break;
        case 5:
            $multiplicador= array(1,30,35,45);
        break;
        case 7:
            $multiplicador= array(1,10,5,5);
        break;
        case 9:
            $multiplicador= array(1,10,5,5);
        break;
    }
    for ($i=0; $i <count($array); $i++){
        $numero = $array[$i];
        //Portero
        if ($numero[1] == 'Portero'){
                $potenciador = $multiplicador[0]/10;
                if($potenciador <= 0){
                    $potenciador = 0.2;
                }
                $numero[$opcion]=$numero[$opcion]*$potenciador;
                $array[$i]= array_replace($array[$i],$numero);
                $multiplicador[0] = $multiplicador[0] -5;
            }
           //Defensas
        if ($numero[1] == 'Defensa'){
        $potenciador = $multiplicador[1]/10;
        if($potenciador <= 0){
            $potenciador = 0.2;
        }
        $numero[$opcion]=$numero[$opcion]*$potenciador;
        $array[$i]= array_replace($array[$i],$numero);
        $multiplicador[1] = $multiplicador[1] -5;
        }
        //Centrocampistas
        if ($numero[1] == 'Centrocampista'){
            $potenciador = $multiplicador[2]/10;
            if($potenciador <= 0){
                $potenciador = 0.2;
            }
            $numero[$opcion]=$numero[$opcion]*$potenciador;
            $array[$i]= array_replace($array[$i],$numero);
            $multiplicador[2] = $multiplicador[2] -5;
        }
        //Delanteros
        if ($numero[1] == 'Delantero'){
            $potenciador = $multiplicador[3]/10;
            if($potenciador <= 0){
                $potenciador = 0.2;
            }
            $numero[$opcion]=$numero[$opcion]*$potenciador;
            $array[$i]= array_replace($array[$i],$numero);
            $multiplicador[3] = $multiplicador[3] -5;
        }

        }
        $array=ordenarasignacion($array,$opcion);
        return($array);
    }


//Asignación de estadisticas




    //Asignación de titulares.
    function asignacionTitular($array){
        $array=mejorapotencial($array,3);
        $sistema=Sistemasequipo();
        for ($i=0; $i <count($array); $i++){
            $numero = $array[$i];
            //Portero
            if ($numero[1] == 'Portero'){
               if ($sistema[0]>0){
                    $numero[4]=1;
                    $array[$i]= array_replace($array[$i],$numero);
                    $sistema[0] = $sistema[0]-1;
                }
                }
               //Defensas
            if ($numero[1] == 'Defensa'){
                if ($sistema[1]>0){
                    $numero[4]=1;
                    $array[$i]= array_replace($array[$i],$numero);
                    $sistema[1] = $sistema[1]-1;
                }
            }
            //Centrocampistas
            if ($numero[1] == 'Centrocampista'){
                if ($sistema[2]>0){
                    $numero[4]=1;
                    $array[$i]= array_replace($array[$i],$numero);
                    $sistema[2] = $sistema[2]-1;

                }
            }
            //Delanteros
            if ($numero[1] == 'Delantero'){
                if($sistema[3]>0){
                    $numero[4]=1;
                    $array[$i]= array_replace($array[$i],$numero);
                    $sistema[3] = $sistema[3]-1;
                }
            }
        }
        return $array;
    }
   // Asignación de goles 
   function asignargol($array,$goles){
        $array=mejorapotencial($array,5);
        for ($i=0; $i <$goles; $i++)
        {
        $numero = $array[0];
        $numero[6]=$numero[6]+1;  //El valor del key 6(Numero de goles) aumenta segun el valor del potencial del key 5
        $numero[5]=$numero[5]-3;    //Cada vez que se le asigna un gol, el valor del potencial del key 5 disminuye (-3).
        $array[0]= array_replace($array[0],$numero);
        $array=ordenarasignacion($array,5);
        }
        return $array;
    }
    //Asignación de tarjetas.
    function asignarTarjetas($array){
        $tarjetas = tarjetas();
        $array = mejorapotencial($array,7);
        for ($i=0; $i <$tarjetas[0]; $i++)
        {
        $numero = $array[0];
        $numero[8]=$numero[8]+1;  //El valor del key 8(tarjetas amarilla) aumenta segun el valor del potencial del key 7
        $numero[7]=$numero[7]-5;    //Cada vez que se le asigna una tarjeta, el valor del potencial del key 7 disminuye (-3).
        $array[0]= array_replace($array[0],$numero);
        $array=ordenarasignacion($array,7);
        } 
        $array = mejorapotencial($array,9);
        for ($i=0; $i <$tarjetas[1]; $i++)
        {
        $numero = $array[0];
        if ($numero[8]<2 and $numero[10]<1){
            $numero[10]=$numero[10]+1;  //El valor del key 10(tarjetas roja) aumenta segun el valor del potencial del key 9
            $numero[9]=$numero[9]-5;    //Cada vez que se le asigna una tarjeta, el valor del potencial del key 9 disminuye (-3).
            $array[0]= array_replace($array[0],$numero);
            $array=ordenarasignacion($array,9);
        }else{
            $numero = $array[1];
            if ($numero[8]<2 and $numero[10]<2){
                $numero[10]=$numero[10]+1;  //El valor del key 10(tarjetas roja) aumenta segun el valor del potencial del key 9
                $numero[9]=$numero[9]-5;    //Cada vez que se le asigna una tarjeta, el valor del potencial del key 9 disminuye (-3).
                $array[1]= array_replace($array[1],$numero);
                $array=ordenarasignacion($array,9);
            }
        }
        
        }
        return($array);
        
    }
    //Funcion de prueba para centralizar la asingacion de estadisticas.
    function asignacionestadisticas($array,$limite,$potencial,$valor){
        for ($i=0; $i <$limite; $i++)
        {
        $numero = $array[0];
        $numero[$valor]=$numero[$valor]+1;  //El valor del key 10(tarjetas roja) aumenta segun el valor del potencial del key 9
        echo "<br>";
        echo $numero[$potencial];
        $numero[$potencial]=$numero[$potencial]-3;    //Cada vez que se le asigna una tarjeta, el valor del potencial del key 9 disminuye (-3).
        $array[0]= array_replace($array[0],$numero);
        $array=ordenarasignacion($array,$potencial);
        }
    }

//Funcion para la elavoración de datos
    function elavoracionDatosjugadores($id,$id_partido,$goles,$amarillas,$roja,$titular){
        include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
        $sentencia = $conexion->prepare("INSERT INTO prueba_Estadisticas_partido(id_jugador,id_partido,goles,amarillas,roja,titularidad) VALUES (?, ?, ?, ?, ?, ?);");
        $resultado = $sentencia->execute([$id,$id_partido,$goles,$amarillas,$roja,$titular]);
    }

// Ejecuta todas las funciones para asignacion de datos a los jugadores.
function EjecutarEstadisticas($club,$goles,$id_partido){
    $array=obtencionjugadores($club);
    $array=asignacionesprobabilidades($array);
    $array=asignacionTitular($array);
    $array=asignargol($array,$goles);
    $array=asignarTarjetas($array);
    for ($i=0; $i <count($array); $i++){
        $numero = $array[$i];
        $id_jugador = $numero[0];
        $titular = $numero[4];
        $gol = $numero[6];
        $amarillas = $numero[8];
        $roja = $numero[10];
        elavoracionDatosjugadores($id_jugador,$id_partido,$gol,$amarillas,$roja,$titular);
        }
}






///Pruebas
// //    $club = 2;
// //    $jugadores=EjecutarEstadisticas($club,4,1020);
//    echo "<br>";
//    echo "<br>";
//    echo "<br>";
//    echo "<br>";
//    //print_r($jugadores);
//    echo "<br>";
//    echo "<br>";
//    for ($i=0; $i <count($jugadores); $i++){
//     $numero = $jugadores[$i];
//     if ($numero[1] == 'Defensa'){
//         echo " id jugador: " . $numero [0] . " Posicion: " . $numero[1] . " valor: " . $numero[2] . " potencial titular: " . $numero[3] . " titular: " . $numero[4] . " Numero de goles: " . $numero[6] . " potencial amarilla: " . $numero[7] ." tarjetas amarillas: " . $numero[8] . " potencial roja: " . $numero[9] . " tarjetas rojas: " . $numero[10];
//         echo "<br>";
//     }
//    }
//    echo "<br>";
//    echo "<br>";
//    for ($i=0; $i <count($jugadores); $i++){
//     $numero = $jugadores[$i];
//     if ($numero[1] == 'Centrocampista'){
//         echo " id jugador: " . $numero [0] . " Posicion: " . $numero[1] . " valor: " . $numero[2] . " potencial titular: " . $numero[3] . " titular: " . $numero[4] . " Numero de goles: " . $numero[6] . " tarjetas amarillas: " . $numero[8] . " tarjetas rojas: " . $numero[10];
//         echo "<br>";
//     }
//    }
//    echo "<br>";
//    echo "<br>";
//    for ($i=0; $i <count($jugadores); $i++){
//     $numero = $jugadores[$i];
//     if ($numero[1] == 'Delantero'){
//         echo " id jugador: " . $numero [0] . " Posicion: " . $numero[1] . " valor: " . $numero[2] . " potencial titular: " . $numero[3] . " titular: " . $numero[4] . " Numero de goles: " . $numero[6] . " tarjetas amarillas: " . $numero[8] . " tarjetas rojas: " . $numero[10];
//         echo "<br>";
//     }
//    }
?>