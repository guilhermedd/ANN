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
    x = [0.3306, 0.3768, 0.7984, 0.9438, 1.1363, 1.3157, 1.7101, 1.9186, 2.2076, 2.4224, 2.5964, 2.8595, 3.1288, 3.2892, 3.5146, 3.7689, 3.9609, 4.2505, 4.416, 4.7237, 4.9604, 5.0961, 5.4174, 5.7228, 5.9394, 6.0072, 6.3469, 6.5605, 6.7945, 7.1184, 7.2305, 7.6229, 7.7349, 7.9576, 8.2006, 8.3583, 8.6371, 8.9398, 9.121, 9.4441, 9.6018, 9.8371]
    y = [1.4303, 1.565, 3.0313, 3.3388, 3.7907, 4.2556, 4.8377, 5.1268, 5.4377, 5.596, 5.7074, 5.9102, 5.9293, 5.9476, 5.9126, 5.911, 5.9066, 5.8302, 5.7406, 5.6654, 5.5733, 5.4667, 5.2752, 5.1496, 5.0416, 4.9509, 4.7762, 4.6457, 4.4726, 4.2777, 4.2251, 4.0295, 3.9602, 3.7405, 3.6326, 3.4993, 3.3675, 3.2124, 3.1319, 2.9216, 2.8089, 2.6934]
    values = [3.3726, 8.3238, 9.3259, 9.5391, 9.8047]
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