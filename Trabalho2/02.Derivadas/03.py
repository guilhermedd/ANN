'''Use o método das diferenças finitas e a seguinte lista de 4 pontos
        x1=1.5927, x2=1.6663, x3=1.8682  e  x4=1.9129
para encontrar uma aproximação para f′′(x0), onde 
     f(x)=sin3(x)−3sin2(x)+sin(x2)+4 e x0=1.7441.'''

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
        return math.sin(math.cos(math.exp(-x)))

    k = 1 # ordem
    n = 9 # número de pontos
    x0 = -2.1768
    x = [-2.4236, -2.3671, -2.2855, -2.2383, -
        2.1852, -2.1459, -2.0602, -2.0277, -1.9558]

    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

   # print(f'{coeffs}')
    print(f'{aprox}')