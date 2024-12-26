# Renombrador Masivo de Archivos

Una utilidad en Python que permite renombrar múltiples archivos reemplazando palabras específicas en sus nombres. Compatible con cualquier tipo de archivo (.pdf, .xlsx, .docx, .jpg, etc.) y mantiene los archivos originales intactos creando copias.

## Características

- Busca archivos que contengan palabras específicas en sus nombres
- Reemplaza las palabras objetivo por nuevas
- Compatible con cualquier tipo de archivo
- Identifica y muestra los tipos de archivos presentes
- Mantiene los archivos originales intactos creando copias
- Carpetas de origen y destino configurables
- Búsqueda sin distinción entre mayúsculas y minúsculas
- Registros detallados de la ejecución

## Requisitos

- Python 3.x
- No requiere dependencias adicionales (usa solo bibliotecas incorporadas)

## Instalación

1. Clona este repositorio
```bash
git clone https://github.com/zinnadiego/renombrador-masivo
```

2. Navega al directorio del proyecto

```bash
cd renombrador-masivo
```

## Uso

1. Configura el script modificando estas variables:

```bash
carpeta_origen = r"ruta/a/carpeta/origen"      # Ruta de la carpeta de origen
carpeta_destino = r"ruta/a/carpeta/destino"    # Ruta de la carpeta de destino
palabra_a_buscar = "palabra-a-buscar"          # Palabra a buscar
palabra_nueva = "palabra-de-reemplazo"         # Palabra por la que reemplazar
```
2. Ejecuta el script:

```bash
python renombrar_archivos.py
```

## Ejemplos de Uso
### Ejemplo 1: Renombrar informes
```bash
carpeta_origen = r"C:\Users\Documentos\Informes"
carpeta_destino = r"C:\Users\Documentos\Informes_Renombrados"
palabra_a_buscar = "informe"
palabra_nueva = "reporte"
```

### Ejemplo 2: Renombrar archivos de un proyecto

```bash
carpeta_origen = r"C:\Proyectos\Proyecto2023"
carpeta_destino = r"C:\Proyectos\Proyecto2023_Nuevo"
palabra_a_buscar = "proyecto_viejo"
palabra_nueva = "proyecto_nuevo"
```

## Tipos de Archivos Soportados

Documentos (.pdf, .doc, .docx, .txt)
Hojas de cálculo (.xls, .xlsx, .csv)
Imágenes (.jpg, .png, .gif, .bmp)
Archivos de presentación (.ppt, .pptx)
Archivos comprimidos (.zip, .rar)
Y cualquier otro tipo de archivo

## Cómo Funciona

El script primero verifica si existe la carpeta de origen
Crea la carpeta de destino si no existe
Analiza y muestra los tipos de archivos encontrados
Lista todos los archivos en la carpeta de origen

Para cada archivo:
Comprueba si contiene la palabra objetivo (sin distinguir mayúsculas/minúsculas)
Crea un nuevo nombre de archivo con la palabra de reemplazo
Copia el archivo a la carpeta de destino con el nuevo nombre


Proporciona un registro detallado de todas las operaciones

Ejemplo de Salida

```bash
Revisando la carpeta de origen: C:\Users\Documentos\Archivos
Los archivos se guardarán en: C:\Users\Documentos\Archivos_Renombrados
Buscando archivos que contengan: 'informe'
Reemplazando por: 'reporte'

Archivos encontrados en la carpeta: 5
Archivo encontrado: informe_enero.pdf
Archivo encontrado: informe_ventas.xlsx
Archivo encontrado: datos_informe.docx

Tipos de archivos encontrados:
- .pdf
- .xlsx
- .docx

Iniciando proceso de renombrado:
Copiado y renombrado: informe_enero.pdf -> reporte_enero.pdf
Copiado y renombrado: informe_ventas.xlsx -> reporte_ventas.xlsx
Copiado y renombrado: datos_informe.docx -> datos_reporte.docx

Se procesaron 3 archivos
```
## Manejo de Errores

El script incluye manejo de errores para escenarios comunes:

- Carpeta de origen inexistente
- Problemas de permisos
- Errores de lectura/escritura de archivos
- Archivos en uso o bloqueados
- Nombres de archivo inválidos
- Cada error se registra con un mensaje descriptivo

## Licencia
MIT

## Autor
Diego Alejandro Zinna Fallico