def Factorial(num):
    return 1 if (num==0 or num==1) else num*Factorial(num-1)

def Fibonnaci(posicion):
    if (posicion==0):
        return 0
    elif (posicion==1):
        return 1
    else:
        return Fibonnaci(posicion-1)+Fibonnaci(posicion-2)




num=5
factorial=Factorial(num)
pos=5
print(f'El facotrial de {num} es {factorial}')
print(f'El valor de fibonacci en la posicion {pos} es {Fibonnaci(pos)}')


