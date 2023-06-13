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
