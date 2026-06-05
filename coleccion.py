# Lógica de negocio (añadir, buscar, editar, eliminar de la lista).
# Importamos el módulo de persistencia que hiciste en el paso anterior
import persistencia

def añadir_elemento(titulo, tipo, autor, genero, valoracion=None):
    """
    Carga la lista actual, crea un diccionario con el nuevo elemento,
    lo suma a la lista y guarda todo en el JSON.
    """
    # 1. Traemos los datos que ya existen en el JSON
    lista_actual = persistencia.cargar_datos()
    
    # 2. Creamos el nuevo elemento (un diccionario) con los datos que nos pasen
    nuevo_elemento = {
        "titulo": titulo,
        "tipo": tipo,          # 'Libro', 'Película' o 'Música'
        "autor": autor,        # Autor, Director o Artista
        "genero": genero,
        "valoracion": valoracion  # Puede ser un número o quedar vacío (None)
    }
    
    # 3. Lo agregamos a nuestra lista
    lista_actual.append(nuevo_elemento)
    
    # 4. Guardamos la lista actualizada en el archivo JSON usando tu otra función
    exito = persistencia.guardar_datos(lista_actual)
    return exito


def listar_elementos(filtro_tipo=None):
    """
    Devuelve la lista de elementos. 
    Si se le pide un tipo específico (ej. 'Libro'), filtra la lista.
    """
    lista_actual = persistencia.cargar_datos()
    
    # Si el usuario no quiere filtrar por tipo, devolvemos todo
    if filtro_tipo is None:
        return lista_actual
    
    # Si quiere filtrar, creamos una lista solo con los que coincidan (ej: solo Películas)
    lista_filtrada = []
    for elemento in lista_actual:
        if elemento["tipo"].lower() == filtro_tipo.lower():
            lista_filtrada.append(elemento)
            
    return lista_filtrada