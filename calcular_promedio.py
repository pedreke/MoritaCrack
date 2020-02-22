
lista_numeros = []
numero_a_ingresar = float(input("Que número deseas ingresar a la lista? (Escribe 000 para terminar): "))

while numero_a_ingresar != 000:
    (lista_numeros.append(numero_a_ingresar))
    numero_a_ingresar = float(input("Que número deseas ingresar a la lista? (Escribe 000 para terminar): "))

divisor = len(lista_numeros)
suma = sum(lista_numeros)
resultado = suma / divisor
print()
print("El promedio es {}".format(resultado))

input()


