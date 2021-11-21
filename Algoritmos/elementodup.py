'''Dado un arreglo a que contiene solo números en el rango de 1 a una longitud,
encuentre el primer número duplicado para el que la segunda aparición tiene el índice mínimo.
En otras palabras, si hay más de 1 número duplicado, devuelve el número para el que la segunda
aparición tiene un índice más pequeño que la segunda aparición del otro número.
Si no hay tales elementos, devuelve -1.'''

a = [2, 1, 3, 5, 3, 2]
b = [2, 4, 3, 5, 1]
c = [2, 2]

def firstDuplicate(lista):
    datosp=[]
    dupl=-1
    for i in lista:
        if i not in datosp:
            datosp.append(i)
        else:
            dupl=i
            return dupl
            break
    return dupl

duplicado = firstDuplicate(a)
print(f'De la primera cadena el primer duplicado es {duplicado}')
duplicado = firstDuplicate(b)
print(f'De la segunda cadena el primer duplicado es {duplicado}')
duplicado = firstDuplicate(c)
print(f'De la tercera cadena el primer duplicado es {duplicado}')