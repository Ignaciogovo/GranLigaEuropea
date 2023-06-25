import re
from datetime import datetime



def replace_ignore_case(texto,viejo,nuevo):
    # Compilar un objeto de patrón de expresión regular
    # utilizando el texto viejo escapado y con coincidencia insensible a mayúsculas y minúsculas --> Escapado que no afecta a las expresiones irregulares
    patron=re.compile((re.escape(viejo)), re.IGNORECASE)
    texto_final=patron.sub(nuevo,texto)
    return(texto_final)






def configurar_fecha(fecha):
    try:
        fecha_dt = datetime.strptime(fecha, '%d.%m.%Y').date()
    except:
        return fecha  
    fecha_mysql = fecha_dt.strftime('%Y-%m-%d')
    return(fecha_mysql)






#Eliminar palabras repetidas
# Obtenido desde: https://foroayuda.es/como-eliminar-palabras-duplicadas-de-la-cadena-en-el-ejemplo-de-codigo-de-python/
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist






# Convertir datos de una lista en str:
def convertir_a_str(lista):
    return [str(elemento) for elemento in lista]





