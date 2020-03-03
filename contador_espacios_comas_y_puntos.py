frase_del_usuario = input("Introduce una frase: ")

caracter = [" ", ".", ","]

n_espacios = 0
n_puntos = 0
n_comas = 0

for letra in frase_del_usuario:
    if letra in caracter[0]:
        n_espacios += 1
    elif letra in caracter[1]:
        n_puntos += 1
    elif letra in caracter[2]:
        n_comas += 1

print()
print("Espacios: {}".format(n_espacios))
print("Puntos: {}".format(n_puntos))
print("Comas: {}".format(n_comas))
input()