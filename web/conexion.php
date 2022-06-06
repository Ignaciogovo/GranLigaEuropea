<?php
function conexion(){
        $conexion=mysqli_connect("host","user","contraseña","liga",3306);
    // Comprobamos la conexión
    if (!$conexion) {
        die("La conexión ha fallado: " . mysqli_connect_error());
    };
    return $conexion;
}


?>