

numero_para_adivinar = input("Número a adivinar (que tu oponente no lo vea):")

numero_elegido_por_el_oponente = input("Adivina el número de tu oponente:")

while numero_para_adivinar != numero_elegido_por_el_oponente:
    numero_elegido_por_el_oponente = input("Ese no es, intenta con otro:")

else:
    print("Has ganado!")


