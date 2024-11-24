import custom_paths
import shutil
import os

def moving_directories_files():
    """
    Mueve los directorios de una ubicación a otra.

    Esta función realiza las siguientes acciones:
    1. Obtiene las rutas de las versiones y los destinos desde `custom_paths`.
    2. Crea los directorios de destino si no existen.
    3. Copia los directorios de las rutas de origen a las rutas de destino.

    Solo se copian los elementos que son directorios, no los archivos individuales.
    """
    version_move_paths = custom_paths.version_move_paths()
    target_paths = custom_paths.target_paths()

    for target in version_move_paths.values():
        if not os.path.exists(target):
            os.makedirs(target)

    for repo in version_move_paths.values():
        target = target_paths.get(repo[-5:-1])
        target_list = [name for name in os.listdir(target) if os.path.isdir(os.path.join(target, name))]
        print(f'Copiando directorios a la carpeta de WSL version {repo[-5:-1]}...')
        for folder in target_list:
            source_folder = os.path.join(target, folder)
            for item in os.listdir(source_folder):
                s = os.path.join(source_folder, item)
                d = os.path.join(repo, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
