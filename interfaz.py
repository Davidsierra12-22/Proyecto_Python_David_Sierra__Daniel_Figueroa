from tabulate import tabulate

def mostrar_menu_principal():
    """
    Dibuja el menú interactivo principal en la consola.
    """
    print("\n=========================================")
    print("  ADMINISTRADOR DE COLECCIÓN CULTURAL   ")
    print("=========================================")
    print(" 1. ➕ Añadir nuevo elemento")
    print(" 2. 📋 Listar toda la colección")
    print(" 3. 🔍 Buscar elemento")
    print(" 4. ✏️  Editar elemento")
    print(" 5. ❌ Eliminar elemento")
    print(" 6. 🚪 Salir")
    print("=========================================")
    
    return input("Seleccione una opción (1-6): ").strip()


def pedir_datos_elemento(valores_previos=None):
    """
    Pide los datos de un elemento por consola. Si recibe 'valores_previos',
    actúa en modo edición mostrando los datos antiguos y permitiendo modificarlos.
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
    Convierte un valor numérico (1-5) en estrellas gráficas.
    """
    if isinstance(valoracion, int):
        return "⭐" * valoracion
    return valoracion


def mostrar_tabla_elementos(lista_elementos, titulo_tabla="MI COLECCIÓN PERSONAL"):
    """
    Construye una matriz limpia y renderiza la tabla usando tabulate.
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
    Captura los filtros necesarios para realizar las búsquedas.
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