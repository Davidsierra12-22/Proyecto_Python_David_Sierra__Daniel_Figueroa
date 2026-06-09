# Módulo de lógica de la colección.
# Aquí se define la gestión de los elementos culturales: agregar, consultar,
# editar y eliminar registros, usando la capa de persistencia para guardar
# y recuperar la información desde el archivo JSON.

import persistencia


def añadir_elemento(titulo, tipo, autor, genero, valoracion=None):
    """
    Agrega un nuevo elemento a la colección.
    Esta función lee los datos actuales, crea un diccionario con los valores
    recibidos y lo añade a la lista antes de guardarlo en el archivo JSON.
    """
    lista_actual = persistencia.cargar_datos()
    nuevo_elemento = {
        "titulo": titulo,
        "tipo": tipo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    lista_actual.append(nuevo_elemento)
    return persistencia.guardar_datos(lista_actual)


def listar_elementos():
    """
    Devuelve toda la colección almacenada en el archivo JSON.
    Se usa para mostrar los elementos actuales al usuario o para trabajar
    con ellos desde otras funciones del programa.
    """
    return persistencia.cargar_datos()


def buscar_elementos(criterio, texto_busqueda):
    """
    Busca elementos que coincidan con un texto dado en un campo específico.
    El criterio puede ser título, autor o género; la comparación se hace de
    forma insensible a mayúsculas y minúsculas para facilitar la búsqueda.
    """
    lista_actual = persistencia.cargar_datos()
    resultados = []
    
    for elemento in lista_actual:
        if texto_busqueda.lower() in elemento[criterio].lower():
            resultados.append(elemento)
            
    return resultados


def editar_elemento(titulo_original, nuevos_datos):
    """
    Modifica un elemento existente usando el título como referencia.
    Busca el registro original, reemplaza sus datos por los nuevos valores
    y guarda la colección actualizada en el archivo JSON.
    """
    lista_actual = persistencia.cargar_datos()
    encontrado = False
    
    for elemento in lista_actual:
        if elemento["titulo"].lower() == titulo_original.lower():
            elemento["titulo"] = nuevos_datos["titulo"]
            elemento["tipo"] = nuevos_datos["tipo"]
            elemento["autor"] = nuevos_datos["autor"]
            elemento["genero"] = nuevos_datos["genero"]
            elemento["valoracion"] = nuevos_datos["valoracion"]
            encontrado = True
            break
            
    if encontrado:
        return persistencia.guardar_datos(lista_actual)
    return False


def eliminar_elemento(titulo_a_borrar):
    """
    Elimina un elemento de la colección por su título.
    Esta función filtra la lista para quitar el registro indicado y guarda
    la nueva versión en el archivo JSON si la eliminación fue exitosa.
    """
    lista_actual = persistencia.cargar_datos()
    longitud_inicial = len(lista_actual)
    
    # Conservamos todos los elementos EXCEPTO el que queremos borrar
    lista_actual = [e for e in lista_actual if e["titulo"].lower() != titulo_a_borrar.lower()]
    
    if len(lista_actual) < longitud_inicial:
        return persistencia.guardar_datos(lista_actual)
    return False