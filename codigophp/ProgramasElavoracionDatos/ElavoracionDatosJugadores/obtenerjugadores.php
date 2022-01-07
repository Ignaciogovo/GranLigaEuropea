<?php
   function obtencionjugadores($club,$posicion){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $consulta="select id, valor from jugadores where id_club = ? and posicion = ? order by convert(int,valor) desc";
    $delanteros=$conexion->prepare($consulta, [   //Obtener datos a partir de un cursor.
        PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL,
    ]);
    $delanteros->execute([$club,$posicion]);
    $v =$delanteros->fetchAll();;
    return $v;
   }
   function asignacionNumeroaleatorio($array){
   for ($i=0; $i <count($array); $i++)
   {
    $numero = rand(0,10);
    $gol = 0;
    echo "<br>" . $numero;
    array_push($array[$i],$numero); //Key que asigna el potenicial de estadisticas.
    array_push($array[$i],$gol);  //key que asigna el número de goles del jugador.
   }
   $array=mejorasignacion($array);
   return($array);
   }
   function ordenarasignacion($array){   //Ordena el valor asignado a cada jugador
    for ($i=0; $i <count($array); $i++)
    {
     for($a=$i+1; $a<count($array);$a++)
     {
        $numero1 = $array[$a];
        $numero2 = $array[$i];
        if($numero1[2]>$numero2[2]){    //Se escoge la key 2 ya que es donde esta situado el valor asignado.
            $intermedio = $array[$a];
            $array[$a]= $array[$i];
            $array[$i]=$intermedio;
        }
     }
    }
    return($array);
   }
   function mejorasignacion($array){ // se mejora el número asignado según su valor;
    $a = 35;  //Número 40 para cada vez que se divida entre 10 el potenciador sea entre 2 y 0.
    for ($i=0; $i <count($array); $i++)
    {
        $potenciador = $a/10;
        if($potenciador <= 0){
            $potenciador = 0.2;
        }
        $numero = $array[$i];
        $numero[2]=$numero[2]*$potenciador;
        echo "<br> potenciador =" . $potenciador . " numero total = " . $numero[2];      
        $array[$i]= array_replace($array[$i],$numero);
        $a = $a -5;
    }
    $array=ordenarasignacion($array);
    return($array);
   }
   // Asignación de goles 
   function asignargol($array,$goles){
    $gol=1;
    for ($i=0; $i <$goles; $i++)
    {
     $numero = $array[0];
     $numero[3]=$numero[3]+1;  //El valor del key 3 aumenta segun el valor del potencial del key 2
     echo "<br>";
     echo $numero[2];
     $numero[2]=$numero[2]-3;    //Cada vez que se le asigna un gol, el valor del potencial del key 2 disminuye (-3).
     $array[0]= array_replace($array[0],$numero);
     $array=ordenarasignacion($array);
    }
    return $array;
}
   $club = 2;
   $posicion = 'Defensa';
   $defensas=obtencionjugadores($club,$posicion);
   $defensas=asignacionNumeroaleatorio($defensas);
   print_r($defensas);
   $defensas = asignargol($defensas, 5);
   echo "<br>";
   echo "<br>";
   print_r($defensas);
   for ($i=0; $i <count($defensas); $i++){
    $numero = $defensas[$i];
    echo "numero asignado " . $numero[2] . " goles : " . $numero[3];
    echo "<br>";
   }
 
?>