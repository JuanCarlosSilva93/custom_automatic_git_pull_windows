import custom_paths
import shutil
import datetime
import stat
import os

def moving_directories_files():
    """
    Realiza el movimiento y tratamiento de los módulos que hayan sido actualizados a las rutas establecidas para el
    cargue de los mismos en los ambientes de QA, dejando trazabilidad en un .txt de cada uno de ellos.

    Pasos:
    1. Recupera las rutas del repositorio y las rutas de destino del módulo custom_paths.
    2. Asegura que todos los directorios de destino existan, creándolos si no lo hacen.
    3. Compara los directorios en las rutas del repositorio con los de las rutas de destino:
       - Copia nuevos directorios de las rutas del repositorio a las rutas de destino.
       - Elimina los directorios .git de los directorios copiados.
    4. Lee el archivo .cambios.cvs para obtener una lista de módulos actualizados:
       - Copia los módulos actualizados de las rutas del repositorio a las rutas de destino.
       - Elimina cualquier directorio existente en las rutas de destino antes de copiar.
    5. Escribe un registro de los módulos actualizados en un archivo seguimiento.txt en cada ruta de destino,
       incluyendo una marca de tiempo de cuando ocurrió la actualización.
    """
    repo_paths = custom_paths.repo_paths()
    target_paths = custom_paths.target_paths()

    # Asegura que todos los directorios de destino existan
    for target in target_paths.values():
        if not os.path.exists(target):
            os.makedirs(target)

    # Compara y copia nuevos directorios del repositorio a las rutas de destino
    for repo in repo_paths.values():
        target = target_paths.get(repo[-5:-1])
        repo_list = [name for name in os.listdir(repo) if os.path.isdir(os.path.join(repo, name))]
        target_list = [name for name in os.listdir(target) if os.path.isdir(os.path.join(target, name))]
        if len(repo_list) != len(target_list):
            difference_set = set(repo_list) - set(target_list)
            for folder in difference_set:
                def on_rm_error(func, path, exc_info):
                    # Cambia los permisos y vuelve a intentar eliminar
                    os.chmod(path, stat.S_IWRITE)
                    func(path)
                shutil.copytree(repo + folder, target + folder)
                if folder == 'l10n_co_base' and repo[-5:-1] != '16.0':
                    folder += '/l10n_co_base'
                shutil.rmtree(target + folder + '/.git', onerror=on_rm_error)
                print(f'Se ha creado el módulo {folder} en la ruta {target}')

    # Lee los módulos actualizados de .cambios.cvs y los copia a las rutas de destino
    for target in target_paths:
        with open(repo_paths.get(target) + '.cambios.cvs', 'r') as open_file:
            updated_modules = open_file.readlines()
        for module in updated_modules:
            comma_index = module.index(':')
            origin_path = os.path.join(repo_paths.get(target), module.replace('\n','')[0:comma_index])
            target_path = os.path.join(target_paths.get(target), module.replace('\n','')[0:comma_index])
            if os.path.isdir(target_path):
                shutil.rmtree(target_path)
            shutil.copytree(origin_path, target_path)
            shutil.rmtree(target_path + '/.git')
            print(f"Se ha actualizado el módulo {module} en la ruta {target_paths.get(target)}.")

        # Escribe un registro de los módulos actualizados en seguimiento.txt
        with open(target_paths.get(target) + 'seguimiento.txt', 'w') as write_file:
            updated_modules.insert(0, '--- Módulos actualizados ---\n\n')
            updated_modules.append(f"\n\nHora actualización: {datetime.datetime.now()}")
            write_file.writelines(updated_modules)

    print("Todo el contenido ha sido movido.")
