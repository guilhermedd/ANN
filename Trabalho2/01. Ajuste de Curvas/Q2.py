"""Encontre os coeficientes da reta
            p(x)=a0+a1x
que melhor se aproxima da seguinte lista de 32 pontos
(0.2546,2.8356), (0.3353,2.9623), (0.7622,3.5339), (0.9622,3.879), (1.468,4.2861), (1.6996,4.9079), (2.1777,5.9086), (2.4461,5.8112), (2.725,6.0436), (2.8418,6.1973), (3.1693,6.6387), (3.5006,7.1383), (3.9663,8.1136), (4.2153,7.9829), (4.4435,8.2739), (4.7779,8.984), (5.2763,8.9839), (5.6217,9.9275), (5.6802,9.9008), (6.1081,10.4479), (6.3065,10.6848), (6.6898,11.6681), (7.1006,11.8002), (7.2881,11.884), (7.5019,12.1178), (7.9556,12.7062), (8.4169,13.5418), (8.6543,14.1933), (8.7964,13.7848), (9.2063,14.3995), (9.4889,14.7255) e (9.8509,15.7955)
    Em seguida, calcule p(x) para os seguintes valores de x:
x=1.6169, x=3.245, x=3.3568, x=7.1247  e  x=7.4396"""

from ctypes import sizeof
import numpy as np

def linear(x,y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    A = [
        [n,sum_x],
        [sum_x,sum_x2]
    ]
    sum_y = sum(y)
    sum_yx = sum(yi*xi for yi,xi in zip(y,x))
    B = [
        sum_y,
        sum_yx
    ]
    return np.linalg.solve(A,B)

def f(a0,a1,x):
    return a0 + a1 * x #mudar se necessario


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


if __name__ == '__main__':
    x = [0.1696, 0.5525, 0.7804, 1.0913, 1.3204, 1.8686, 2.0708, 2.325, 2.5044, 2.911, 3.2111, 3.7197, 3.8299, 4.2193, 4.571, 4.8013, 5.1293, 5.5275, 5.6511, 6.1763, 6.4378, 6.8308, 7.0773, 7.1899, 7.7453, 7.833, 8.4028, 8.532, 8.9272, 9.3677, 9.6442, 9.9133]
    y = [3.1643, 3.5237, 3.9154, 4.0876, 4.7993, 4.9908, 5.4722, 5.5973, 5.8933, 6.2905, 6.5776, 7.309, 7.4098, 7.9429, 8.3714, 8.5494, 9.0512, 9.3873, 9.657, 10.1131, 10.5976, 11.0201, 10.7794, 11.508, 11.9917, 12.0991, 12.9252, 12.8596, 13.487, 13.9972, 14.3762, 14.5349]
    values = [2.1031, 3.4627, 3.9893, 7.9514, 9.0573]
    z = []

    a0, a1 = linear(x,y)
    
    print(a0, ',', a1,',')

    for i in x:
        z.append(f(a0, a1, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')