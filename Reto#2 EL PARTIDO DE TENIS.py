"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Ventaja P1
  Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.   
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""

### MARCADOR FUNCIONAL DE TENIS CON SISTEMA DE VENTAJA E IGUALES ###


def partidoDeTenis():
    puntos_P1 = 0
    puntos_P2 = 0
    iguales = False
    ventajaP1 = False
    ventajaP2 = False
    finished = False

    puntuaciones_p1 = ["Love", 15, 30, 40, "VICTORIA P1"]
    puntuaciones_p2 = ["Love", 15, 30, 40, "VICTORIA P2"]

    print("Comienza el partido")

    while not finished:
        if puntos_P1 < 3 or puntos_P2 < 3:
            ganador_punto = input("¿Quién ha ganado el punto?")
            if ganador_punto == "P1":
                puntos_P1 += 1
            elif ganador_punto == "P2":
                puntos_P2 += 1

            print(puntuaciones_p1[puntos_P1], " - ", puntuaciones_p2[puntos_P2])

            if puntos_P1 == 4 or puntos_P2 == 4:
                print(puntuaciones_p1[-1] if puntos_P1 == 4 else puntuaciones_p2[-1])
                finished = True
        
        while (puntos_P1 == 3 and puntos_P2 == 3):
            iguales = True
            # iguales
            if iguales == True:
                ventajaP1 = False
                ventajaP1 = False
                print("IGUALES")
            ganador_punto = input("¿Quién ha ganado el punto?")
            # ventajas
            if (iguales == True and ganador_punto == "P1"):
                ventajaP1 = True
                ventajaP2 = False
                print("VENTAJA P1")
                ganador_punto = input("¿Quién ha ganado el punto?")
            elif (iguales == True and ganador_punto == "P2"):
                ventajaP2 = True
                ventajaP1 = False
                print("VENTAJA P2")
                ganador_punto = input("¿Quién ha ganado el punto?")
            # ganar por ventaja
            if (ventajaP1 and ganador_punto == "P1"):
                puntos_P1 += 1
                print("VICTORIA P1")
                finished = True
            elif (ventajaP2 and ganador_punto == "P2"):
                puntos_P2 += 1
                print("VICTORIA P2")
                finished = True

partidoDeTenis()