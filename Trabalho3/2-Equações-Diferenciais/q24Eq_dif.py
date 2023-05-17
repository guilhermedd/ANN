"""Em um circuito com tensão aplicada E e com resistência R, indutância 
L e capacitância C em paralelo, a corrente i satisfaz a equação diferencial
didt=Cd2Edt2+1RdEdt+1LE.
Suponha que C=0.2311farads, R=1.3534ohm, L=1.5026henrie e que a tensão seja dada por
E(t)=e−0.0549πtsin(2t−π).
Se i(t0)=i0, com t0=0 e i0=0, use o método de Heun para encontrar estimativas
para a corrente i nos pontos
t1=0.0853, t2=0.124, t3=0.2613, t4=0.3842, t5=0.4704, t6=0.5809, t7=0.6249, 
t8=0.7385, t9=0.8313, t10=0.9542, ...... t149=14.8388 e t150=14.939."""

import numpy as np



def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return y * (1 - x) + x + 2


def g(t, i):
    c = 0.2636
    r = 1.1806
    l = 1.8229

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0549*pi*t) => e_value = 0.0549
    e_value = 0.0599

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.101
    n = 150
    b = 1/2
    t_values = [0.0284, 0.1752, 0.2181, 0.313, 0.4545, 0.5781, 0.6346, 0.7713, 0.8475, 0.9155, 1.0892, 1.1264, 1.2231, 1.3666, 1.481, 1.5704, 1.6806, 1.7403, 1.8686, 1.9692, 2.0105, 2.1792, 2.2619, 2.3529, 2.4694, 2.5325, 2.675, 2.7654, 2.8807, 2.9167, 3.0506, 3.1695, 3.2471, 3.3775, 3.418, 3.546, 3.6193, 3.7354, 3.8444, 3.9642, 4.038, 4.1536, 4.2239, 4.3429, 4.4779, 4.5454, 4.6334, 4.7396, 4.886, 4.9558, 5.0498, 5.1896, 5.2568, 5.3847, 5.4556, 5.5185, 5.6554, 5.7409, 5.8141, 5.9768, 6.0191, 6.1103, 6.2164, 6.3407, 6.4113, 6.5382, 6.6635, 6.7667, 6.8205, 6.9266, 7.0227, 7.1796, 7.219, 7.3206, 7.4768, 7.5696, 7.6389, 7.7854, 7.8851, 7.9352, 8.0883, 8.1414, 8.2419, 8.3216, 8.4738, 8.5195, 8.668, 8.731, 8.8732, 8.9837, 9.0116, 9.1643, 9.2455, 9.3431, 9.4559, 9.5339, 9.6632, 9.7877, 9.8133, 9.9874, 10.0232, 10.1713, 10.2334, 10.344, 10.4636, 10.5182, 10.6825, 10.7841, 10.8264, 10.9756, 11.0283, 11.1646, 11.2287, 11.3592, 11.474, 11.5225, 11.6892, 11.7788, 11.8356, 11.9583, 12.0249, 12.1655, 12.213, 12.3425, 12.4136, 12.5564, 12.6312, 12.7659, 12.8871, 12.926, 13.0567, 13.1195, 13.2667, 13.373, 13.4591, 13.5644, 13.6388, 13.7366, 13.8493, 13.918, 14.059, 14.167, 14.2204, 14.3215, 14.4467, 14.5791, 14.6375, 14.7431, 14.8329, 14.9504]
    """observar o valor de b na função para qual médoto é usado:
    --> b = 1 => metodo = euler_mid
    --> b = 1/2 => metodo = heun
    --> b = 2/3 => metodo = ralston"""
    
    
    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo6 = rk2_h_variavel(g, x0, y0, n, b, t_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo6)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

 