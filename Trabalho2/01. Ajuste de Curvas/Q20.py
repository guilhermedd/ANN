import numpy as np
import math

# k = kmax*C²/cs+C²

"""Um pesquisador relatou os dados tabulados a seguir de um experimento realizado 
para determinar a taxa de crescimento k (por dia) de bactérias como uma função da 
concentração de oxigênio c (em mg/L).
Sabe-se que tais dados podem ser modelados pela seguinte equação:
        k = kmax*C²/cs+C²
onde cs e kmax são parâmetros. Use uma transformação para linearizar essa equação. 
A seguir, use regressão linear para encontrar os valores de cs e kmax e prever a taxa de 
crescimento para as seguintes concentrações de oxigênio
    c1=5.7891mg/L , c2=8.5182mg/L  e  c3=9.2664mg/L"""

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
    return (a*x**2)/(b+x**2)
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [1.8357, 2.3799, 3.1555, 3.9453, 5.2684, 5.8312, 6.6334, 8.1929, 8.5803, 9.5195, 10.4909, 11.1608]
    y = [2.7419, 3.3906, 3.7783, 4.1265, 4.4455, 4.4639, 4.5717, 4.8403, 4.6852, 4.6842, 4.6787, 4.7756]
    values = [4.4379, 5.7099, 6.6326]
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

    x_ = np.divide(1,(np.power(x,2)))
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = 1/a0

    b = a1*a
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

'''   import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png')'''