# Módulo de lógica de la colección.
# Aquí se define la gestión de los elementos culturales: agregar, consultar,
# editar y eliminar registros, usando la capa de persistencia para guardar
# y recuperar la información desde el archivo JSON.
import os #se ñade por q se requier para el proceso de calcular el promedio
import json#necesitamos el json por manejamos un nuvo modulo con archivos jison de la misma def de promedio
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

#funcion q calcula el promedio general del tipo tal como piede el quiz


def promedio_valoraciones(categoria=None):
    """
    Calcula la valoración promedio por categoría o de toda la colección.
    Si se especifica una categoría (Libro, Película, Música), calcula el promedio
    solo para esa categoría. Si no se especifica, calcula el promedio general.
    Los resultados se exportan a 'reports/promedio_valoraciones.json'.
    """
    # 1. Obtener todos los elementos de la colección
    elementos = listar_elementos()
    
    # 2. Inicializar acumuladores y contadores
    acumuladores = {"Libro": 0, "Película": 0, "Música": 0}
    contadores = {"Libro": 0, "Película": 0, "Música": 0}
    
    # 3. Clasificar y sumar valoraciones
    for item in elementos:
        tipo = item.get("tipo")
        valoracion = item.get("valoracion")
        
        if tipo in acumuladores and isinstance(valoracion, (int, float)):
            acumuladores[tipo] += valoracion
            contadores[tipo] += 1

    # 4. Calcular promedios por categoría
    promedios_finales = {
        "Libro": round(acumuladores["Libro"] / contadores["Libro"], 2) if contadores["Libro"] > 0 else 0.0,
        "Película": round(acumuladores["Película"] / contadores["Película"], 2) if contadores["Película"] > 0 else 0.0,
        "Música": round(acumuladores["Música"] / contadores["Música"], 2) if contadores["Música"] > 0 else 0.0
    }

    # 5. Mostrar resultados según la categoría solicitada
    if categoria:
        promedio_categoria = promedios_finales.get(categoria, 0.0)
        print(f"\n📊 Promedio de valoraciones para {categoria}: {promedio_categoria} ⭐")
        return promedio_categoria
    else:
        print("\n📊 === PROMEDIOS CALCULADOS ===")
        for cat, prom in promedios_finales.items():
            print(f"🔸 {cat}: {prom} ⭐")
        print("================================\n")
    
    # 6. Crear la carpeta de reportes y guardar el archivo JSON
    os.makedirs("reports", exist_ok=True)
    ruta_reporte = os.path.join("reports", "promedio_valoraciones.json")
    
    try:
        with open(ruta_reporte, "w", encoding="utf-8") as archivo:
            json.dump(promedios_finales, archivo, ensure_ascii=False, indent=4)
        print(f"✅ ¡Reporte guardado con éxito en '{ruta_reporte}'!")
        return promedios_finales
    except Exception as e:
        print(f"❌ Error al escribir el archivo: {e}")
        return None