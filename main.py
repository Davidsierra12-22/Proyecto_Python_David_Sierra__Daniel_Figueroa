# Punto de entrada. Solo arranca la app y llama al menú principal.
# Importamos los tres módulos que creaste paso a paso
import interfaz
import coleccion
import persistencia

def ejecutar_aplicacion():
    """
    Función principal que coordina el flujo de toda la aplicación.
    """
    # Al iniciar el programa, saludamos al usuario
    print("¡Bienvenido al Administrador de Colección!")
    
    while True:
        # 1. Mostramos el menú y capturamos la opción elegida
        opcion = interfaz.mostrar_menu_principal()
        
        # 2. Evaluamos la opción del usuario
        if opcion == "1":
            # Recolectamos los datos desde la interfaz
            titulo, tipo, autor, genero, valoracion = interfaz.pedir_datos_elemento()
            
            # Pasamos los datos a la lógica de la colección para que los procese y guarde
            exito = coleccion.añadir_elemento(titulo, tipo, autor, genero, valoracion)
            
            if exito:
                print("\n✅ ¡Elemento añadido con éxito a la colección!")
            else:
                print("\n❌ Hubo un problema al intentar guardar el elemento.")
                
        elif opcion == "2":
            # Traemos todos los elementos que hay guardados
            elementos = coleccion.listar_elementos()
            
            # Le pasamos la lista a la interfaz para que dibuje la tabla con tabulate
            interfaz.mostrar_tabla_elementos(elementos)
            
        elif opcion in ["3", "4", "5"]:
            # Dejamos un mensaje temporal para las opciones que programaremos luego
            print("\n🔍 Esta función estará disponible en la próxima actualización.")
            
        elif opcion == "6":
            # Rompemos el ciclo infinito para cerrar la aplicación de consola
            print("\n👋 ¡Gracias por usar el Administrador de Colección! Hasta luego.")
            break
            
        else:
            print("\n❌ Opción inválida. Por favor, digita un número del 1 al 6.")

# Este bloque le dice a Python que si ejecutamos este archivo directamente, corra la app
if __name__ == "__main__":
    ejecutar_aplicacion()