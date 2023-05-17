"""Encontre os coeficientes do polinômio de grau 5
        p(x)=a0+a1x+a2x2+a3x3+a4x4+a5x5
que melhor se aproxima da seguinte lista de 16 pontos
(−3.9938,−0.1977), (−3.3972,1.6594), (−3.1428,3.3373), (−2.3556,−0.0751), (−2.2078,0.4927), (−1.2174,−0.9251), (−1.0884,−0.7903), (−0.2997,−0.2558), (0.2837,0.5042), (1.0177,0.3647), (1.4287,−0.7894), (2.1347,0.0071), (2.328,−0.5366), (2.8746,−1.7185), (3.4311,−1.8013) e (4.0467,0.3257)
Em seguida, calcule p(x) para os seguintes valores de x:
    x=−2.7522, x=−0.0844  e  x=3.0554"""

import numpy as np
import math

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)



def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])

def f(a0,a1,a2,a3,a4,a5,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3+a4*x**4+a5*x**5

if __name__ == '__main__':
    x = [-4.2004, -3.7663, -3.1969, -2.7653, -1.9161, -1.1841, -0.6756, -0.0615, 0.2463, 1.069, 1.6191, 2.0595, 2.6097, 2.964, 3.8136, 4.4911]
    y = [-2.8114, 1.6738, 2.9194, 2.0299, 0.5844, -1.0324, -0.965, -0.2323, 0.4695, 0.9297, 0.648, -0.0437, -2.0543, -2.3881, -1.1676, 7.5278]
    values = [1.2818, 3.2976, 3.8357]
    z = []

    a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',',a4,',',a5,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3,a4,a5, i)) #nao esqueça de colocar aqui tb

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')