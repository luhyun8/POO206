try:
    for i in range(10, 201):
        if i % 5 == 0:
            print(i)
except ValueError as e:
    print("Error",e)
        