# Módulo de interfaz de consola.
# Aquí se concentra toda la parte visual del programa: menús, preguntas,
# mensajes para el usuario y la presentación de los datos en tablas.

from tabulate import tabulate


def mostrar_menu_principal():
    """
    Muestra el menú principal del sistema en pantalla.
    Esta función sirve como punto de entrada para que el usuario elija qué
    acción desea realizar: añadir, listar, buscar, editar, eliminar,
    filtrar por categoría, guardar/cargar, calcular promedios o salir.
    Devuelve la opción escrita por el usuario para que la lógica principal
    la procese en el bucle del programa.
    """
    print("\n=========================================")
    print("     ADMINISTRADOR DE COLECCIÓN         ")
    print("=========================================")
    print(" 1. ➕ Añadir un Nuevo Elemento")
    print(" 2. 📋 Ver Todos los Elementos")
    print(" 3. 🔍 Buscar un Elemento")
    print(" 4. ✏️  Editar un Elemento")
    print(" 5. ❌ Eliminar un Elemento")
    print(" 6. 🗂️  Ver Elementos por Categoría")
    print(" 7. 💾 Guardar y Cargar Colección")
    print(" 8. 📊 Calcular Promedio por Categoría")#se añade la opcion n el menu principal para q tmabien la puedan usar como tal 
    print(" 9. 🚪 Salir")
    print("=========================================")

    return input("Selecciona una opción (1-9): ").strip()


def mostrar_menu_categorias():
    """
    Muestra un submenú para filtrar la colección por tipo de contenido.
    Ayuda al usuario a ver únicamente libros, películas o música sin
    complicar la navegación del programa.
    """
    print("\n=========================================")
    print("      VER ELEMENTOS POR CATEGORÍA        ")
    print("=========================================")
    print(" 1. Ver Libros")
    print(" 2. Ver Películas")
    print(" 3. Ver Música")
    print(" 4. Regresar al Menú Principal")
    print("=========================================")

    return input("Selecciona una opción (1-4): ").strip()


def mostrar_menu_guardado():
    """
    Muestra un submenú para guardar o recargar la colección desde disco.
    Esto mantiene la experiencia clara y ayuda a entender dónde se guardan
    los cambios realizados en la aplicación.
    """
    print("\n=========================================")
    print("      GUARDAR Y CARGAR COLECCIÓN        ")
    print("=========================================")
    print(" 1. Guardar la Colección Actual")
    print(" 2. Cargar la Colección Guardada")
    print(" 3. Regresar al Menú Principal")
    print("=========================================")

    return input("Selecciona una opción (1-3): ").strip()


def pedir_datos_elemento(valores_previos=None):
    """
    Solicita al usuario todos los datos necesarios para crear o editar un elemento.
    Si recibe una colección de valores previos, esta función funciona en modo
    edición: muestra los datos actuales y permite cambiarlos uno por uno,
    manteniendo los valores que el usuario deje en blanco.
    Devuelve una tupla con título, tipo, autor, género y valoración.
    """
    if valores_previos:
        print(f"\n--- EDITANDO: {valores_previos['titulo']} ---")
        msg_omitir = " (Presione Enter para mantener el actual)"
    else:
        print("\n--- REGISTRAR NUEVO ELEMENTO ---")
        msg_omitir = ""

    # 1. Validar Tipo (Permite edición fluida)
    while True:
        default = f" [{valores_previos['tipo']}]" if valores_previos else ""
        tipo = input(f"Tipo (Libro / Película / Música){default}: ").strip().capitalize()
        
        if not tipo and valores_previos:
            tipo = valores_previos["tipo"]
            break
            
        if tipo in ["Libro", "Película", "Música", "Pelicula", "Musica"]:
            if tipo == "Pelicula": tipo = "Película"
            if tipo == "Musica": tipo = "Música"
            break
        print("❌ Tipo no válido. Por favor, escribe Libro, Película o Música.")

    # 2. Validar Título
    while True:
        default = f" [{valores_previos['titulo']}]" if valores_previos else ""
        titulo = input(f"Título{default}: ").strip()
        if not titulo and valores_previos:
            titulo = valores_previos["titulo"]
            break
        if titulo: break
        print("❌ El título es obligatorio.")

    # 3. Validar Autor
    while True:
        default = f" [{valores_previos['autor']}]" if valores_previos else ""
        autor = input(f"Autor/Director/Artista{default}: ").strip()
        if not autor and valores_previos:
            autor = valores_previos["autor"]
            break
        if autor: break
        print("❌ Este campo es obligatorio.")

    # 4. Género
    default = f" [{valores_previos['genero']}]" if valores_previos else ""
    genero = input(f"Género{default}: ").strip().capitalize()
    if not genero and valores_previos:
        genero = valores_previos["genero"]
    elif not genero:
        genero = "General"

    # 5. Valoración
    while True:
        default = f" [{valores_previos['valoracion']}]" if valores_previos else ""
        val_input = input(f"Valoración (1 al 5){default}{msg_omitir}: ").strip()
        if val_input == "" and valores_previos:
            valoracion = valores_previos["valoracion"]
            break
        if val_input == "":
            valoracion = "Sin calificar"
            break
        if val_input.isdigit() and 1 <= int(val_input) <= 5:
            valoracion = int(val_input)
            break
        print("❌ Ingrese un número entero entre 1 y 5.")

    return titulo, tipo, autor, genero, valoracion


def convertir_estrellas(valoracion):
    """
    Convierte una valoración numérica en una representación visual de estrellas.
    Si la puntuación es un número entero entre 1 y 5, la función devuelve
    una cadena con ese número de símbolos ⭐; si no es numérica, devuelve
    el valor tal como está para mostrarlo sin alterar el formato.
    """
    if isinstance(valoracion, int):
        return "⭐" * valoracion
    return valoracion


def mostrar_tabla_elementos(lista_elementos, titulo_tabla="MI COLECCIÓN PERSONAL"):
    """
    Presenta una lista de elementos en formato de tabla para facilitar su lectura.
    Esta función convierte los datos en filas y columnas, aplica el formato
    visual de la librería tabulate y muestra el resultado en consola.
    Si la lista está vacía, informa al usuario que no hay elementos.
    """
    print(f"\n--- {titulo_tabla} ---")
    if not lista_elementos:
        print("⚠️ No hay elementos para mostrar.")
        return

    tabla = []
    for item in lista_elementos:
        estrellas = convertir_estrellas(item["valoracion"])
        tabla.append([
            item["titulo"],
            item["tipo"],
            item["autor"],
            item["genero"],
            estrellas
        ])
    
    encabezados = ["Título", "Tipo", "Autor/Artista", "Género", "Valoración"]
    print(tabulate(tabla, headers=encabezados, tablefmt="fancy_grid"))


def pedir_criterio_busqueda():
    """
    Pide al usuario el criterio y el texto para buscar elementos en la colección.
    Permite filtrar por título, autor o género, y devuelve ambos valores para
    que la capa de lógica pueda localizar coincidencias en los datos guardados.
    """
    print("\n--- CRITERIOS DE BÚSQUEDA ---")
    print("1. Por Título")
    print("2. Por Autor/Director/Artista")
    print("3. Por Género")
    opc = input("Seleccione el criterio (1-3): ").strip()
    
    texto = input("Escriba el texto a buscar: ").strip()
    
    if opc == "1": return "titulo", texto
    if opc == "2": return "autor", texto
    return "genero", texto

#se crea un menu interacri para la nueva funcionalidad del quiz 
def mostrar_menu_promedio():
    """
    Muestra un submenú para calcular el promedio de valoraciones por categoría.
    Permite al usuario elegir si desea calcular el promedio de libros,
    películas, música o regresar al menú principal.
    """
    print("\n=========================================")
    print("   CALCULAR PROMEDIO POR CATEGORÍA      ")
    print("=========================================")
    print(" 1. Promedio de Libros")
    print(" 2. Promedio de Películas")
    print(" 3. Promedio de Música")
    print(" 4. Promedio General")
    print(" 5. Regresar al Menú Principal")
    print("=========================================")

    return input("Selecciona una opción (1-5): ").strip()