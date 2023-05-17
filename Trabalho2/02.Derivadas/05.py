'''Use o método das diferenças finitas e a seguinte lista de 7 pontos
    x1=2.3663, x2=2.4307, x3=2.4588, x4=2.5234, x5=2.6599, x6=2.6884  e  x7=2.7455
para encontrar uma aproximação para f′′′(x0), onde 
    f(x)=sin^4(x)−4sin^2(x)+cos(x2)+e−x^2+5 e x0=2.5581.'''

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
        return  math.sqrt(math.cos(x**2) + x)

    k = 2 # ordem
    n = 8 # número de pontos
    x0 = 2.5269
    x = [2.3247, 2.3399, 2.4273, 2.4691, 2.5847, 2.6167, 2.6603, 2.7203]



    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

   # print(f'{coeffs}')
    print(f'{aprox}')