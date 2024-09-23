class Products:
    def __init__(self):
        self.__key: str = ""  # Nombre del producto
        self.__value: int = 0  # Valor del producto
        self.__inventory = {}  # Diccionario para almacenar el inventario

    def add_inventory(self):
        print(
            '----Digite primero el nombre del producto y después el valor, para salir digite "termine"----'
        )
        while True:
            self.__key = input("Digite el nombre del producto: ")
            if self.__key.lower() == "termine":  # Salir si el usuario escribe "termine"
                break
            while True:
                try:
                    self.__value = int(
                        input("Digite el valor del producto, sin comas: ")
                    )
                    break
                except ValueError:
                    print(
                        "Valor erróneo. Por favor, ingrese un número entero sin comas."
                    )

            # Agregar el producto y su valor al diccionario de inventario
            self.__inventory[self.__key] = self.__value

    def show_inventory(self):  # mostrar inventario
        print("Inventario actual:")
        for key, value in self.__inventory.items():
            print(f"Producto: {key},Valor: {value}")

    def addition_inventory(self):
        return sum(self.__inventory.values())


class Employees:
    def __init__(self, num_employees: int, num_types_employees: int):
        self.__num_employees = num_employees
        self.__num_types_employees = num_types_employees
        self.__employees = {}

    def salario(self):
        for i in range(1, self.__num_types_employees + 1):
            while True:
                try:
                    salario = float(
                        input(f"Digite el salario del tipo de empleado #{i}: ")
                    )
                    break
                except ValueError:
                    print("Digite un número válido para el salario.")

            while True:
                try:
                    num = int(input("Digite el número de empleados con ese salario: "))
                    break
                except ValueError:
                    print("Digite un número válido para el número de empleados.")

            # Agregar la clave y valor al diccionario, repitiéndolo según el número de empleados
            for j in range(num):
                self.__employees[f"empleado {i}_{j + 1}"] = salario

    def show_employees(self):  # Mostrar inventario
        print("Numero de empleados actuales:")
        for key, value in self.__employees.items():
            print(f"Empleado: {key}, Valor: {value}")

    def addition_salary(self):
        return sum(self.__employees.values())
