import random
import numpy as np
import math
def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        A.append([0]*n)
        for j in range(n):
            A[i][j] = xs[j] ** i
        potencias = [k + 1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i - ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A,B)
    soma = 0
    for ck, xk in zip(cs, xs):
        soma += ck * f(xk)
    return soma

def f(x):
    return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)


x0 = 0.4927
ordem = 5
xs = [0.2521, 0.2965, 0.3624, 0.4337, 0.4772,
     0.5223, 0.5514, 0.6161, 0.6489, 0.7341]
values = [0.3211, 0.378, 0.4064, 0.6536, 0.7094]
ordem1 = 1
ordem2 = 2
ordem3 = 3
ordem4 = 4
ordem5 = 5

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(xs, ordem1, x0, f)*(values[i] - x0) + ((finite_diffs(xs, ordem2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(xs, ordem3, x0, f)/6) * ((values[i]-x0)**3)) + ((finite_diffs(xs, ordem4, x0, f)/24) * ((values[i]-x0)**4)) + ((finite_diffs(xs, ordem, x0, f)/120) * ((values[i]-x0)**5)) 
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{p}, {erroN},')

num_pontos = 0
a = x0 - 0.25
b = x0 + 0.25
#xs = [a + (b - a) * random.random() for _ in range(num_pontos)]
#xs.sort()

#r = finite_diffs(xs, ordem, x0, f)
#print(xs)
#print(f'aprox para derivada de ordem {ordem} de f no ponto {x0} {r}')