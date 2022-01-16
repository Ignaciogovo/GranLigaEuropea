<?php
    //Este es un ejemplo de la conexion que se esta usando
    //Solamente hay que cambiar Los datos del new PDO (La ip, puerto, nombre de la base de datos y los datos de usuario)
         $conexion=new PDO("sqlsrv:server=IP, PUERTO;database=NombreBaseDatos", "usuario", "Contraseña");
         $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
?>