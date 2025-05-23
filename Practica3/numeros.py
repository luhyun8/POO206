try:
    numero = int(input("Introduce un número"))
    if numero % 2 == 0:
        print("Es un numero par")
    else:
        print("Es un numero inpar")
except ValueError:
    print("Debes ingresar un numero")