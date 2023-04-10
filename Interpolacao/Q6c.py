import numpy as np
from math import exp


def f(x):
    return exp(-x**2) + np.cos(x) + 3


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
    x = [0.31, 1.366, 1.803, 2.818, 3.658, 4.54, 4.985, 5.9, 6.92]
    values = [0.814, 1.114, 3.36, 3.736, 6.922]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)

for v in values:
    print(str(abs(f(v) - p(v, coefs))) + ',')#pontos