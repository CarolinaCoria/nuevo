from .AbstractAlumno import Alumno


class AlumnoArgentino(Alumno):
    def __init__(self, **kwargs):
        self.nombre: str = kwargs.get("nombre", "no_definido")
        self.cant_cursos: int = kwargs.get("cant_cursos", 0)
        self.edad: int = kwargs.get("edad", 17)
        self.nacionalidad: str = kwargs.get("nacionalidad", "argentino")

    def __str__(self):
        return f"""
        Soy un alumno {self.nacionalidad}
        Mi nombre es: {self.nombre}
    """

    def get_nombre(self):
        print(f"Soy Alumno {self.nacionalidad}, mi nombre es {self.nombre}")

    def get_nacionalidad(self):
        pass


class AlumnoItaliano(Alumno):
    def __init__(self, **kwargs):
        self.nombre: str = kwargs.get("nombre", "no_definido")

    def get_nombre(self):
        respuesta: str = f"Sono uno studente italiano, mi chiamo {self.nombre}."
        print(respuesta)

    def get_nacionalidad(self):
        pass
