import interfaz
import coleccion

def ejecutar_aplicacion():
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
            
        # 6. SALIR
        elif opcion == "6":
            print("\n👋 ¡Gracias por usar el Administrador de Colección! Hasta luego.")
            break
        else:
            print("\n❌ Opción inválida. Digita de 1 a 6.")

if __name__ == "__main__":
    ejecutar_aplicacion()