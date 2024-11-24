from custom_paths import repo_paths
import subprocess
import os
import ast
import datetime


def updating_modules_from_github():
    """
        Toma las rutas prestablecidas en el módulo de repo_paths para actualizar cada módulo de la localización con
        respecto a lo que está alojado en el repositorio de Github y deja la trazabilidad en un .txt de cada uno de ellos
    """

    for repo in repo_paths().values():
        print(f'Actualizando fichero versión {repo[-5:-1]}')
        file_list = [name for name in os.listdir(repo) if os.path.isdir(os.path.join(repo, name))]
        unchanged_modules = ['--- Módulos sin actualizar ---\n', ]
        updated_modules = ['\n\n\n--- Módulos actualizados ---', ]
        updated_modules_view = []

        for file in file_list:
            file2 = file
            if file == 'l10n_co_exo':
                file2 = 'exo_config'
            path = repo + '/'.join([file, file2, '__manifest__.py'])
            if file == 'l10n_co_base':
                file = 'l10n_co_base/l10n_co_base'

            try:
                os.chdir(repo + file)
            except FileNotFoundError:
                print(f'No se encuentra el módulo {file} en la ruta {repo}')
                continue

            with open(path, 'r') as open_file:
                content = open_file.read()
            old_version = ast.literal_eval(content).get('version')

            info = subprocess.run(["git", "pull"], capture_output=True, text=True)
            if info.stdout:
                if 'Fast-forward' in info.stdout:
                    with open(path, 'r') as open_file:
                        content = open_file.read()
                    new_version = ast.literal_eval(content).get('version')
                    updated_modules.append('\n' + file + ': ' + old_version + ' ----> ' + new_version)
                    updated_modules_view.append(file + ': ' + new_version + '\n')
                    print(f'Cambios detectados: {file}')
                else:
                    unchanged_modules.append('\n' + file + ': ' + old_version)
            elif info.stderr:
                print(f'No es posible conectar al repositorio del módulo {file}.')

        write_lines = unchanged_modules + updated_modules
        total_modules = len(write_lines) - 2
        write_lines.append(f'\n\n\nTotal módulos: {total_modules}')
        write_lines.append(f"\nHora actualización: {datetime.datetime.now()}")

        with open(repo + 'cambios.txt', 'w') as write_file:
            write_file.writelines(write_lines)
        with open(repo + '.cambios.cvs', 'w') as write_file:
            write_file.writelines(updated_modules_view)

        print(f'Módulos analizados: {total_modules}\n')
