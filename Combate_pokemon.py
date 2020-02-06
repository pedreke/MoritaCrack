print("Bienvenido a tu combate pokemon, tu aliado es pikachu, tiene 100 puntos de vida y cuenta con 2 ataques")
print("El primero es impactrueno que infringe 10 puntos de daño")
print("El segundo es cola de hierro que infringe 12 puntos de daño")

pokemon_elegido = input("Cual quieres que sea tu oponente?  (Squirtle / Charmander / Bulbasaur):").upper()

vida_pickachu = 100
vida_enemigo = 0
ataque_enemigo = 0
movimiento_enemigo = "Placaje"

if pokemon_elegido == "SQUIRTLE":
    movimiento_enemigo = "Pistola Burbuja"
    vida_enemigo = 90
    ataque_enemigo = 10
    print("Has elegido a {}, tiene {} puntos de vida y su ataque {} infringe {} puntos de daño".format(pokemon_elegido, vida_enemigo, movimiento_enemigo, ataque_enemigo))

elif pokemon_elegido == "CHARMANDER":
    movimiento_enemigo = "Ascuas"
    vida_enemigo = 80
    ataque_enemigo = 9
    print("Has elegido a {}, tiene {} puntos de vida y su ataque {} infringe {} puntos de daño".format(pokemon_elegido, vida_enemigo, movimiento_enemigo, ataque_enemigo))

elif pokemon_elegido == "BULBASAUR":
    movimiento_enemigo = "Látigo cepa"
    vida_enemigo = 100
    ataque_enemigo = 8
    print("Has elegido a {}, tiene {} puntos de vida y su ataque {} infringe {} puntos de daño".format(pokemon_elegido, vida_enemigo, movimiento_enemigo, ataque_enemigo))

while vida_pickachu >0 and vida_enemigo >0:

    ataque_elegido = input("Que ataque quieres usar?  (Impactrueno / Cola de hierro):").upper()

    if ataque_elegido == "IMPACTRUENO":
        vida_enemigo -=10
    elif ataque_elegido == "COLA DE HIERRO":
        vida_enemigo -=12

    print("A {} le quedan {} puntos de vida".format(pokemon_elegido, vida_enemigo))

    if pokemon_elegido == "SQUIRTLE" and vida_enemigo > 0:
        print("{} ha usado {}".format(pokemon_elegido, movimiento_enemigo))

    elif pokemon_elegido == "CHARMANDER" and vida_enemigo > 0:
        print("{} ha usado {}".format(pokemon_elegido, movimiento_enemigo))

    elif pokemon_elegido == "BULBASAUR" and vida_enemigo > 0:
        print("{} ha usado {}".format(pokemon_elegido, movimiento_enemigo))

    vida_pickachu -= ataque_enemigo

    print("A PIKACHU le quedan {} puntos de vida".format(vida_pickachu))

print("El combate ha terminado")

if vida_pickachu > vida_enemigo:
    print("Has ganado!, bien hecho")
else:
    print("Te han vencido, mejor suerte para la próxima")
input()



