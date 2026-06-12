# 📊 Reporte de Configuración y Estrategia de Commits
### Campuslands | Plan de Distribución Integral del Parcial

Este documento contiene la planificación y distribución de cambios estructurados en Git bajo el estándar internacional de **Conventional Commits**. Se detalla el mapeo de modificaciones realizadas sobre las capas de presentación, lógica y datos para la nueva funcionalidad analítica del sistema de gestión.

---

## 1. Matriz de Cambios Realizados

| Módulo Modificado | Capa de Software | Descripción del Cambio Realizado |
| :--- | :--- | :--- |
| **`coleccion.py`** | Lógica de Negocio | Implementación del motor matemático para promedios globales e individuales por categoría (evita la división por cero). |
| **`interfaz.py`** | Presentación / UX | Estructuración visual de menús individuales, captura de inputs depurados con `.strip()` y renderizado estético con la librería `tabulate`. |
| **`main.py`** | Controlador / Orquestación | Enrutamiento de opciones en el ciclo principal y mapeo de señales hacia la interfaz y lógica. |
| **`reports/ (JSON)`** | Persistencia de Reportes | Generación física automática del archivo de reporte permanente estructurado con claves semánticas precisas (`Libros`, `Películas`, `Música`). |

> **💡 Recomendación del Trainer:** Para garantizar un historial de Git impecable y profesional ante la revisión del repositorio, dividiremos los cambios en 3 commits específicos. Esto demuestra control absoluto del flujo y evita el antipatrón de subir "todo en un solo paquete gigante".

---

## 2. Secuencia de Commits Planificada

### 🔹 Primer Commit: La Infraestructura Lógica e Individual
Este paso asegura que el backend y los cálculos matemáticos funcionen perfectamente antes de pintar interfaces en la terminal de Linux.

* **Archivos Modificados:**
  - `coleccion.py`

* **Descripción del Cambio:**
  - Se añade el núcleo matemático para procesar las métricas de libros, películas y música.
  - Se estructura el procesamiento independiente para la colección global y elementos individuales.
  - Se implementan controles contra la división por cero y redondeo a dos decimales.

* **Comandos en la Terminal de Linux:**
  ```bash
  git add coleccion.py
  git commit -m "feat(logic): implementar promedios generales e individuales por categoria

  - Se añade el nucleo matematico para procesar las metricas de libros, peliculas y musica.
  - Se estructura el procesamiento independiente para la coleccion global y elementos individuales.
  - Se implementan controles contra la division por cero y redondeo a dos decimales."

### 🔹 Segundo Commit: Integración de Menús Analíticos y Enrutamiento
Este paso conecta la lógica matemática con la interfaz de usuario y asegura que las opciones del menú principal y submenús funcionen correctamente.

* **Archivos Modificados:**
  - `interfaz.py`
  - `main.py`

* **Descripción del Cambio:**
  - Se diseñan submenús específicos en la terminal para consultar promedios de ítems individuales.
  - Se conectan las rutas de control en main.py para disparar las funciones de reporte de forma fluida.
  - Se vincula la limpieza de datos de entrada con .strip() para la validación del usuario.

* **Comandos en la Terminal de Linux:**
  ```bash
  git add interfaz.py main.py
  git commit -m "feat(ui): integrar menus analiticos y opciones de enrutamiento

  - Se diseñan submenus especificos en la terminal para consultar promedios de items individuales.
  - Se conectan las rutas de control en main.py para disparar las funciones de reporte de forma fluida.
  - Se vincula la limpieza de datos de entrada con .strip() para la validacion del usuario."

### 🔹 Tercer Commit: Generación de Reportes y Documentación
Este paso asegura que los resultados de los cálculos se guarden en un archivo JSON y que la documentación del proyecto esté actualizada.

* **Archivos Modificados:**
  - `reports/`
  - `README-REPORTS.md`

* **Descripción del Cambio:**
  - Se configura el esquema os.makedirs para garantizar el despliegue del directorio de salida de forma dinámica.
  - Se exportan los cálculos a reports/promedio_valoraciones.json utilizando codificación UTF-8.
  - Se agrega el archivo README-REPORTS.md con la estructura, justificación y la matriz de cambios del parcial.

* **Comandos en la Terminal de Linux:**
  ```bash
  git add reports/ README-REPORTS.md
  git commit -m "feat(report): autogenerar volcado de metricas JSON y documentacion

  - Se configura el esquema os.makedirs para garantizar el despliegue del directorio de salida.
  - Se exportan los calculos a 'reports/promedio_valoraciones.json' con codificacion UTF-8.
  - Se agrega el archivo README-REPORTS.md con la estructura y la matriz de cambios del parcial."