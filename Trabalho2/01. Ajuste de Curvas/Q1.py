"""Encontre os coeficientes da reta
            p(x)=a0+a1x
que melhor se aproxima da seguinte lista de 12 pontos
    (0.7064,4.1678), (1.3923,6.563), (2.4829,9.7186), (3.0716,11.0116), (3.8615,13.5959), (4.6128,15.2451), (5.2869,18.5277), (5.9634,19.5883), (6.859,22.2843), (8.0048,25.5162), (8.8814,27.997) e (9.3609,29.2071)
    Em seguida, calcule p(x) para os seguintes valores de x:
    x=3.7086, x=5.2767  e  x=5.4068*"""

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
    x = [0.7073, 1.0735, 2.0271, 3.1754, 3.9105, 4.182, 5.7525, 6.5695, 7.3189, 8.3057, 8.9372, 9.5002]
    y = [4.6466, 5.3415, 6.2297, 8.7545, 9.9766, 10.4724, 12.8314, 14.3216, 15.6485, 17.1167, 18.3602, 18.9071]
    values = [0.7459, 2.341, 3.2559]
    z = []

    a0, a1 = linear(x,y)
    
    print(a0, ',', a1,',')

    for i in x:
        z.append(f(a0, a1, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')