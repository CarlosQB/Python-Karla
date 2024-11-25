def challenging_hike():
    # Imprime un mensaje de inicio de la función
    print("\n--- Challenging Hike ---")

    # Solicita al usuario el número de puntos de referencia en la montaña
    N = int(input("¿Cuántos puntos de referencia hay en la montaña? "))  # Número de puntos de referencia

    # Pide al usuario ingresar las conexiones entre los puntos de referencia
    # Estos valores podrían representar algún tipo de conexión o ruta entre los puntos
    print("Ingresa las conexiones entre los puntos de referencia (separadas por espacios):")
    paths = list(map(int, input().split()))  # Convierte la entrada a una lista de enteros (conexiones entre los puntos)

    # Pide al usuario ingresar los valores de likes para cada punto de referencia
    print("Ingresa los valores de likes esperados para cada punto de referencia (separados por espacios):")
    likes = list(map(int, input().split()))  # Convierte la entrada a una lista de enteros (likes de cada punto)

    # Inicializa una lista llamada max_photos con ceros para cada punto de referencia
    max_photos = [0] * N  # Esta lista almacenará el máximo número de fotos que se pueden tomar hasta cada punto

    # Rellena la lista max_photos con los likes de cada punto como el valor inicial
    for i in range(N):
        max_photos[i] = likes[i]  # Inicialmente, el máximo número de fotos en el punto i es igual al número de likes de ese punto

        # Compara el punto actual (i) con todos los puntos anteriores (j) para ver si se puede tomar más fotos
        for j in range(i):
            # Verifica si la conexión entre los puntos cumple con los requisitos de la caminata desafiante
            if paths[j] < paths[i] and max_photos[i] < max_photos[j] + likes[i]:
                # Si es posible tomar más fotos al llegar al punto i, actualiza el valor en max_photos[i]
                max_photos[i] = max_photos[j] + likes[i]

    # Muestra el máximo número de fotos que se pueden tomar en cada punto de referencia
    print("El máximo número de fotos para cada punto es:")
    # Convierte la lista max_photos a cadenas de texto y las imprime separadas por espacios
    print(" ".join(map(str, max_photos)), "\n")
