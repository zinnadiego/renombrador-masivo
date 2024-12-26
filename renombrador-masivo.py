import os
import shutil

def renombrar_archivos(ruta_origen, ruta_destino, palabra_buscar, palabra_reemplazo):
    # Verificar que la carpeta de origen existe
    if not os.path.exists(ruta_origen):
        print(f"La carpeta de origen {ruta_origen} no existe")
        return
    
    # Verificar que la carpeta de destino existe, si no, crearla
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)
        print(f"Se creó la carpeta de destino: {ruta_destino}")
    
    # Mostrar todos los archivos encontrados y sus extensiones
    archivos = os.listdir(ruta_origen)
    extensiones = set()
    print(f"\nArchivos encontrados en la carpeta: {len(archivos)}")
    for archivo in archivos:
        extension = os.path.splitext(archivo)[1]
        if extension:
            extensiones.add(extension)
        print(f"Archivo encontrado: {archivo}")
    
    # Mostrar tipos de archivos encontrados
    if extensiones:
        print("\nTipos de archivos encontrados:")
        for ext in sorted(extensiones):
            print(f"- {ext}")
    
    # Contador de archivos procesados
    archivos_procesados = 0
    
    print("\nIniciando proceso de renombrado:")
    for nombre_archivo in archivos:
        if palabra_buscar.lower() in nombre_archivo.lower():
            nuevo_nombre = nombre_archivo.lower().replace(palabra_buscar.lower(), palabra_reemplazo.lower())
            
            ruta_original = os.path.join(ruta_origen, nombre_archivo)
            ruta_nuevo = os.path.join(ruta_destino, nuevo_nombre)
            
            try:
                shutil.copy2(ruta_original, ruta_nuevo)
                print(f"Copiado y renombrado: {nombre_archivo} -> {nuevo_nombre}")
                archivos_procesados += 1
            except Exception as e:
                print(f"Error al procesar {nombre_archivo}: {e}")
    
    # Resumen final
    if archivos_procesados == 0:
        print(f"\nNo se encontró ningún archivo con '{palabra_buscar}' en el nombre")
    else:
        print(f"\nSe procesaron {archivos_procesados} archivos")

if __name__ == "__main__":
    # Configuración de las rutas y palabras
    carpeta_origen = r"ruta/a/carpeta/origen"
    carpeta_destino = r"ruta/a/carpeta/destino"
    palabra_a_buscar = "palabra-a-buscar"    # Aquí pones la palabra que quieres buscar
    palabra_nueva = "palabra-de-reemplazo"      # Aquí pones la palabra por la que quieres reemplazar

    print(f"Revisando la carpeta de origen: {carpeta_origen}")
    print(f"Los archivos se guardarán en: {carpeta_destino}")
    print(f"Buscando archivos que contengan: '{palabra_a_buscar}'")
    print(f"Reemplazando por: '{palabra_nueva}'")
    
    renombrar_archivos(carpeta_origen, carpeta_destino, palabra_a_buscar, palabra_nueva)