# Imprimir en pantalla números del 1 a N
# Si el número es divisible entre 3 imprimimos Fizz
# Si el número es divisible entre 5 imprimimos Buzz
# Si el número es divisible entre 3 y 5 imprimimos FizzBuzz

def FizzBuzz(numero):
    for i in range(1, numero + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 3 == 0):
            print("Buzz")
        else:
            print(i)


num = input("Numero que desea probar: ")
#print(type(num))
FizzBuzz(int(num))

#Resuleto