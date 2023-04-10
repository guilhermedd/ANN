import numpy as np
from math import exp


def f(x):
    return np.cos(exp(-x**2)) + np.sin(x**2 / 2)


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
    x = [0.187, 0.812, 1.411, 1.866, 2.17, 2.69, 3.149, 3.95]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    for p in coefs:
        print(str(p) + ',')
    print(coefs)
    print(abs(f(-2.285) - p(-2.285, coefs)))
    print(abs(f(-1.791) - p(-1.791, coefs)))
    print(abs(f(-0.837) - p(-0.837, coefs))) #pontos