from re import A
import numpy as np

#e^(y-b)/a

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p=i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x*np.exp(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


def modelo(x):
    a, b = -40, -30
    erro = a + (b - a) * np.random.random()
    return 2.5 * np.e ** (1.47 * x) + erro

if __name__ == '__main__':

    
    x = [1.46, 2.0068, 2.7268, 3.9628, 4.291, 5.0652, 5.5718, 6.6116, 7.1537, 7.8166, 8.9321, 9.3638]
    y = [2.0086, 2.4124, 2.9806, 3.4347, 3.5626, 3.9692, 4.1121, 4.3111, 4.3049, 4.5117, 4.6365, 4.7432]
    values = [3.56, 5.374, 5.8363] # x1, x2


    #transladar os pontos para cima
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    x_ = np.log(x)

    y_ = y

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    #print(f'{a0 = } e {a1 = }')

    a = a1
    b = a0

    print(f'{a = } e {b = }')

    n = len(values)
    somas = []
    for xi in range(n):
        print(f'{a0+a1*np.log(values[xi])}, ')

    p = build_func(a, b)

    def q(x):
        return p(x) - k


'''   import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt, color='r')
    plt.savefig('best_exp.png')'''