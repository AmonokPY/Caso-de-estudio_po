# Capa de Datos
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "✔" if self.completed else "✘"
        return f"{status} {self.description}"

# Capa de Lógica

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        new_task = Task(task_description)
        self.tasks.append(new_task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True

    def list_tasks(self):
        if not self.tasks:
            print("No hay tareas.")
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")

# Capa de Presentación
class TaskApp:
    def __init__(self):
        self.manager = TaskManager()

    def run(self):
        while True:
            print("\n1. Agregar tarea")
            print("2. Completar tarea")
            print("3. Eliminar tarea")
            print("4. Ver todas las tareas")
            print("5. Editar tarea")
            print("6. Salir")
            choice = input("\nSelecciona una opción: ")

            if choice == "1":
                task_desc = input("Descripción de la tarea: ")
                self.manager.add_task(task_desc)
            elif choice == "2":
                task_index = int(input("Índice de la tarea a completar: "))
                self.manager.complete_task(task_index)
            elif choice == "3":
                task_index = int(input("Índice de la tarea a eliminar: "))
                self.manager.remove_task(task_index)
            elif choice == "4":
                self.manager.list_tasks()
            elif choice == "5":
                task_index = int(input("Índice de la tarea a editar: "))
                if 0 <= task_index < len(self.manager.tasks):
                    new_description = input("Nueva descripción de la tarea: ")
                    self.manager.tasks[task_index].description = new_description
                else:
                    print("Índice de tarea no válido.")
            elif choice == "6":
                print("Saliendo de la aplicación.")
                break
            else:
                print("Opción no válida.")

# Ejecución
if __name__ == "__main__":
    app = TaskApp()
    app.run()
