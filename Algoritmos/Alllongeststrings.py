#* Dado un arreglo de cadenas regresar otro arreglo que contenga
# * solo las cadenas mas largas
# *
# * Ejemplo:
# * para:
# * inputArray = ["aba", "aa", "ad", "vcd", "aba"]
# *
# * la salida debe ser:
# * allLongestStrings(inputArray) = ["aba", "vcd", "aba"]

inputArray = ["aba", "aa", "ad", "vcd", "aba","prueba"]

def allLongestStrings(inputArray):
    Arraylongcad=[]
    loncadlarga = 0
    for i in inputArray:
        lencad = len(i)
        if lencad > loncadlarga:
            loncadlarga = lencad
    for i in inputArray:
        if len(i) == loncadlarga:
            Arraylongcad.append(i)
    print(Arraylongcad)


allLongestStrings(inputArray)


#Resuleto