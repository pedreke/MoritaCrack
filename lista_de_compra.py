
lista_de_cosas_por_comprar = []
input_usuario = input("Que deseas agregar a la lista? (Escribe FIN si ya has terminado)")

while input_usuario != "FIN":
    lista_de_cosas_por_comprar.append(input_usuario)
    input_usuario = input("Que deseas agregar a la lista? (Escribe FIN si ya has terminado)")


largo_lista = len(lista_de_cosas_por_comprar)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(lista_de_cosas_por_comprar[indice_actual]))
    indice_actual += 1

print("Esta es la lista para comprar")

input()



