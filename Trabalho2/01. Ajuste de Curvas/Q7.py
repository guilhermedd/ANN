"""Encontre os coeficientes do polinômio de grau 4
    p(x)=a0+a1x+a2x2+a3x3+a4x4
que melhor se aproxima da seguinte lista de 15 pontos
(−4.4757,−3.0911), (−3.558,1.5156), (−2.9413,2.4488), (−2.5241,2.1296), (−1.6177,0.8754), (−0.8727,−0.303), (0.0278,−0.6147), (0.6886,−0.4195), (1.344,0.4561), (1.7158,2.0599), (2.4426,2.8625), (3.7933,4.7005), (4.1497,4.152), (5.2038,−1.6168) e (5.3924,−4.6273)
Em seguida, calcule p(x) para os seguintes valores de x:
    x=−1.5075, x=−1.1099  e  x=2.1815"""

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

def f(a0,a1,a2,a3,a4,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3+a4*x**4

if __name__ == '__main__':
    x = [-4.9742, -3.8495, -3.1291, -2.4684, -1.9416, -0.6587, -0.0476, 0.4263, 0.9771, 2.2458, 3.0086, 3.2641, 4.007, 4.5755, 5.3698]
    y = [-10.455, 0.82, 2.8325, 2.9024, 1.7352, -0.3561, -0.425, 0.7856, -0.1432, 3.2959, 5.2041, 5.8199, 5.4119, 3.2142, -4.635]
    values = [-4.122, -2.5816, -0.256]
    z = []

    a0, a1, a2, a3, a4 = best_poly(x, y, 4) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',',a4,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3,a4, i)) #nao esqueça de colocar aqui tb

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')