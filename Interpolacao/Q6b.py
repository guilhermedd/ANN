from cmath import sin, sqrt
import numpy as np



def f(x):
    return x**5 - 4 * x**2 + 2 * sqrt(x + 1) + np.cos(x)  


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
    x = [0.371, 1.072, 1.779, 2.64, 3.587, 3.973, 4.753, 5.872, 6.596]
    values = [0.637, 1.152, 3.931, 4.205, 5.9]
            
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)

print('-----------')
for v in values:
    print(str(abs(f(v) - p(v, coefs))) + ',')