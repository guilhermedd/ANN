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

    x = [-1.591, -0.712, 0.441, 1.612, 2.718, 3.653, 4.135, 5.649, 6.204]
    y = [0.689, 0.943, 0.967, 0.679, -0.103, -0.795, -0.977, -0.355, 0.168]
    values = [1.648, 3.67, 3.774, 4.132]

    coeffs = poly(x,y)
    #print(coeffs)

    for x in (coeffs):
        print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)
print("\n================================")
for v in values:
    print("%.16f," %p(v))