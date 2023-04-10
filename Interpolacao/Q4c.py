from cmath import log
import numpy as np
from math import sqrt,log,pow


def f(x):
    return np.cos(x+sqrt(log(x**2)))


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
    x = [1.539, 1.925, 2.165, 2.658, 2.93, 3.208, 3.398, 3.816, 4.283, 4.573, 4.857]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)
   # print(abs(f(-2.285) - p(-2.285, coefs)))
    #print(abs(f(-1.791) - p(-1.791, coefs)))
    #print(abs(f(-0.837) - p(-0.837, coefs))) #pontos