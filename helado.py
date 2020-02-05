


quiere_helado_input = input("Te gustaria comer un helado? (Si/No): ").upper()

if quiere_helado_input == "SI":
    apetece_helado = True
elif quiere_helado_input == "NO":
    apetece_helado = False
else:
    print("Es si o no, asi que lo que me dijiste lo tomaré como un no")
    apetece_helado = False


tiene_dinero_input = input("Tienes dinero? (Si/No): ").upper()
hay_heladero_input = input("Esta el heladero? (Si/No): ").upper()
estas_con_tu_tia_input = input("Estás con tu tía? (Si/No): ").upper()

apetece_helado = quiere_helado_input == "SI"
puedes_comprarlo = tiene_dinero_input == "SI" or estas_con_tu_tia_input == "SI"
hay_heladero = hay_heladero_input == "SI"


if apetece_helado and puedes_comprarlo and hay_heladero:
    print("Pues compra")
else:
    print("Comamos otra cosa")
