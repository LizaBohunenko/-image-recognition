def av(xi, xj):
    summ = 0
    for i in range(len(xi)):
        summ += (xi[i]*xj[i])
    return summ


def bv(xi, xj):
    summ = 0
    for i in range(len(xi)):
        summ=summ+(1-xi[i])*(1-xj[i])
    return summ


def gv(xi, xj):
    summ = 0
    for i in range(len(xi)):
        summ=summ+xi[i]*(1-xj[i])
    return summ


def hv(xi, xj):
    summ = 0
    for i in range(len(xi)):
        summ=summ+(1-xi[i])*xj[i]
    return summ


def rusel_rao(xi, xj):
    return av(xi, xj)/len(xi)


def gokart_nidmen(xi, xj):
    return av(xi, xj)/(len(xi)-bv(xi, xj))


def daise(xi, xj):
    return av(xi,xj)/(2*av(xi, xj)+gv(xi,xj)+hv(xi,xj))


def sokol_snifa(xi, xj):
    return av(xi, xj)/(av(xi,xj)+2*(gv(xi,xj)+hv(xi,xj)))


def sokol_mish(xi, xj):
    return (av(xi,xj)+bv(xi,xj))/len(xi)


def kulzhinskiy(xi, xj):
    return av(xi,xj)/(gv(xi,xj)+hv(xi, xj))


def ula(xi, xj):
    ab = (av(xi,xj)*bv(xi,xj))
    gh = (gv(xi,xj)*hv(xi,xj))
    return (ab-gh)/(ab+gh)


def heming_distance(xi, xj):
    s = 0
    for k in range(len(xi)):
        s += abs(xi[k]-xj[k])

    return s

test = [1,0,0]
test1 = [1,0,1]
print(gokart_nidmen(test, test1))
print(ula(test, test1))
print(sokol_snifa(test, test1))
print(daise(test, test1))
print(kulzhinskiy(test, test1))
print(sokol_mish(test, test1))
print(rusel_rao(test, test1))

rao_mx = [0, 0, 0]
rao_mx_1 = [1, 0, 0]
print(rusel_rao(rao_mx, rao_mx_1))

ham_min = [1, 1, 1]
ham_min1 = [1, 1, 1]
print(heming_distance(ham_min, ham_min1))
print(rusel_rao(ham_min, ham_min1))
