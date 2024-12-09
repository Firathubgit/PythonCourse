def round_list(x):
    for i in range(len(x)):
        x[i] = round(x[i], 2)

lista_från_användaren = list(map(float, input("Ange en lista (separerad med mellanslag): ").split()))

round_list(lista_från_användaren)

print(lista_från_användaren)
