def repo_paths():
    """
    Devuelve las rutas de los módulos de localización desde el repositorio de GitHub.

    :return: dict
        Un diccionario donde las claves son números de versión y los valores son las rutas correspondientes a los módulos.
    """
    repo_path = {
        '14.0': '/Users/nombre_usuario/Documents/QA/Módulos/Producción/14.0/',
        '15.0': '/Users/nombre_usuario/Documents/QA/Módulos/Producción/15.0/',
        '16.0': '/Users/nombre_usuario/Documents/QA/Módulos/Producción/16.0/',
        '17.0': '/Users/nombre_usuario/Documents/QA/Módulos/Producción/17.0/',
        '18.0': '/Users/nombre_usuario/Documents/QA/Módulos/Producción/18.0/'
    }

    return repo_path


def target_paths():
    """
    Devuelve las rutas de los módulos de localización actualizados listos para ser cargados en los entornos de QA.

    :return: dict
        Un diccionario donde las claves son números de versión y los valores son las rutas correspondientes a los módulos actualizados.
    """
    target_path = {
        '14.0': '/Users/nombre_usuario/Documents/QA/Módulos/SH/Carga_14.0/',
        '15.0': '/Users/nombre_usuario/Documents/QA/Módulos/SH/Carga_15.0/',
        '16.0': '/Users/nombre_usuario/Documents/QA/Módulos/SH/Carga_16.0/',
        '17.0': '/Users/nombre_usuario/Documents/QA/Módulos/SH/Carga_17.0/',
        '18.0': '/Users/nombre_usuario/Documents/QA/Módulos/SH/Carga_18.0/'
    }

    return target_path

def version_move_paths():
    """
    Devuelve las rutas de los módulos de localización para mover versiones específicas que usan WSL.

    :return: dict
        Un diccionario donde las claves son números de versión y los valores son las rutas correspondientes a los módulos.
    """
    version_path = {
        '14.0': '/Users/nombre_usuario/Documents/QA/Módulos/WSL/WSL_14.0/',
        '15.0': '/Users/nombre_usuario/Documents/QA/Módulos/WSL/WSL_15.0/',
        '16.0': '/Users/nombre_usuario/Documents/QA/Módulos/WSL/WSL_16.0/', # No se necesita mover la versión 16.0
        '17.0': '/Users/nombre_usuario/Documents/QA/Módulos/WSL/WSL_17.0/', # No se necesita mover la versión 17.0
        '18.0': '/Users/nombre_usuario/Documents/QA/Módulos/WSL/WSL_18.0/', # No se necesita mover la versión 18.0
    }

    return version_path

def available_modules_list():
    """
    Devuelve una lista de módulos de localización disponibles en el repositorio de GitHub.

    :return: list
        Una lista de nombres de módulos disponibles en el repositorio.
    """
    modules_list = [
        'nombre_modulo_1',
        'nombre_modulo_2',
        'nombre_modulo_3',
    ]

    return modules_list
