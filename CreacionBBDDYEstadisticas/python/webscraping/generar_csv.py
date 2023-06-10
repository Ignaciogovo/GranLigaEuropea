import os
import csv

class CSVWriter:
    def __init__(self, filename, headers, directory='datos_csv'):
        # Concatenamos el directorio con el nombre de archivo para obtener la ruta completa
        self.filename = os.path.join(directory, filename) # Esta función combina los datos para crear una ruta valida según el s.o
        self.headers = headers

    def _file_exists(self):
        # Comprueba si el archivo especificado en self.filename existe
        if self.filename is not None:
            return os.path.isfile(self.filename)

    def write_data(self, data, mode='w'):
        # Escribe los datos en un archivo CSV especificado en self.filename
        if self.filename is not None:
            with open(self.filename, mode=mode, newline='') as csv_file:
                writer = csv.writer(csv_file)

                if mode == 'w' or not self._file_exists():
                    # Si el modo es 'w' (write) o el archivo no existe, escribe las cabeceras
                    writer.writerow(self.headers)

                for row in data:
                    # Escribe cada fila de datos en el archivo
                    writer.writerow(row)

    def add_row(self, row):
        # Agrega una sola fila al archivo CSV
        self.write_data([row], mode='a')

    def clear_file(self):
        # Borra el contenido del archivo CSV
        open(self.filename, 'w').close()
