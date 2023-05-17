"""Encontre os coeficientes do polinômio de grau 4
        p(x)=a0+a1x+a2x2+a3x3+a4x4
que melhor se aproxima da seguinte lista de 38 pontos
(−4.9489,−9.5064), (−4.5742,−4.5547), (−4.2021,−1.1793), (−4.1265,−1.0684), (−3.6553,0.5669), (−3.415,1.2778), (−3.1051,2.8418), (−2.6848,2.0178), (−2.5429,2.7355), (−2.1241,1.9963), (−1.8478,1.2875), (−1.6876,1.4513), (−1.295,0.1971), (−0.9678,−0.511), (−0.8626,−0.1479), (−0.6183,−0.4257), (−0.1375,−0.5845), (0.0162,−0.6345), (0.4125,−0.881), (0.6398,−0.4792), (0.9794,−0.549), (1.0934,0.1588), (1.456,1.8034), (1.7582,1.4119), (2.1345,3.3194), (2.4787,3.4206), (2.6436,4.4766), (2.9558,4.7565), (3.1502,4.861), (3.662,5.1976), (3.7056,5.2142), (4.0513,5.0069), (4.4459,4.5915), (4.8015,1.5513), (5.056,−1.2271), (5.3173,−3.6849), (5.4752,−5.5827) e (5.9987,−15.6477)
Em seguida, calcule p(x) para os seguintes valores de x:
    x=−2.6927, x=−1.5599, x=−0.1812, x=1.483  e  x=3.0327"""

import numpy as np
import math

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)



def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])

def f(a0,a1,a2,a3,a4,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3+a4*x**4

if __name__ == '__main__':
    x = [-4.8599, -4.5148, -4.3732, -4.1041, -3.7839, -3.5242, -2.9742, -2.8318, -2.4937, -2.2297, -2.0353, -1.5274, -1.2977, -1.1545, -0.8975, -0.6173, -0.2976, -0.0296, 0.4512, 0.722, 0.9593, 1.3262, 1.5197, 1.7867, 1.983, 2.3194, 2.8107, 2.8341, 3.1238, 3.6161, 3.745, 4.0347, 4.3892, 4.5534, 4.8684, 5.2244, 5.6599, 5.9431]
    y = [-6.6272, -3.8146, -2.5659, -0.4347, 1.0898, 1.8471, 2.505, 2.6619, 2.4757, 1.8559, 1.7351, 0.7723, 0.8969, 0.1488, -1.4651, 0.1986, -0.8073, -0.3616, -1.26, -0.5916, -1.7006, 0.8516, 0.7775, 1.8092, 1.9091, 2.1414, 3.8797, 4.0257, 5.1326, 4.7047, 4.9988, 4.6891, 3.5942, 2.809, 1.2545, -1.9156, -7.7289, -12.6219]
    values = [-3.0162, 0.6399, 2.7694, 2.84, 5.2488]
    z = []

    a0, a1, a2, a3, a4 = best_poly(x, y, 4) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',',a4,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3,a4, i)) #nao esqueça de colocar aqui tb

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')