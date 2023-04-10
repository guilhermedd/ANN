from cmath import log
import numpy as np
from math import sqrt,log,pow


def f(x):
    return 1 / (1 + 25 * x**2)


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
    x = [-0.943, -0.711, -0.618, -0.344, -0.172, -0.015, 0.192, 0.369, 0.493, 0.719, 0.896]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    for p in coefs:
        print(str(p) + ',') 
    print(coefs)
   # print(abs(f(-2.285) - p(-2.285, coefs)))
    #print(abs(f(-1.791) - p(-1.791, coefs)))
    #print(abs(f(-0.837) - p(-0.837, coefs))) #pontos