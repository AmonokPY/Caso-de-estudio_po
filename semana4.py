"Este programa se basa en la funcion de administrar ciertas cuentas para saber la cantidad de gastos y ganancias"


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

    def show_inventory(self):  # Mostrar inventario
        print("Inventario actual:")
        for key, value in self.__inventory.items():
            print(f"Producto: {key}, Valor: {value}")

    def addition_inventory(self):
        return sum(self.__inventory.values())

    # Getter and Setter for __inventory
    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, inventory):
        self.__inventory = inventory


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
        print("Número de empleados actuales:")
        for key, value in self.__employees.items():
            print(f"Empleado: {key}, Valor: {value}")

    def addition_salary(self):
        return sum(self.__employees.values())

    # Getter and Setter for __employees
    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        self.__employees = employees

    # Getter and Setter for __num_employees
    @property
    def num_employees(self):
        return self.__num_employees

    @num_employees.setter
    def num_employees(self, num_employees):
        self.__num_employees = num_employees

    # Getter and Setter for __num_types_employees
    @property
    def num_types_employees(self):
        return self.__num_types_employees

    @num_types_employees.setter
    def num_types_employees(self, num_types_employees):
        self.__num_types_employees = num_types_employees


class Administration(Products, Employees):
    def __init__(self, num_employees: int, num_types_employees: int, name: str):
        Products.__init__(self)
        Employees.__init__(self, num_employees, num_types_employees)
        self.__name = name
        self.__sales = 0  # Para registrar las ventas

    def add_sales(self):
        while True:
            try:
                self.__sales = float(input("Digite el monto total de ventas: "))
                break
            except ValueError:
                print("Digite un número válido para el monto de ventas.")

    def calculate_profit(self):
        total_expenses = self.addition_inventory() + self.addition_salary()
        profit = self.__sales - total_expenses
        return profit

    def show_summary(self):
        print(f"Nombre de la Administración: {self.__name}")
        self.show_inventory()
        self.show_employees()
        print(f"Total Ventas: {self.__sales}")
        print(f"Total Gastos: {self.addition_inventory() + self.addition_salary()}")
        print(f"Ganancia: {self.calculate_profit()}")

    # Getter and Setter for __name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Getter and Setter for __sales
    @property
    def sales(self):
        return self.__sales

    @sales.setter
    def sales(self, sales):
        self.__sales = sales


# Crear una instancia de la clase Administration y ejecutar los métodos
admin = Administration(4, 2, "Mi Empresa")
admin.add_inventory()
admin.salario()
admin.add_sales()
admin.show_summary()
