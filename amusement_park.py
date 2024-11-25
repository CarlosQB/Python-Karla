def amusement_park():
    # Imprime un mensaje de inicio de la función
    print("\n--- Amusement Park Adventure ---")

    # Solicita al usuario el número de juegos en el parque
    N = int(input("¿Cuántos juegos hay en el parque? "))  # Número de juegos disponibles en el parque

    # Solicita al usuario su altura en centímetros
    H = int(input("¿Cuál es tu altura en centimetros? "))  # Altura del usuario en centímetros

    # Pide al usuario ingresar las alturas mínimas requeridas para cada juego
    print("Ingresa las alturas mínimas requeridas para cada juego, separadas por espacios:")
    min_heights = list(map(int, input().split()))  # Convierte la entrada a una lista de enteros (las alturas mínimas para cada juego)

    # Calcula cuántos juegos puede disfrutar el usuario en función de su altura
    rides_count = sum(1 for height in min_heights if H >= height)  # Cuenta los juegos donde la altura del usuario es suficiente

    # Imprime cuántos juegos puede disfrutar el usuario
    print(f"Puedes subirte a {rides_count} juegos.\n")
