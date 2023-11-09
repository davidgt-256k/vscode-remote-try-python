import random
import time


class JuegoPiedraPapelTijeras:
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijeras"]
        self.puntaje = 0

    def obtener_eleccion(self):
        while True:
            eleccion = input("Elige piedra, papel o tijeras: ").lower()
            if eleccion in self.opciones:
                return eleccion
            else:
                print("Opción no válida. Introduce piedra, papel o tijeras.")

    def determinar_resultado(self, jugador, oponente):
        reglas = {
            "piedra": {"tijeras": "Ganaste", "papel": "Perdiste"},
            "papel": {"piedra": "Ganaste", "tijeras": "Perdiste"},
            "tijeras": {"papel": "Ganaste", "piedra": "Perdiste"},
        }
        if jugador == oponente:
            return "Empate"
        return reglas[jugador].get(oponente, "Ganaste")

    def mostrar_animacion(self, eleccion_jugador, eleccion_oponente):
        print("Preparando el resultado...")
        time.sleep(1)
        print(f"Tú elegiste: {eleccion_jugador}")
        time.sleep(1)
        print(f"El oponente eligió: {eleccion_oponente}")
        time.sleep(1)

    def jugar(self):
        print("Bienvenido al juego de piedra, papel o tijeras.")

        while True:
            eleccion_jugador = self.obtener_eleccion()
            eleccion_oponente = random.choice(self.opciones)

            self.mostrar_animacion(eleccion_jugador, eleccion_oponente)

            resultado = self.determinar_resultado(eleccion_jugador, eleccion_oponente)
            print(resultado)

            if resultado == "Ganaste":
                self.puntaje += 1
            elif resultado == "Perdiste":
                self.puntaje -= 1

            print(f"Puntaje actual: {self.puntaje}")

            jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if jugar_nuevamente != "s":
                print("¡Gracias por jugar!")
                break


if __name__ == "__main__":
    juego = JuegoPiedraPapelTijeras()
    juego.jugar()
