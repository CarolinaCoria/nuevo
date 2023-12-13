import random

def generate_australian_email(name):
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"]
    random_domain = random.choice(domains)
    return f"{name.lower()}_{random.randint(100, 999)}@{random_domain}"

_names:list = [
    "Liam", "Olivia", "Noah", "Charlotte", "Ava", "William", "Mia", "Isla", "James", "Grace"
    ]

_dni:list = [random.randint(50_000_000, 99_000_000) for _ in range(100)]

def create_user(nombre:str = None, email:str = None, dni:int = None) -> dict:
    """
    Crea un diccionario representando un usuario con información opcional.

    Parámetros:
    - nombre (str): Nombre del usuario.
    - email (str): Dirección de correo electrónico del usuario.
    - dni (int): Número de Documento Nacional de Identidad del usuario.

    Retorna:
    dict: Un diccionario con la información del usuario. Si se proporciona
          al menos uno de los parámetros como None, se generará aleatoriamente
          el valor correspondiente.

    Ejemplos:
    >>> create_user("Juan", "juan@example.com", 12345678)
    {'nombre': 'Juan', 'email': 'juan@example.com', 'dni': 12345678}

    >>> create_user()
    {'nombre': 'NombreAleatorio', 'email': 'EmailAleatorio', 'dni': DNIaleatorio}
    """
    if nombre is None and email is None and dni is None:
        nombre_random:str = random.choice(_names)
        return {
            "nombre": nombre_random,
            "email": generate_australian_email(nombre_random),
            "dni": random.choice(_dni)
        }
    return {
        "nombre": nombre,
        "email": email,
        "dni": dni
    }

def create_database(cant_user:int = 10):
    """
    Crea una base de datos simulada con usuarios generados aleatoriamente.

    Parámetros:
    - cant_user (int): Número de usuarios a generar y agregar a la base de datos.
                      El valor predeterminado es 10.

    Retorna:
    list: Una lista que contiene diccionarios representando usuarios. Cada usuario
          es generado mediante la función create_user().

    Ejemplo:
    >>> create_database(5)
    [{'nombre': 'NombreAleatorio1', 'email': 'EmailAleatorio1@example.com', 'dni': DNIaleatorio1},
     {'nombre': 'NombreAleatorio2', 'email': 'EmailAleatorio2@example.com', 'dni': DNIaleatorio2},
     {'nombre': 'NombreAleatorio3', 'email': 'EmailAleatorio3@example.com', 'dni': DNIaleatorio3},
     {'nombre': 'NombreAleatorio4', 'email': 'EmailAleatorio4@example.com', 'dni': DNIaleatorio4},
     {'nombre': 'NombreAleatorio5', 'email': 'EmailAleatorio5@example.com', 'dni': DNIaleatorio5}]
    """
    return [
        create_user()
        for _ in range(cant_user)
    ]