
frase_del_usuario = input("Introduce una frase: ")

n_mayusculas = 0

for letra in frase_del_usuario:
    if letra.isupper():
        n_mayusculas += 1

print()
print("Mayúsculas: {}".format(n_mayusculas))
input()
