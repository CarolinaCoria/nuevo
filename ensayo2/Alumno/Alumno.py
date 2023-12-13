def nombre_alumno(nombre,cls):
    if nombre:
        return nombre
    
    cls.nombre_alumno:str = input("Ingrese el nombre del alumno\n")



class Alumno:
    # Atributos de clase
    _tipo_alumno:str = "anual"

    def __init__(self,**kwargs):
        print(kwargs)
        self.cursos:int = kwargs["cursos"]
        self.apellido:str = kwargs["apellido"]
        self.ciudad:str = kwargs["ciudad"]
        self.nombre_alumno:str = kwargs.get("nombre_alumno",None)

        self.__nombramiento()
    
    def __nombramiento(self):
        nombre_alumno(self.nombre_alumno, self)
    
    #Métodos
    def cantidad_cursos(self):
        print(f"El alumno tiene {self.cursos} cursos")

    def __str__(self):
        return f"""
        >>>   El {self._tipo_alumno}:
        >>>     Nombre: {self.nombre_alumno}
        >>>     Apellido: {self.apellido}
        >>>     Cantidad de cursos: {self.cursos}
        >>>     Ciudad: {self.ciudad}
    """

    def to_string(self):
        return f"""
        >>>   El {self._tipo_alumno}:
        >>>     Nombre: {self.nombre_alumno}
        >>>     Apellido: {self.apellido}
        >>>     Cantidad de cursos: {self.cursos}
        >>>     Ciudad: {self.ciudad}
        {'_'*50}
    """