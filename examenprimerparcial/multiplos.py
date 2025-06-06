#programa que visualice numeros multiplos de cinco comprendidos entre diez y doscientos
try:
    for i in range(10, 201):
        if i % 5 == 0:
            print(i)
except ValueError as e:
    print("Error.Debe ser un numero multiplo de 5",e)
        