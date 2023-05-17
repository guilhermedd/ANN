import numpy as np
'''
Encontre os coeficientes a e b da função potência y=ax^b que melhor se aproxima da seguinte lista de 12 pontos
(0.6168,1.2651)...
'''

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi**p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi*xi**i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x**b


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':
    x = [0.52, 0.6067, 0.6414, 0.7318, 0.7652, 0.8071, 0.8688, 0.9592, 0.9845, 1.09, 1.1146, 1.1635, 1.2684, 1.3068, 1.3903, 1.4253, 1.5047, 1.527, 1.5728, 1.6792, 1.7167, 1.7501, 1.8559, 1.89, 1.9295, 2.0066, 2.1055, 2.1538, 2.1732, 2.2797, 2.3189, 2.3468, 2.4321, 2.5131, 2.5572, 2.5999, 2.6971, 2.7061, 2.7683, 2.8654, 2.8857, 2.9845]
    y = [0.0793, 0.6627, 0.5971, 1.1942, 0.6896, 1.3488, 1.3098, 2.1786, 2.0209, 2.9222, 4.075, 4.1844, 6.832, 5.8027, 7.5927, 9.1993, 11.1406, 11.031, 10.782, 16.0081, 17.6908, 18.1509, 22.7337, 23.8921, 25.4042, 29.3335, 35.6998, 38.7852, 38.736, 47.373, 50.3466, 52.1633, 59.9521, 65.3217, 71.4319, 76.0381, 85.336, 88.173, 95.7712, 108.4455, 112.9189, 125.999]
    values = [0.7427, 1.3435, 2.0266, 2.0481, 2.4523]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(yt)

    xt = [xi + k2 for xi in x]

    x_ = np.log(xt)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes da potencia')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(f'{q(value)}, ')

    # visualização

   # import matplotlib.pyplot as plt

   # plt.scatter(x, y)

    #t = np.linspace(min(x), max(x), 200)
    #qt = [q(ti) for ti in t]

    #plt.plot(t, qt)

    #plt.savefig('best_poly_regressao_potencia.png')