# Herencia de clase abstracta
from abc import ABC, abstractclassmethod


class Alumno(ABC):
    @abstractclassmethod
    def get_nombre(self):
        ...

    @abstractclassmethod
    def get_nacionalidad(self):
        pass
