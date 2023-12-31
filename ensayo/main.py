# -------------- functions

# def greeting(nombre:str) -> None:
#     print (f"Hola, {nombre}")
#     return None
# nombre:str = input("ingresa tu nombre: \n")

# greeting( nombre )

# CRUD
"""

database (crear un usuario | muchos usuarios)
- ingreso la operación del CRUD
- controllers : lógica del negocio
-qué paso hacer después?

"""

from database import create_database
from controllers import delete_user
from controllers import read_users
from controllers import create_user
from controllers import update_user

db_user: list[dict] = create_database()

print(db_user)

def main():
    print("gracias por usar nuestro gestor de usuarios")
    choice_crud:str = input("""
    Ingrese la opción de operación que quiere hacer
    Opciones :   
        - a para leer
        - b para crear
        - c para editar   
        - d para borrar      
    """)

    if choice_crud == "a":
        _dni:str = input("dni del usuario:\n")
        read_users(int(_dni),db_user)
        return
    if choice_crud == "b":
        _dni:str = input("dni del usuario:\n")
        create_user(int(_dni),db_user)
        print(db_user)
        return
    if choice_crud == "c":
        _dni:int = int(input("dni del usuario:\n"))
        update_user(_dni,db_user)
        print(db_user)
        return

    if choice_crud == "d":
        _dni:str = input("dni del usuario:\n")
        print(len(db_user))
        delete_user(int(_dni),db_user)
        print(len(db_user))

main()
    