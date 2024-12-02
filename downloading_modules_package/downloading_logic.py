from time import sleep
import custom_paths
import subprocess
import os

def cloning_modules_from_github(repo, module):
    """
    Clona módulos desde el repositorio de GitHub.

    Args:
        repo (str): La ruta del repositorio.
        module (str): El nombre del módulo a clonar.

    La función determina la rama a clonar basada en la ruta del repositorio.
    Luego ejecuta el comando `git clone` para clonar el módulo especificado desde GitHub.
    Si la clonación es exitosa, imprime un mensaje de éxito; de lo contrario, imprime un mensaje de error.
    """
    # Determina la rama a clonar
    branch = repo[-5:-1]
    response = subprocess.run(["git", "clone", f"https://github.com/Repo_Company/{module}.git", "--branch", branch], capture_output=True, text=True)
    sleep(0.5)
    if response.returncode == 0:
        print(f'Módulo {module} descargado')
    else:
        print(f'Error al descargar módulo {module}, o no existe en el repositorio para esa rama.')


def downloading_modules_from_github():
    """
    Descarga módulos desde el repositorio de GitHub.

    La función itera sobre las rutas del repositorio y verifica si existen.
    Si una ruta del repositorio no existe, crea el directorio y clona los módulos disponibles.
    Si la ruta del repositorio ya existe, verifica los módulos faltantes y los clona si es necesario.
    """
    for repo in custom_paths.repo_paths().values():
        if not os.path.exists(repo):
            print(f'Descargando fichero versión {repo[-5:-1]}, por favor espere...')
            os.makedirs(repo)
            for module in custom_paths.available_modules_list():
                repo2 = repo
                validator_flag = (module == 'l10n_co_base' and repo[-5:-1] != '16.0')
                if validator_flag:
                    if not os.path.exists(repo + module):
                        os.makedirs(repo + module)
                    repo2 = repo + module + '/'
                    path2 = repo2 + module
                path = repo + module
                os.chdir(repo if not validator_flag else repo2)
                if not os.path.exists(path if not validator_flag else path2):
                    cloning_modules_from_github(repo, module)
            print(f'Proceso terminado. Módulos descargados.\n')
        else:
            print(f'El fichero para la versión {repo[-5:-1]} ya existe.')
            repo_list = [name for name in os.listdir(repo) if os.path.isdir(os.path.join(repo, name))]
            modules_list = custom_paths.available_modules_list()
            if len(repo_list) != len(modules_list):
                difference_set = set(modules_list) - set(repo_list)
                print(f'Falta(n) {len(difference_set)} módulo(s) por descargar')
                os.chdir(repo)
                for module in difference_set:
                    cloning_modules_from_github(repo, module)
            else:
                print('Todos los módulos de la versión ya han sido descargados.')
