medicion = input("En que medición tienes tus datos?  (Fahrenheit / Celsius): ").upper()

if medicion == "FAHRENHEIT":
    grados = int(input("Ingresa tus grados {}: ".format(medicion)))
    resultado = (grados - 32) / 1.8
    print("°{} {} son °{} celsius".format(grados, medicion, resultado))
elif medicion == "CELSIUS":
    grados = int(input("Ingresa tus grados {}: ".format(medicion)))
    resultado = (grados * 1.8 + 32)
    print("°{} {} son °{} farenheit".format(grados, medicion, resultado))

input()




