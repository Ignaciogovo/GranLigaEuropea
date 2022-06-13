#!/bin/bash
# Hay que cambiar las rutas
#  Realizamos backup
archivo=$(cat jornadaTemporada.txt)
mysqldump --defaults-extra-file=/ruta/datos/autenticación  liga> /ruta/$archivo
cp /ruta/$archivo /ruta2/$archivo # Copiamos la copia de seguridad en otro disco

# Necesitamos tener una conexion ssh con otro servidor para el siguiente comando
#  introducimos la clave al agente ssh
eval `ssh-agent`
ssh-add /ruta/id_rsa
# copiamos el archivo creado y hacemos un restore en el otro servidor de escucha
scp /ruta/$archivo usuario@IP:/ruta/backup.sql
ssh usuario@IP "sudo mysql liga < /ruta/backup.sql"
