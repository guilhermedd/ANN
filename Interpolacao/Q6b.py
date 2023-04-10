from cmath import sin
import numpy as np



def f(x):
    return np.sin(x)**3- 3*np.sin(x)**2+np.sin(pow(x,2)) + 4


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
    x = [-3.741, -1.233, -0.28, 1.582, 3.725]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)
print(abs(f(-0.455) - p(-0.455, coefs)))
print(abs(f(1.476) - p(1.476, coefs)))
print(abs(f(2.114) - p(2.114, coefs)))