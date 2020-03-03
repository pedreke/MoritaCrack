
os = input("Prefieres iOS o Android?: ").upper()

if os == "ANDROID":
    dinero = input("Tienes dinero? (Si/No): ").upper()
    if dinero == "NO":
        print("Tu mejor opción es un android chino de 50 lks")
    else:
        camara = input("Te importa la cámara? (Si/No): ").upper()
        if camara == "SI":
            print("Compra un google pixel con supercámara")
        else:
            print("Compra un Xiaomi, es la mejor opción calidad-precio")

elif os == "IOS":
    dinero = input("Tienes dinero? (Si/No): ").upper()
    if dinero == "NO":
        print("Compra un iphone de segunda mano")
    else:
        print("Compra un iphone super ultra plus pro")

input()