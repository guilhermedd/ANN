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

    x = [-2.519, -0.405, 3.627]
    y = [2.844, 3.636, 3.801]

    coeffs = poly(x,y)
    #print(coeffs)

    # for x in (coeffs):
        # print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)
    
for v in [-2.886, -1.853]:
    print("%.16f," %p(v))
    print("%.16f," %p(v))