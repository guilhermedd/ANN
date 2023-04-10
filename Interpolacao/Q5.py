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

    x=[-3.501, 0.782, 2.865]
    y=[3.368, 3.434, 4.735]

    coeffs = poly(x,y)
    #print(coeffs)

    for x in (coeffs):
        print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)

print("%.16f" %p(-3.229))
print("%.16f" %p(1.308))