# Manejo de la consola (mostrar menús, tablas, colores, inputs).
from tabulate import tabulate

def mostrar_menu_principal():
    """
    Dibuja el menú de opciones en la consola y retorna la opción que elija el usuario.
    Basado en estructuras limpias de menús de consola.
    """
    print("\n=========================================")
    print("  ADMINISTRADOR DE COLECCIÓN CULTURAL   ")
    print("=========================================")
    print(" 1. ➕ Añadir nuevo elemento")
    print(" 2. 📋 Listar toda la colección")
    print(" 3. 🔍 Buscar elemento (Próximamente)")
    print(" 4. ✏️  Editar elemento (Próximamente)")
    print(" 5. ❌ Eliminar elemento (Próximamente)")
    print(" 6. 🚪 Salir")
    print("=========================================")
    
    opcion = input("Seleccione una opción (1-6): ").strip()
    return opcion


def pedir_datos_elemento():
    """
    Le pide al usuario los datos necesarios para registrar un libro, película o música.
    Valida que los campos obligatorios no queden vacíos.
    """
    print("\n--- REGISTRAR NUEVO ELEMENTO ---")
    
    # Validamos el tipo
    while True:
        tipo = input("Tipo (Libro / Película / Música): ").strip().capitalize()
        if tipo in ["Libro", "Película", "Música", "Pelicula", "Musica"]:
            # Normalizamos con tildes para que el JSON quede impecable
            if tipo == "Pelicula": tipo = "Película"
            if tipo == "Musica": tipo = "Música"
            break
        print("❌ Tipo no válido. Por favor, escribe Libro, Película o Música.")

    # Validamos el título (Obligatorio)
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            break
        print("❌ El título no puede estar vacío.")

    # Validamos el Autor/Artista (Obligatorio)
    while True:
        autor = input("Autor / Director / Artista: ").strip()
        if autor:
            break
        print("❌ Este campo es obligatorio.")

    genero = input("Género: ").strip().capitalize()
    if not genero:
        genero = "General"  # Valor por defecto si no pone nada

    # Valoración opcional (Validamos que sea un número entre 1 y 5, o vacío)
    while True:
        val_input = input("Valoración (1 al 5 - Opcional, presione Enter para saltar): ").strip()
        if val_input == "":
            valoracion = "Sin calificar"
            break
        if val_input.isdigit() and 1 <= int(val_input) <= 5:
            valoracion = int(val_input)
            break
        print("❌ Por favor, ingrese un número entero entre 1 y 5.")

    return titulo, tipo, autor, genero, valoracion


def mostrar_tabla_elementos(lista_elementos):
    """
    Recibe una lista de diccionarios y la dibuja en una tabla hermosa 
    en la consola usando la librería tabulate.
    """
    print("\n--- MI COLECCIÓN PERSONAL ---")
    
    if not lista_elementos:
        print("⚠️ La colección está vacía. ¡Prueba añadiendo algo primero!")
        return

    # Creamos una lista de listas (matriz) que es el formato que pide tabulate
    tabla = []
    for item in lista_elementos:
        tabla.append([
            item["titulo"],
            item["tipo"],
            item["autor"],
            item["genero"],
            item["valoracion"]
        ])
    
    # Definimos los encabezados de las columnas
    encabezados = ["Título", "Tipo", "Autor/Artista", "Género", "Valoración"]
    
    # Imprimimos la tabla con un diseño limpio (estilo 'fancy_grid')
    print(tabulate(tabla, headers=encabezados, tablefmt="fancy_grid"))