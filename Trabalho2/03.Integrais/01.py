import math
from numpy import double

# Usado para aproximar o valor de uma integral
def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


def f(x):
    return math.sin((math.exp(-x**2))) + 1

intervalo = [-1.091, 1.214]
subintervalos = [6, 13, 26, 70, 76, 116, 244, 299, 609, 837, 1621, 5046]
for i in range(len(subintervalos)):
    r = trapz(f, intervalo[0], intervalo[1], subintervalos[i])
    print(r,',')
