def compara(lst, o, d):
    if lst[o] > lst[d]:
        lst[o], lst[d] = lst[d], lst[o]

def redord(lst):
    compara(lst, 0, 2)
    compara(lst, 1, 3)
    compara(lst, 0, 1)
    compara(lst, 2, 3)
    compara(lst, 1, 2)
    
    
lista = [3,2,4,1]
redord(lista)
print(lista)