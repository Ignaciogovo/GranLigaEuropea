<?php
    
    //Delanteros
   function obtencionDelanteros($club){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $consulta="select id, valor from jugadores where id_club = ? and posicion = 'Delantero' order by convert(int,valor) desc";
    $delanteros=$conexion->prepare($consulta, [   //Obtener datos a partir de un cursor.
        PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL,
    ]);
    $delanteros->execute([$club]);
    $v =$delanteros->fetchAll();;
    return $v;
   }
   function ordenarasignacion($array){   //Ordena el valor asignado a cada jugador
    for ($i=0; $i <count($array); $i++)
    {
     for($a=$i+1; $a<count($array);$a++)
     {
        $numero1 = $array[$a];
        $numero2 = $array[$i];
        if($numero1[2]>$numero2[2]){
            $intermedio = $array[$a];
            $array[$a]= $array[$i];
            $array[$i]=$intermedio;
        }
     }
    }
    return($array);
   }
   function mejorasignacion(){ // se mejora el número asignado según su valor;

   }
   $delanteros=obtencionDelanteros(2);
   for ($i=0; $i <count($delanteros); $i++)
   {
    $numero = rand(0,10);
    array_push($delanteros[$i],$numero);
   }
   $delanteros = ordenarasignacion($delanteros);
   print_r($delanteros);
   echo "<br>";
   for ($i=0; $i <count($delanteros); $i++)
   {
    $prueba=$delanteros[$i]; 
    echo $prueba[2];
    echo "<br>";
   }
   obtencionDelanteros(3);
    //Centrocampistas
    //Defensas
    
?>