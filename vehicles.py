class Vehiculo:
    _nombre: str
    _capacidad: int
    _vel_max: float  # Velocidad maxima
    _en_movimiento: bool

    def __init__(self, nombre: str, capacidad: int, vel_max: float) -> None:
        self._nombre = nombre
        self._capacidad = capacidad
        self._vel_max = vel_max
        self._en_movimiento = False  # El carro no se mueve al inicio

    @property
    def nombre(self):
        return self._nombre

    def mover(self):
        print("Run run")

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def vel_max(self):
        return self._vel_max

    @property
    def en_movimiento(self):
        return self._en_movimiento

    @en_movimiento.setter
    def en_movimiento(self, moviendose: bool):
        self.en_movimiento = moviendose


class Coche(Vehiculo):
    _marca: str

    def __init__(self, nombre: str, marca: str, vel_max: float) -> None:
        super().__init__(nombre, 4, vel_max)
        self._marca = marca

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca: str):
        self._marca = marca


class Bus(Vehiculo):
    def __init__(self, nombre: str, vel_max: float) -> None:
        super().__init__(nombre, 10, vel_max)


class VehiculoAereo(Vehiculo):
    _ubicacion: str
    _destino: str

    def __init__(
        self,
        nombre: str,
        ubicacion: str,
        destino: str,
        capacidad: int,
        vel_max: float,
    ) -> None:
        super().__init__(nombre, capacidad, vel_max)
        self._ubicacion = ubicacion
        self._destino = destino

    @property
    def ubicacion(self):
        return self._ubicacion

    @property
    def destino(self):
        return self._destino

    @destino.setter
    def destino(self, destino: str):
        self._destino = destino


class VehiculoAcuatico(Vehiculo):
    _profundidad: int

    def __init__(
        self, profundidad: int, nombre: str, capacidad: int, vel_max: float
    ) -> None:
        super().__init__(nombre, capacidad, vel_max)
        self._profundidad = profundidad

    @property
    def profundidad(self):
        return self.profundidad

    @profundidad.setter
    def profundidad(self, nueva_profundidad: int):
        self._profundidad = nueva_profundidad

    def sumergirse(self):
        print(f"Glu glu a {self._profundidad} metros")


class Avion(VehiculoAereo):
    _aerolinea: str

    def __init__(
        self,
        nombre: str,
        ubicacion: str,
        destino: str,
        capacidad: int,
        vel_max: float,
        aerolinea: str,
    ) -> None:
        super().__init__(nombre, ubicacion, destino, capacidad, vel_max)
        self._aerolinea = aerolinea

    def despegar(self):
        print(f"Despegando con destino a {self._destino}, desde {self._ubicacion}")

    @property
    def aerolinea(self):
        return self._aerolinea


class Helicoptero(VehiculoAereo):
    def __init__(
        self, nombre: str, ubicacion: str, destino: str, capacidad: int, vel_max: float
    ) -> None:
        super().__init__(nombre, ubicacion, destino, capacidad, vel_max)

    def atacar(self):
        print("Boom boom, muerte muerte")


class HidroAvion(Avion, VehiculoAcuatico):
    def __init__(
        self,
        nombre: str,
        ubicacion: str,
        destino: str,
        capacidad: int,
        vel_max: float,
        aerolinea: str,
    ) -> None:
        super().__init__(nombre, ubicacion, destino, capacidad, vel_max, aerolinea)

    def volar_en_el_agua(self):
        print(f"flu flu glu glu {self.profundidad} \n aerolinea : {self.aerolinea}")


class AutobusAnfibio(Bus, VehiculoAcuatico):
    def __init__(self, nombre: str, vel_max: float, profundidad: int) -> None:
        super().__init__(nombre, vel_max)

    def rodar_en_el_agua(self):
        print(f"run run glu glu {self._profundidad}")
