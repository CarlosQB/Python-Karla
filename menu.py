from amusement_park import amusement_park
from challenging_hike import challenging_hike
from extracting_pollen import extracting_pollen


def main_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Amusement Park Adventure")
        print("2. Challenging Hike")
        print("3. Extracting Pollen")
        print("4. Salir")
        choice = input("Selecciona una opción (1-4): ")
        if choice == "1":
            amusement_park()
        elif choice == "2":
            challenging_hike()
        elif choice == "3":
            extracting_pollen()
        elif choice == "4":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    main_menu()




            
#QuezadaBenavidesJoseCarlos