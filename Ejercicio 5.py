def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista [j], lista [j+1] = lista[j+1], lista[j]
    return lista


lista_ordenada = bubble_sort([64, 34, 25, 12, 22, 11, 90])
print(lista_ordenada)