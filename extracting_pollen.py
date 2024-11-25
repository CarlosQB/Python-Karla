def extracting_pollen():
    # Imprime un mensaje de inicio de la función
    print("\n--- Extracting Pollen ---")

    # Solicita al usuario el número de flores y la posición de Gertrude en la fila
    N = int(input("Ingresa el número de flores : "))  # Número total de flores
    K = int(input("Ingresa la posición de Gertrude en la fila : "))  # Posición de Gertrude (cuántas abejas antes que ella)
    
    # Pide al usuario ingresar la cantidad de polen en cada flor como una lista de enteros
    print("Ingresa la cantidad de polen en cada flor, separada por espacios:")
    flowers = list(map(int, input().split()))  # Convierte la entrada en una lista de enteros

    # Función auxiliar que recibe un número y devuelve la suma de sus dígitos
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))  # Convierte el número a cadena, recorre sus dígitos y los suma

    # Simula las abejas que recolectan polen antes que Gertrude
    for _ in range(K - 1):  # Repite el proceso K-1 veces, ya que Gertrude es la K-ésima abeja
        max_pollen_index = flowers.index(max(flowers))  # Encuentra el índice de la flor con más polen
        if flowers[max_pollen_index] > 0:  # Si la flor tiene polen (es mayor que 0)
            # Resta el valor de los dígitos del polen de esa flor
            flowers[max_pollen_index] -= sum_of_digits(flowers[max_pollen_index])

    # Ahora es el turno de Gertrude
    max_pollen_index = flowers.index(max(flowers))  # Encuentra la flor con más polen en el turno de Gertrude
    
    # Si la flor tiene polen, Gertrude recolecta la suma de sus dígitos, sino recoge 0
    gertrude_pollen = sum_of_digits(flowers[max_pollen_index]) if flowers[max_pollen_index] > 0 else 0

    # Imprime el resultado: cuántos granos de polen recolectará Gertrude
    print(f"Gertrude recolectará {gertrude_pollen} granos de polen.\n")
