import persistencia

def añadir_elemento(titulo, tipo, autor, genero, valoracion=None):
    """
    Carga la lista, añade un diccionario con el nuevo elemento y guarda.
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
    Devuelve todos los elementos registrados en el JSON.
    """
    return persistencia.cargar_datos()


def buscar_elementos(criterio, texto_busqueda):
    """
    Busca elementos que coincidan parcial o totalmente con el criterio elegido 
    ('titulo', 'autor' o 'genero'). No distingue entre mayúsculas y minúsculas.
    """
    lista_actual = persistencia.cargar_datos()
    resultados = []
    
    for elemento in lista_actual:
        if texto_busqueda.lower() in elemento[criterio].lower():
            resultados.append(elemento)
            
    return resultados


def editar_elemento(titulo_original, nuevos_datos):
    """
    Busca un elemento por su título original y actualiza todos sus campos,
    incluyendo el tipo modificado.
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
    Elimina de la lista el elemento que coincida con el título entregado.
    """
    lista_actual = persistencia.cargar_datos()
    longitud_inicial = len(lista_actual)
    
    # Conservamos todos los elementos EXCEPTO el que queremos borrar
    lista_actual = [e for e in lista_actual if e["titulo"].lower() != titulo_a_borrar.lower()]
    
    if len(lista_actual) < longitud_inicial:
        return persistencia.guardar_datos(lista_actual)
    return False