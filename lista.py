
mi_lista = []
input_usuario = input("Que deseas agregar a la lista de compras? (si ya has terminado escribe FIN)")

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("Que deseas agregar a la lista de compras? (si ya has terminado escribe FIN)")

for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print()
print("Esta es la lista de la compra")
input()










