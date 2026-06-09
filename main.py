# Módulo principal de la aplicación.
# Este archivo orquesta el flujo general del programa: muestra el menú,
# recibe la opción del usuario y llama a las funciones de la interfaz y
# de la colección para realizar cada operación.

import interfaz
import coleccion
import persistencia


def ejecutar_aplicacion():
    """
    Inicia y mantiene el ciclo principal de la aplicación.
    Esta función muestra el menú al usuario, interpreta la opción elegida
    y dirige la ejecución hacia las funciones de añadir, listar, buscar,
    editar o eliminar elementos hasta que el usuario decida salir.
    """
    print("¡Bienvenido al Administrador de Colección!")
    
    while True:
        opcion = interfaz.mostrar_menu_principal()
        
        # 1. AÑADIR
        if opcion == "1":
            titulo, tipo, autor, genero, valoracion = interfaz.pedir_datos_elemento()
            if coleccion.añadir_elemento(titulo, tipo, autor, genero, valoracion):
                print("\n✅ ¡Elemento añadido con éxito!")
            else:
                print("\n❌ Error al guardar.")
                
        # 2. LISTAR
        elif opcion == "2":
            elementos = coleccion.listar_elementos()
            interfaz.mostrar_tabla_elementos(elementos)
            
        # 3. BUSCAR
        elif opcion == "3":
            criterio, texto = interfaz.pedir_criterio_busqueda()
            resultados = coleccion.buscar_elementos(criterio, texto)
            interfaz.mostrar_tabla_elementos(resultados, f"RESULTADOS DE BÚSQUEDA ({texto.upper()})")
            
        # 4. EDITAR
        elif opcion == "4":
            titulo_editar = input("\n✏️ Escribe el título EXACTO del elemento a editar: ").strip()
            coincidencias = coleccion.buscar_elementos("titulo", titulo_editar)
            
            elemento_encontrado = None
            for c in coincidencias:
                if c["titulo"].lower() == titulo_editar.lower():
                    elemento_encontrado = c
                    break
            
            if elemento_encontrado:
                # Capturamos todos los datos (incluyendo el tipo modificado)
                t, tp, aut, gen, val = interfaz.pedir_datos_elemento(elemento_encontrado)
                
                # Armamos el diccionario correcto con el tipo incluido
                nuevos_datos = {
                    "titulo": t,
                    "tipo": tp,
                    "autor": aut,
                    "genero": gen,
                    "valoracion": val
                }
                
                if coleccion.editar_elemento(titulo_editar, nuevos_datos):
                    print("\n✅ ¡Elemento modificado exitosamente!")
                else:
                    print("\n❌ No se pudieron guardar las modificaciones.")
            else:
                print("❌ No se encontró ningún elemento con ese título.")
                
        # 5. ELIMINAR
        elif opcion == "5":
            titulo_borrar = input("\n❌ Escribe el título EXACTO del elemento a eliminar: ").strip()
            seguro = input(f"¿Estás seguro de eliminar '{titulo_borrar}'? (s/n): ").strip().lower()
            
            if seguro == 's':
                if coleccion.eliminar_elemento(titulo_borrar):
                    print("\n🗑️ ¡Elemento eliminado correctamente de la colección!")
                else:
                    print("❌ No se encontró ningún elemento con ese título.")
            else:
                print("\n🚫 Operación cancelada.")
            
        # 6. VER ELEMENTOS POR CATEGORÍA
        elif opcion == "6":
            subopcion = interfaz.mostrar_menu_categorias()
            if subopcion == "1":
                categoria = "Libro"
            elif subopcion == "2":
                categoria = "Película"
            elif subopcion == "3":
                categoria = "Música"
            elif subopcion == "4":
                print("\n↩️ Regresando al menú principal...")
                continue
            else:
                print("\n❌ Opción inválida. Intenta de nuevo.")
                continue

            elementos = [item for item in coleccion.listar_elementos() if item.get("tipo") == categoria]
            interfaz.mostrar_tabla_elementos(elementos, f"ELEMENTOS DE TIPO {categoria.upper()}")

        # 7. GUARDAR Y CARGAR COLECCIÓN
        elif opcion == "7":
            subopcion = interfaz.mostrar_menu_guardado()

            if subopcion == "1":
                if persistencia.guardar_datos(coleccion.listar_elementos()):
                    print("\n💾 Colección guardada correctamente en disco.")
                else:
                    print("\n❌ No se pudo guardar la colección.")

            elif subopcion == "2":
                elementos = persistencia.cargar_datos()
                if elementos:
                    print("\n📂 Colección cargada desde el archivo JSON.")
                    interfaz.mostrar_tabla_elementos(elementos, "COLECCIÓN RECARGADA DESDE DISCO")
                else:
                    print("\n⚠️ No hay datos guardados para cargar.")

            elif subopcion == "3":
                print("\n↩️ Regresando al menú principal...")

            else:
                print("\n❌ Opción inválida. Intenta de nuevo.")

        # 8. SALIR
        elif opcion == "8":
            print("\n👋 ¡Gracias por usar el Administrador de Colección! Hasta luego.")
            break
        else:
            print("\n❌ Opción inválida. Digita de 1 a 8.")

if __name__ == "__main__":
    ejecutar_aplicacion()