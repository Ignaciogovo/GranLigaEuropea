# Gran Liga Europea
Idea: Crear un simulador de una liga inventada con los mejores equipos de fútbol de europa al estilo "la superliga de florentino" con equipos fundadores y los mejores equipos restantes de las grandes ligas.
 
 Actualización: Uso de este proyecto como parte del tfg, nuesvas tecnologias: python, mysql.
 
 Version moderna:

- Implementacion de python en el proyecto a partir de webscraping y otros conceptos.
- Uso de mysql como sistema de gestión de base de datos.
- Uso de php para página de estadisticas.
- Bot de twitter para twittear el resultado de los partidos.


Web scraping:
hemos usado las paginas oficiales de las ligas. Para las estadisticas de los jugadores hemos usado la página:
https://sofifa.com/teams

para ejecutar las jornadas hay que utilizar el archivo: https://github.com/Ignaciogovo/GranLigaEuropea/blob/master/CreacionBBDDYEstadisticas/python/EjecucionEstadisticas/jornada.py

Hay que conectarlo al servidor Mysql indicando las credenciales en el archivo:
https://github.com/Ignaciogovo/GranLigaEuropea/blob/master/CreacionBBDDYEstadisticas/python/conexionpython.py


Bot de twitter: https://twitter.com/granligaeuropa

Página con resultados: http://granligaeuropea.freetzi.com
     
     


 Modelo relacional: 
![ Modelo relacional](https://github.com/Ignaciogovo/GranLigaEuropea/blob/master/CreacionBBDDYEstadisticas/mysql/diagrama.png)





Version antigua:
 Se utiliza sql server como sistema de gestión de la base de datos y xampp para php. A la hora de conectar la base de datos con el codigo php se tendrá que configurar xampp
    Enfoque:
     Proyecto durante las navidades para practicar conceptos aprendidos en sql server y php.
     Además de eso, hay una series de recursos que se pueden utilizar de forma independiente, como es La creación de las jornadas.
