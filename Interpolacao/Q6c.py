import numpy as np


def f(x):
    return (np.cos(x)**3)+(2*np.cos(x)**2)+1


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
    x = [-2.515, -2.042, -0.695, -0.183, 1.049, 1.328, 2.317, 3.4, 4.286]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)

print(abs(f(-0.12) - p(-0.12, coefs)))
print(abs(f( 0.552) - p( 0.552, coefs)))
print(abs(f(3.471) - p(3.471, coefs)))
print(abs(f(3.952) - p(3.952, coefs)))
print(abs(f( 4.235) - p( 4.235, coefs)))#pontos