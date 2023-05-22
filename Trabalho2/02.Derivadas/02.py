'''Use o método das diferenças finitas e a seguinte lista de 5 pontos
        x1=1.2002, x2=1.3504, x3=1.4137, x4=1.5124  e  x5=1.6499
para encontrar uma aproximação para f′(x0), onde 
        f(x)=sin(cos(e−x)) e x0=1.417.'''

from cmath import exp
import numpy as np
import math

def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1] * n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matrz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    return np.linalg.solve(A, B)

def dif_fin(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))


if __name__ == '__main__':
    
    def f(x):
        return math.cos(math.exp(-x**2)) + math.sin(x**2 / 2)

    k = 1 # ordem
    n = 5 # número de pontos
    x0 = 0.4448
    x = [0.2702, 0.3334, 0.413, 0.5444, 0.6587]


    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

   # print(f'{coeffs}')
    print(f'{aprox}')