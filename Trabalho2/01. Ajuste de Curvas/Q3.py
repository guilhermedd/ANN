"""Encontre os coeficientes da parábola
        p(x)=a0+a1x+a2x2
que melhor se aproxima da seguinte lista de 14 pontos
(0.5214,4.8497), (0.9699,4.5825), (1.5672,4.1897), (2.4802,3.8022), (3.508,3.5953), (3.7891,3.5712), (4.3322,3.4629), (5.4911,3.6128), (5.7468,3.6383), (7.1001,4.0907), (7.4395,4.2607), (8.4192,4.9239), (9.0073,5.3796) e (9.3096,5.8089)
Em seguida, calcule p(x) para os seguintes valores de x:
x=6.7293, x=7.6609  e  x=8.1986"""

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

def f(a0,a1,a2,x):
    return a0+a1*x+a2*math.pow(x,2) #mudar se necessario

if __name__ == '__main__':
    x = [0.2404, 1.3342, 1.8272, 2.3903, 2.9803, 3.9183, 4.7107, 5.04, 6.3793, 7.1402, 7.4579, 7.8816, 8.7554, 9.3118]
    y = [5.6157, 4.7761, 4.317, 4.05, 3.6713, 3.2195, 3.2271, 3.1965, 3.3568, 3.6134, 3.7014, 3.8965, 4.3461, 4.7881]
    values = [1.298, 4.1128, 8.7508]
    z = []

    a0, a1, a2 = best_poly(x, y, 2)
    
    print(a0, ',', a1,',',a2,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')