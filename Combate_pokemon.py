
pokemon_elegido = input("Cual quieres que sea tu oponente?  (Squirtle / Charmander / Bulbasaur):").upper()

vida_pickachu = 100
vida_enemigo = 0
ataque_enemigo = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    ataque_enemigo = 10

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    ataque_enemigo = 9

elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 100
    ataque_enemigo = 8

while vida_pickachu >0 and vida_enemigo >0:

    ataque_elegido = input("Que ataque quieres usar?  (Impactrueno / Cola de hierro):").upper()

    if ataque_elegido == "IMPACTRUENO":
        vida_enemigo -=10
    elif ataque_elegido == "COLA DE HIERRO":
        vida_enemigo -=12

    print("A {} le quedan {} puntos de vida".format(pokemon_elegido, vida_enemigo))

    if pokemon_elegido == "SQUIRTLE":
        print("Squirtle ha usado pistola burbuja")

    elif pokemon_elegido == "CHARMANDER":
        print("Charmander ha usado ascuas")

    elif pokemon_elegido == "BULBASAUR":
        print("Bulbasaur ha usado látigo cepa")

    vida_pickachu -= ataque_enemigo

    print("A PIKACHU le quedan {} puntos de vida".format(vida_pickachu))

print("El combate ha terminado")

if vida_pickachu > vida_enemigo:
    print("Has ganado!, bien hecho")
else:
    print("Te han vencido, mejor suerte para la próxima")




