import numpy as np

#a*2^(bx)

def best_poly(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * 2 ** (b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.0278, 0.2391, 0.4063, 0.5246, 0.787, 0.8515, 1.0454, 1.3126, 1.4339, 1.5746, 1.7955, 1.931]
    y = [4.9933, 6.5281, 9.4012, 10.4222, 20.329, 23.2308, 34.4856, 57.2641, 74.2364, 98.3647, 150.6253, 194.7234]
    values = [0.2925, 0.5137, 0.7155]
    y_ = np.log(y)
 
    grau = 1

    a0, a1 =  best_poly(x, y_, grau)

   # print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1

    print(f'{a = } e {b = }')

    p = build_func(a, b/np.log(2))


    
    for xi_v in values:
        print(f'{p(xi_v)}, ')
        
        
"""Encontre os coeficientes a e b da função exponencial y=aebx que melhor se aproxima da seguinte lista de 12 pontos
(0.1346,4.6201), (0.3274,8.4424), (0.4946,12.0172), (0.5763,13.9066), (0.7828,17.5688), (0.8358,22.9029), (1.1293,35.3308), (1.3232,52.7761), (1.4635,65.8886), (1.5397,78.7052), (1.6776,99.6252) e (1.9197,150.9273)
Em seguida, calcule o valor de y para os seguintes valores de x:
x=0.1659, x=1.8411  e  x=1.8708"""