# Clase que representa un reproductor de MP3
class ReproductorMp3:
    # Método constructor (inicializador) que recibe el nombre de la canción
    def __init__(self, nombreCancion):
        # Atributo privado para almacenar el nombre de la canción (Encapsulamiento)
        self.__nombreCancion = nombreCancion

    # Método público para reproducir música
    def reproducirMusica(self):
        # Accede al atributo privado para imprimir un mensaje
        print(f"La canción {self.__nombreCancion} se está reproduciendo.")

# Clase que representa una calculadora básica
class Calculadora:
    # Método constructor que recibe dos números para las operaciones
    def __init__(self, num1, num2):
        # Atributos privados para almacenar los números (Encapsulamiento)
        self.__num1 = num1
        self.__num2 = num2

    # Método público para sumar los dos números
    def sumar(self):
        print(f"{self.__num1} + {self.__num2} = {self.__num1 + self.__num2}")

    # Método público para restar los dos números
    def resta(self):
        print(f"{self.__num1} - {self.__num2} = {self.__num1 - self.__num2}")

# Clase que representa un celular, heredando de Calculadora y ReproductorMp3 (Herencia Múltiple)
class Celular(Calculadora, ReproductorMp3):
    # Método constructor que inicializa la marca del celular, la canción, y los números
    def __init__(self, marca, nombreCancion, num1, num2):
        # Inicializa los atributos de las clases padre (Calculadora y ReproductorMp3) (Sobrecarga de Constructor)
        ReproductorMp3.__init__(self, nombreCancion)
        Calculadora.__init__(self, num1, num2)
        # Atributo privado para almacenar la marca del celular (Encapsulamiento)
        self.__marca = marca

    # Método público para realizar una llamada
    def hacerLlamada(self, numeroCelular):
        print(f"Llamando a {numeroCelular}")

# Creación de un objeto de la clase Celular (Instanciación de la Clase Celular)
celular1 = Celular("Apple", "No more tears", 5, 8)

# Llamada al método hacerLlamada (Uso de un método propio de Celular)
celular1.hacerLlamada(3115113355)

# Llamada al método sumar heredado de la clase Calculadora (Polimorfismo)
celular1.sumar()

# Llamada al método reproducirMusica heredado de la clase ReproductorMp3 (Polimorfismo)
celular1.reproducirMusica()