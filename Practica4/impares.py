try:
    num = int(input("Ingrese un número entero positivo mayor que 10: "))
    if num <= 10:
        raise ValueError("El número debe ser mayor que 10.")
    impares = [str(i) for i in range(3, num + 1, 2)]
    print("Números impares desde 2 hasta", num, ":", ", ".join(impares))
except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")
except Exception as e:
            print(("Se produjo un error inesperado:", e))




