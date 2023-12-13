from .Alumno import Alumno

class Manager:
    def __init__(self, **kwargs)->None:
        self.db:list[Alumno] = kwargs.get("db", [])

    def insertar_alumno(self, a:Alumno):
        self.db.append(a)
        print(f"Se agregó un alumno {a.nombre_alumno}")
    
    def mostrar_alumnos(self):
        if isinstance(self.db, list):
            for a in self.db:
                print(a.to_string())



    def save_alumnos(self):
        if isinstance(self.db, list):
            out_text:str = ''
            
            for a in self.db:
                out_text += a.to_string()

            with open("base_datos.txt", "w", encoding="latin-1") as f:
                f.write(out_text)