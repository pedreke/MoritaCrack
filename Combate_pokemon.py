print("Bienvenido a tu combate pokemon, tu aliado es pikachu, tiene 100 puntos de vida y cuenta con 2 ataques")
print("El primero es impactrueno que infringe 10 puntos de daño")
print("El segundo es cola de hierro que infringe 12 puntos de daño")
print()
pokemon_elegido = input("Cual quieres que sea tu oponente?  (Squirtle / Charmander / Bulbasaur):").upper()
print()
vida_pickachu = 100
vida_enemigo = 0
ataque_enemigo = 0
movimiento_enemigo = "Placaje"

while pokemon_elegido != "SQUIRTLE" and pokemon_elegido != "CHARMANDER" and pokemon_elegido != "BULBASAUR":
    pokemon_elegido = input("{} no es un enemigo, intentalo de nuevo:".format(pokemon_elegido)).upper()

if pokemon_elegido == "SQUIRTLE":
    movimiento_enemigo = "Pistola Burbuja"
    vida_enemigo = 90
    ataque_enemigo = 10
    print("Has elegido a {}, tiene {} puntos de vida y su ataque {} infringe {} puntos de daño".format(pokemon_elegido,
                                                                     vida_enemigo, movimiento_enemigo, ataque_enemigo))
    print()

elif pokemon_elegido == "CHARMANDER":
    movimiento_enemigo = "Ascuas"
    vida_enemigo = 80
    ataque_enemigo = 9
    print("Has elegido a {}, tiene {} puntos de vida y su ataque {} infringe {} puntos de daño".format(pokemon_elegido,
                                                                     vida_enemigo, movimiento_enemigo, ataque_enemigo))
    print()

elif pokemon_elegido == "BULBASAUR":
    movimiento_enemigo = "Látigo cepa"
    vida_enemigo = 100
    ataque_enemigo = 8
    print("Has elegido a {}, tiene {} puntos de vida y su ataque {} infringe {} puntos de daño".format(pokemon_elegido,
                                                                     vida_enemigo, movimiento_enemigo, ataque_enemigo))
    print()

while vida_pickachu > 0 and vida_enemigo > 0:

    ataque_elegido = input("Que ataque quieres usar?  (Impactrueno / Cola de hierro):").upper()

    if ataque_elegido == "IMPACTRUENO":
        vida_enemigo -= 10
        print()
        print("Has usado {} que infringe 10 puntos de daño".format(ataque_elegido))

    elif ataque_elegido == "COLA DE HIERRO":
        vida_enemigo -= 12
        print()
        print("Has usado {} que infringe 12 puntos de daño".format(ataque_elegido))

    if vida_enemigo > 0:
        print("A {} le quedan {} puntos de vida".format(pokemon_elegido, vida_enemigo))
        print()

    if pokemon_elegido == "SQUIRTLE" and vida_enemigo > 0:
        print("{} ha usado {}".format(pokemon_elegido, movimiento_enemigo))

    elif pokemon_elegido == "CHARMANDER" and vida_enemigo > 0:
        print("{} ha usado {}".format(pokemon_elegido, movimiento_enemigo))

    elif pokemon_elegido == "BULBASAUR" and vida_enemigo > 0:
        print("{} ha usado {}".format(pokemon_elegido, movimiento_enemigo))


    vida_pickachu -= ataque_enemigo

    print("A PIKACHU le quedan {} puntos de vida".format(vida_pickachu))
    print()

    if ataque_elegido != "IMPACTRUENO" and ataque_elegido != "COLA DE HIERRO":
        ataque_elegido = print("Pikachu no te ha entendido por lo que no puede atacar.")

print("El combate ha terminado")
print()
if vida_pickachu > vida_enemigo and vida_pickachu > 0:
    print("{} ya no puede continuar, pikachu es el ganador".format(pokemon_elegido))
else:
    print("pikachu ya no puede continuar {} es el ganador".format(pokemon_elegido))
input()