import numpy as np


def levenshteinDistance(a, b):
    matriz = np.zeros(((len(a) + 1), (len(b) + 1)))
    for i in range(0,len(b)+1):
        matriz[0][i]=i
    for j in range(0,len(a)+1):
        matriz[j][0]=j
    #calculo distancias
    for i in range(1,len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1]==b[j-1]:
                indicator=0
            else:
                indicator=1
            superior=matriz[i-1][j]+1
            lateral=matriz[i][j-1]+1
            diagonal=matriz[i-1][j-1]+indicator
            compval=[superior,lateral,diagonal]
            agregar= min(compval)
            matriz[i][j]=agregar
    print(matriz)
    numcambios=int(matriz[len(a),len(b)])
    #print(numcambios)
    return numcambios


cambios=levenshteinDistance("paralelogramo", "cuadrado")
print(f'La cantidad de cambios por la palabras son: {cambios}')

#terminado
