from Alumno import Alumno
from Alumno import Manager  


def main():

    benito:Alumno = Alumno(
        cursos = 2,
        apellido = "Pereyra",
        ciudad = "Parque San Martín"
    )


    veronica:Alumno = Alumno(
        cursos = 1,
        apellido = "Salas",
        ciudad = "Quito"
    )

    local_database:Manager = Manager()

    local_database.insertar_alumno(benito)
    local_database.insertar_alumno(veronica)

    local_database.mostrar_alumnos()
    local_database.save_alumnos()



if __name__ == '__main__':
    main()
