try:
    cadena = input ("Ingresa una cadena de caracteres:")
    if cadena == cadena[::-1]:
        print(f"La cadena '{cadena}' es palíndroma")
    else:
        print(f"La cadena '{cadena}' no es palíndroma")
except Exception as e :
    print(f"Ocurrio un error: {e}")