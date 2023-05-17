import numpy as np
import math

'''
Encontre os coeficientes a e b da função y=axe^bx que melhor se aproxima da seguinte lista de 12 pontos
(0.8185,2.6099)...
'''
def best_line(x, y, grau=1):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a*x*np.e**(b*x)
    # return a * (x/(x+b))
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.2796, 1.453, 2.252, 2.7761, 4.1638, 4.7379, 5.7235, 5.9268, 6.9955, 7.7054, 8.5214, 9.5927]
    y = [0.8421, 2.8471, 3.3548, 3.5255, 3.1768, 2.9186, 2.5111, 2.417, 1.9819, 1.7159, 1.409, 1.1258]
    values = [2.5166, 2.7575, 9.2583]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(np.divide(y,x))

    xt = [xi + k2 for xi in x]

    x_ = x
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px = }')

    # visualização

""" import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png')
    """