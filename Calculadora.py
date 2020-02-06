primer_numero = 1
segundo_numero = 1

operador = input("Qué operación quieres realizar?  (Suma / Resta / Multiplicación / División)").upper()


if operador == "SUMA" or "MULTIPLICACIÓN" or "RESTA" or "DIVISIÓN":
    primer_numero = int(input("Cual será el primer número?"))
    segundo_numero = int(input("Cual sera el segundo número?"))

if operador == "SUMA":
    print(primer_numero + segundo_numero)
    print("Operación terminada")
if operador == "RESTA":
    print(primer_numero - segundo_numero)
    print("Operación terminada")
if operador == "MULTIPLICACIÓN":
    print(primer_numero * segundo_numero)
    print("Operación terminada")
if operador == "DIVISIÓN":
    print(primer_numero / segundo_numero)
    print("Operación terminada")







