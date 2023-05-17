import numpy as np
import math


'''
Encontre os coeficientes a e b da função taxa de crescimento da saturação y=a(x/(x+b) que melhor se aproxima da seguinte lista de 12 pontos
(2.106,0.8735)...
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
    return a * (x/(x+b))
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [1.242, 1.7964, 2.0978, 2.4697, 2.8209, 3.3865, 3.8488, 4.1777, 4.9318, 5.4696, 5.6321, 6.0379, 6.8459, 7.2758, 7.6496, 7.8399, 8.5626, 8.6912, 9.5646, 9.7181, 10.1446, 10.6166, 11.2661, 11.496, 12.0494, 12.7053, 12.788, 13.4008, 14.0099, 14.2957, 14.792, 15.1182, 15.5796, 16.0335, 16.6725, 17.0004, 17.3679, 18.0958, 18.4252, 18.7414, 19.4322, 19.7343]
    y = [2.424, 2.8512, 3.0642, 3.178, 3.3427, 3.5213, 3.6775, 3.7232, 3.8439, 3.9104, 3.9119, 3.9747, 4.0459, 4.1009, 4.1062, 4.1175, 4.1815, 4.2132, 4.244, 4.2425, 4.2619, 4.2803, 4.33, 4.319, 4.3499, 4.3424, 4.356, 4.3697, 4.3708, 4.3853, 4.4433, 4.4275, 4.4153, 4.4414, 4.4438, 4.4386, 4.4772, 4.4775, 4.4765, 4.4957, 4.4484, 4.4557]
    values = [2.1771, 8.4768, 8.5472, 8.5764, 10.7741]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = (np.divide(1,y))

    xt = [xi + k2 for xi in x]

    x_ = np.divide(1,x)
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = 1/a0

    b = a1/a0
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

''' import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png')
    '''