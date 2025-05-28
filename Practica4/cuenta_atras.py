try:
    num = int(input("Ingrese un número positivo:"))
    if num<0:
        raise ValueError ("El número debe de ser positivo")
    cuenta = [str(i) for i in range(num, -1, -1)]
    print("Cuenta atrás:", ", ".join(cuenta))
except ValueError:
    print("Entrada invalida por favor ingrese un número")
except Exception as e:
    print("Se produjo un error inesperado:", e)
    