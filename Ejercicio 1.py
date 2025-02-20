def suma(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma
    

mi_lista=[1,2,3,4,5,6]  
print(suma(mi_lista))
