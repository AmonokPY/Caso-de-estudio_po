# Caso de estudio
from abc import ABC, abstractmethod


class Poligono(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class Triangulo(Poligono):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagono(Poligono):
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagono(Poligono):
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilatero(Poligono):
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangulo()
R.noofsides()

K = Quadrilatero()
K.noofsides()

R = Pentagono()
R.noofsides()

K = Hexagono()
K.noofsides()
