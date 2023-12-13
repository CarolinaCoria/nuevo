from Alumno import AlumnoArgentino
from Alumno import AlumnoItaliano


def main():
    alvarez: AlumnoArgentino = AlumnoArgentino(nombre="Lionel")

    print(alvarez)
    alvarez.get_nombre()

    rossi: AlumnoItaliano = AlumnoItaliano(nombre="Francesca")
    rossi.get_nombre()


if __name__ == "__main__":
    main()
