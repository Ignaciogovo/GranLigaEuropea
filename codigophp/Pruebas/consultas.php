<?php
    include("../ProgramasElavoracionDatos/ElavoracionPartidos/functionJugadores.php");

   $club = 2;
   $jugadores=obtencionjugadores($club); //Obtenemos los judadores
   $jugadores=asignacionesprobabilidades($jugadores); //Se le asignan probabilidades.
   $jugadores=asignacionTitular($jugadores); // Asignación de titular.
   echo "antes goles: ";
   print_r($jugadores[0]);
   echo "<br>";
   echo "<br>";
   $jugadores=asignargol($jugadores,4); // Aginación de goles.
   echo "Pos goles:<br>";
   echo "<br>";
   echo "<br>";
   echo "<br>";
   print_r($jugadores[0]);
   echo "<br>";
   echo "<br>";
   echo "<br>";   
   echo "<br>";
   print_r($jugadores[1]);
   echo "<br>";
   echo "<br>";
   print_r($jugadores[3]);
   echo "<br>";
   echo "<br>";
   echo "<br>";
   $jugadores=ordenarasignacion($jugadores,12);
   print_r($jugadores);
   echo "<br>";
   echo "<br>";
   echo "<br>";
   $jugadores=ordenarasignacion($jugadores,6);
   print_r($jugadores);
?>