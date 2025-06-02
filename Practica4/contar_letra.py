try:
    frase= input("Ingrese una frase:")
    letra = input("Ingrese una letra:")
    if len(letra) != 1:
        raise ValueError("Debes introducir solo una letra.")
    contador = frase.count(letra)
    if any (char,i)
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")
except ValueError as e:
        print("Error:", e)
except Exception as e:
        print("Se produjo un error inesperado:", e)
