from .tools import check_db

def delete_user(dni:int,db_user:list=None) ->None:
    """
    Elimina un usuario de la base de datos según su número de Documento Nacional de Identidad (DNI).

    Parámetros:
    - dni (int): Número de Documento Nacional de Identidad del usuario a eliminar.
    - db_user (list): Lista que representa la base de datos de usuarios.
    Cada usuario en la lista debe ser
    un diccionario que contenga al menos la clave 'dni'.
    Si no se proporciona, se asume una lista vacía.

    Retorna:
    None: La función no retorna ningún valor explícito.
    Modifica la lista `db_user` eliminando el usuario con el DNI proporcionado.

    Nota:
    La función utiliza la función `check_db`
    para verificar la validez de la base de datos antes de realizar la eliminación.
    Si la base de datos no es válida, la función retorna None sin realizar cambios.

    Ejemplo:
    >>> usuarios = [{'dni': 12345678, 'nombre': 'Juan'}, {'dni': 98765432, 'nombre': 'Ana'}]
    >>> delete_user(12345678, usuarios)
    >>> print(usuarios)
    [{'dni': 98765432, 'nombre': 'Ana'}]
    """
    if not check_db(db_user):
        return None

    # return [
    #     user
    #     for user in db_user
    #     if user["dni"] == dni
    # ]

    for index,user in enumerate(db_user):
        if user["dni"] == dni:
            db_user.pop(index)