import itertools

def calcular_puntuacion(jugador):
    return sum(jugador[1:])

def generar_combinaciones(jugadores):
    mejor_diferencia = float('inf')
    equipos_balanceados = None

    for combinacion in itertools.combinations(jugadores, len(jugadores) // 2):
        equipo1 = list(combinacion)
        equipo2 = [j for j in jugadores if j not in equipo1]

        puntuacion_equipo1 = sum(calcular_puntuacion(jugador) for jugador in equipo1)
        puntuacion_equipo2 = sum(calcular_puntuacion(jugador) for jugador in equipo2)

        diferencia = abs(puntuacion_equipo1 - puntuacion_equipo2)
        if diferencia < mejor_diferencia:
            mejor_diferencia = diferencia
            equipos_balanceados = (equipo1, equipo2)

    return equipos_balanceados

def main():
    jugadores = [
        ('walter', 8.5, 8, 9.5),
        ('ivan', 8.5, 9.5, 8),
        ('Fabri', 6.5, 5, 7.5),
        ('Fabro 2.0', 6, 6.5, 6),
        ('Gabo', 7.5,7.5,7.5),
        ('Gabi', 7,7.5,6),
        ('Joaco', 6.5, 6, 6),
        ('Matias', 5, 6, 4),
        ('Seba', 7, 8, 5),
        ('Johan', 5, 5, 4),
        ('benja', 5,6,6),
        ('Augusto', 7, 7.5, 8),
        ('Alexis', 9, 8.5, 9),
        ('Fede', 8,8,8)
    ]

    equipo1, equipo2 = generar_combinaciones(jugadores)

    # Mostrar los equipos balanceados
    print("Equipo 1:")
    for i, jugador in enumerate(equipo1, 1):
        print(f"{jugador[0]}: Nivel {jugador[1]}, Condición {jugador[2]}, Experiencia {jugador[3]}")

    print("\nEquipo 2:")
    for i, jugador in enumerate(equipo2, 1):
        print(f"{jugador[0]}: Nivel {jugador[1]}, Condición {jugador[2]}, Experiencia {jugador[3]}")

if __name__ == "__main__":
    main()