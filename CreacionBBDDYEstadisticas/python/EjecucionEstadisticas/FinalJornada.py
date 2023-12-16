import sys 
import os
# Obtén la ruta del directorio padre
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agrega el directorio padre al sys.path
sys.path.append(parent_dir)
     
import conexiontwitter as ct
from conexionsql import selectJornadaSinSuma

# Con este archivo twitteamos que la página web esta actualiazada.
jornada = selectJornadaSinSuma()
if jornada > 0:
    if jornada > 38:
        print("Temporada terminada")
    else:
        ct.twittearPaginaweb(jornada)
        print("Twitteado Jornada:", jornada)