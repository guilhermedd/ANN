from weakref import ProxyTypes
import numpy as np


def poly(x,y):
    n = len(x)-1
    A =[]
    B =[]
    for xi in x:
        row = [1]
        for j in range(1, n+1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A, y)

def func_poly(x, coeffs):
    first=coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])

if __name__ == '__main__':
    #exemplo 1

    x=[0.093, 0.703, 1.029, 1.584, 2.05, 2.329, 2.797, 3.173, 3.722]
    y=[0.552, 1.064, 1.445, 1.947, 1.862, 1.416, 0.304, 0.051, 1.6]

    coeffs = poly(x,y)
    #print(coeffs)

    for x in (coeffs):
        print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)

print("%.16f" %p(2.016))
print("%.16f" %p(2.069))
print("%.16f" %p(2.343))
print("%.16f" %p(3.445))