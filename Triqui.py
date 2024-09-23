import datetime
import random

# Clase Juego usando Programación Orientada a Objetos (POO)
class JuegoPiedraPapelTijera:
    def __init__(self):
        self.opciones = ["Piedra", "Papel", "Tijera"]
        self.resultados = {"Jugador": 0, "Computadora": 0}
        self.iniciar_juego()
    
    def bienvenida(self):
        hora_actual = datetime.datetime.now().minute
        if hora_actual % 2 == 0:
            print("Bienvenido a triqui")
        else:
            print("Combate mortal de triqui, ¡Bienvenido!")
    
    def jugar_ronda(self):
        eleccion_jugador = input("Elige Piedra, Papel o Tijera: ").capitalize().strip()
        if eleccion_jugador not in self.opciones:
            print("Elección inválida. Inténtalo de nuevo.")
            return self.jugar_ronda()  # Recursividad para pedir una elección válida

        eleccion_computadora = random.choice(self.opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_jugador == eleccion_computadora:
            print("Es un empate!")
        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
             (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel"):
            print(f"Ganas esta ronda!")
            self.resultados["Jugador"] += 1
        else:
            print(f"Pierdes esta ronda.")
            self.resultados["Computadora"] += 1
    
    def mostrar_iniciales(self, texto):
        return "".join([parte[0] for parte in texto.split()]).upper()

    def resumen(self):
        print("\nResumen del juego:")
        for clave, valor in self.resultados.items():
            iniciales = self.mostrar_iniciales(clave)
            print(f"{iniciales}: {valor}")

    def iniciar_juego(self):
        self.bienvenida()
        while True:
            self.jugar_ronda()
            continuar = input("¿Quieres jugar otra ronda? (sí/no): ").lower().strip()
            if continuar != "sí":
                break
        self.resumen()

# Ejecutar el juego
if __name__ == "__main__":
    JuegoPiedraPapelTijera()
