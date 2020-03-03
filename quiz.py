
texto = "Bienvenido al test del queso"
print("\n" + texto + "\n" + "-" * len(texto) + "\n")

puntuacion = 0

opcion = input("Que haces cuando ves una tabla de quesos?\n"
               "A - Salgo corriendo\n"
               "B - Pruebo uno de los quesos o incluso varios\n"
               "C - No puedo evitar devorarla\n"
               "(A/B/C): ").upper()

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A B y C")
    exit()

opcion = input("Como te gusta la hamburguesa?\n"
               "A - Sin queso\n"
               "B - Con queso\n"
               "C - Pan y queso\n"
               "(A/B/C): ").upper()

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10

opcion = input("Eres intolerante a la lactosa?\n"
               "A - Si\n"
               "B - A veces\n"
               "C - No\n"
               "(A/B/C): ").upper()

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10

if puntuacion >= 25:
    print("Te encanta el queso")
elif puntuacion >= 15 and puntuacion < 25:
    print("Te gusta el queso")
else:
    print("No te gusta el queso")