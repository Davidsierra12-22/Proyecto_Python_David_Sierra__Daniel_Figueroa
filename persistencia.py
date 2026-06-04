# Cargar y guardar el archivo JSON.

{
    "titulo": "El Señor de los Anillos",
    "tipo": "Libro",  # Puede ser Libro, Película o Música
    "autor": "J.R.R. Tolkien",
    "genero": "Fantasía",
    "valoracion": 5  # Puntuación opcional del 1 al 5
}

import json
import os

# Nombre del archivo donde se guardará la colección
ARCHIVO_DATOS = "coleccion.json"

def guardar_datos(lista_elementos):
    """
    Recibe una lista de Python (con todos los libros/películas)
    y la guarda en el archivo JSON.
    """
    try:
        # 'w' significa modo escritura (write). Si el archivo no existe, lo crea.
        # Si ya existe, borra lo anterior y escribe lo nuevo.
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
            # json.dump convierte la lista de Python en formato JSON y la guarda.
            # indent=4 es para que el archivo JSON se vea ordenado y bonito, no en una sola línea.
            json.dump(lista_elementos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        # Si algo falla (por ejemplo, permisos de administrador), avisa del error
        print(f"Error al guardar los datos: {e}")
        return False


def cargar_datos():
    """
    Busca el archivo JSON. Si existe, lee los datos y los devuelve como una lista.
    Si no existe, devuelve una lista vacía para empezar desde cero.
    """
    # os.path.exists verifica si el archivo 'coleccion.json' ya existe en la carpeta
    if not os.path.exists(ARCHIVO_DATOS):
        # Si no existe, devolvemos una lista vacía para que el programa empiece limpio
        return []

    try:
        # 'r' significa modo lectura (read).
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
            # json.load toma el texto del JSON y lo convierte de vuelta en una lista de Python
            datos = json.load(archivo)
            return datos
    except Exception as e:
        # Si el archivo está corrupto o tiene un error de formato, devolvemos lista vacía
        print(f"Error al cargar los datos: {e}")
        return []