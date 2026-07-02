def imprime(mat):
    for x in mat:
        print(x)
    print   

def cammcorRE(lab, f, c):
    global ops
    ops += 1
    if f == 0 and c == 0:
        return lab[f][c]
    elif f == 0:
        return lab[f][c] + cammcorRE(lab, f, c-1)
    elif c == 0:
        return lab[f][c] + cammcorRE(lab, f-1, c)
    else:
        return lab[f][c] + min(cammcorRE(lab, f-1, c),cammcorRE(lab, f, c-1))

def cammcorPD(lab, acu, f, c):
    global ops
    ops += 1
    if acu[f][c] != 0:
        return acu[f][c]
    elif f == 0 and c == 0:
        acu[f][c] = lab[f][c]
        return acu[f][c]
    elif f == 0:
        acu[f][c] = lab[f][c] + cammcorPD(lab, acu, f, c-1)
        return acu[f][c]
    elif c == 0:
        acu[f][c] = lab[f][c] + cammcorPD(lab, acu, f-1, c)
        return acu[f][c]
    else:
        acu[f][c] = lab[f][c] + min(cammcorPD(lab, acu, f-1, c),cammcorPD(lab, acu, f, c-1))
        return acu[f][c]


lab = [
    [9,6,4],
    [8,3,5],
    [2,1,7]
]

acu = [[0 for _ in range(len(lab))] for _ in range(len(lab))]

ops = 0
costo = cammcorRE(lab, len(lab)-1, len(lab[0])-1)
print(f"Cuesta {costo} RE y usa {ops} operaciones")

ops = 0
costo = cammcorPD(lab, acu, len(lab)-1, len(lab[0])-1)
print(f"Cuesta {costo} PD y usa {ops} operaciones")
imprime(acu)