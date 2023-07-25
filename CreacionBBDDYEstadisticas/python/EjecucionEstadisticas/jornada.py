# importing the sys module
import sys 
import os
import os
from dotenv import load_dotenv



# Obtén la ruta del directorio padre
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agrega el directorio padre al sys.path
sys.path.append(parent_dir)
import conexionsql as cs
import conexiontwitter as ct
import CreadorJornadas as cj
from time import sleep
from datetime import datetime

# Concatena el nombre del archivo .env al final de la ruta
env_path = os.path.join(parent_dir , '.env')
load_dotenv(env_path)
# Carga las variables de entorno desde el archivo .env
control_backup=os.getenv('CONTROL_BACKUP')
ruta_backup=os.getenv('RUTA_BACKUP')





def finalizarTemporada():
    # Finalizamos temporada
    cs.finalizarTemporada()
    # desactivamos a los jugadores y club
    cs.AnularActivoJugadores()
    cs.AnularActivoClub()

#fecha actual
jornada = cs.selectJornada()
if jornada > 0:
    if jornada > 38:
        print("La temporada ha terminado, debes iniciar una temporada")
    else:
        temporada = cs.selectTemporada()
        if jornada == 1:
            print("Comienzo de la temporada", temporada)
            cs.actualizar_fecha_temporada()
            # Creamos el calendario y las jornadas
            cj.generar_calendario(temporada)
        print("Comienzo de jornada: ",jornada)
        now = datetime.now()
        print(now)
        # ct.twittearJornada(jornada)
        sleep(2)
        cj.partidos_jornada(jornada)
        print("Finalización de jornada", jornada)
        try:
            cs.insert_clasificacion_jornada(jornada,temporada)
        except:
            print("No se ha podido actualizar clasificación jornada")
        if jornada == 38:
            print("Finalización de temporada")
            finalizarTemporada()
            ct.twittearFinal()
        if control_backup == 'S':
        # Escritura del nombre de la copia de seguridad para la ejecución del comando en bash
            newdata="LJ"+str(jornada)+"T"+str(temporada)+".sql"
            with open(ruta_backup, "w") as myfile:
                myfile.write(newdata)
else:
    print("Lo siento, la temporada aún no ha empezado")
    
now = datetime.now()
print(now)