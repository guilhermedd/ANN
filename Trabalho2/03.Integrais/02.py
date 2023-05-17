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
    return math.sin((x/math.sqrt(x*x+1))) + 1

intervalo = [-1.823, 1.843]
subintervalos = [6, 16, 48, 70, 82, 139, 206, 416, 612, 756, 3649, 9958]
for i in range(len(subintervalos)):
    r = trapz(f, intervalo[0], intervalo[1], subintervalos[i])
    print(r,',')
