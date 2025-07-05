import random

def obtener_eleccion_usuario():
    print("Elige una opción: ")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = input("Ingresa el número de tu elección: ")
    if opcion == "1":
        return "piedra"
    elif opcion == "2":
        return "papel"
    elif opcion == "3":
        return "tijera"
    else:
        return None

def obtener_eleccion_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or  (usuario == "papel" and computadora == "piedra") or (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Pendejo XDD"

def jugar():
    print("=== Juego: Piedra, Papel o Tijera ===")
    rondas = 3
    for ronda in range(1, rondas + 1):
        print(f"\nRonda {ronda}")
        usuario = obtener_eleccion_usuario()
        if usuario is None:
            print("Opción inválida. Pierdes esta ronda.")
            continue
        computadora = obtener_eleccion_computadora()
        print(f"Tú elegiste: {usuario}")
        print(f"La computadora eligió: {computadora}")
        resultado = determinar_ganador(usuario, computadora)
        print(resultado)

jugar()