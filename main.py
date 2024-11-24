from updating_modules_package import updating_logic
from files_move_package import automatic_files, automatic_move_files
from downloading_modules_package import downloading_logic

if __name__ == "__main__":
    """
    v1.0

    Punto de entrada principal del script.

    Este script realiza las siguientes acciones:
    1. Descarga módulos desde GitHub.
    2. Actualiza los módulos descargados.
    3. Mueve los módulos actualizados a los directorios correspondientes.

    Las funciones específicas para cada acción se importan de diferentes paquetes.
    """
    #downloading_logic.downloading_modules_from_github()    # Descomentar para descargar módulos nuevos desde GitHub.
    print('Iniciando actualización, por favor espere...')
    updating_logic.updating_modules_from_github()
    print('Actualización terminada.\n')
    print('Iniciando movimiento de módulos actualizados, por favor espere...')
    automatic_files.moving_directories_files()
    automatic_move_files.moving_directories_files()
    print('Ejecución terminada.')
