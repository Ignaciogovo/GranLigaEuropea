# importing the sys module
import sys
# in the sys.path list
sys.path.append('.\\')        
import conexiontwitter as ct
from conexionsql import selectJornadaSinSuma

# Con este archivo twitteamos que la página web esta actualiazada.
jornada = selectJornadaSinSuma()
ct.twittearPaginaweb(jornada)
print("Twitteado Jornada:", jornada)