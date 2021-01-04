import math
def L_Evklid(s, x):
    summ = 0
    for i in range(len(s)):
        summ += math.pow((s[i]-x[i]),2)
    return math.sqrt(summ)

def L_Evklid_v(s, x, ves):
    summ = 0
    for i in range(len(s)):
        summ += math.pow((s[i]-x[i])*ves,2)
    return math.sqrt(summ)

def L_Minkowski(s, x, k):
    summ = 0
    for i in range(len(s)):
        summ += math.pow(s[i]-x[i],k)

    return math.pow(summ, 1/k)

def L_Minkowski_v(s, x, k, ves):
    summ = 0
    for i in range(len(s)):
        summ += math.pow((s[i]-x[i])*ves,k)

    return math.pow(summ, 1/k)

def L_po_mod(s, x):
    summ = 0
    for i in range(len(s)):
        summ += math.fabs(s[i]-x[i])
    return summ

def L_po_mod_v(s, x, ves):
    summ = 0
    for i in range(len(s)):
        summ += math.fabs((s[i]-x[i])*ves)
    return summ

def L_Camberro(s,x):
    summ = 0
    for i in range(len(s)):
        summ += math.fabs((s[i]-x[i])/(s[i]+x[i]))
    return summ


def delta(x1, x2):
    if x1>x2:
        return 1
    if x1<x2:
        return -1
    if x1==x2:
        return 0


def L_Kendal(s, x):
    summ = 0
    for q in range(len(s)-1):
        for k in range(1,len(s)):
            if q<k:
                summ += delta(s[q],s[k])*delta(x[q],x[k])
    r2=1-(2/(len(s)/2*len(s)))
    return summ*(2/((len(s)/2)*len(s)))


def L_4ebishev(s,x):
    l4 = math.fabs(s[0]-x[0])
    for i in range(len(s)):
        raz=math.fabs(s[i]-x[i])
        if raz>l4:
            l4 = raz
    return l4
test = [0, 1, 0]
test2 = [4, 0, 4]
print(L_Evklid(test, test2))
print(L_Minkowski(test, test2, 2))
print(L_po_mod(test, test2))
print(L_Camberro(test, test2))
print(L_Kendal(test, test2))
print(L_4ebishev(test, test2))

kmax = [[1, 2, 3], [3, 2, 1]]
kmin = [[1, 2, 3], [1, 2, 3]]
kme = [[1, 0, 2], [1, 3, 4]]
print((kmin[0], kmin[1]))
print(L_Kendal(kmax[0], kmax[1]))
print(L_Kendal(kme[0], kme[1]))

vari = [[1, 2, 2], [1, 2, 3]]
print(L_4ebishev(vari[0], vari[1]))

doriv = [[1,2,3],[1,2,3]]
print(L_4ebishev(doriv[0], doriv[1]))
print(L_Kendal(doriv[0], doriv[1]))
