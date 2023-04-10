from re import S
import numpy as np
from math import sqrt


def f(x):
    return 4 + np.sin(x) - (x**2)/30


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
    x = [1.411, 2.106, 4.451]
    values = [0.403, 1.247]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print('------------')
    for v in values:
        print(str(abs(f(v) - p(v, coefs))) + ',')