"""Encontre os coeficientes do polinômio de grau 5
    p(x)=a0+a1x+a2x2+a3x3+a4x4+a5x5
que melhor se aproxima da seguinte lista de 41 pontos
(−4.3929,−3.9203), (−4.1223,−1.2143), (−3.9842,−0.2167), (−3.8212,0.312), (−3.4309,2.9508), (−3.2041,2.2278), (−3.1505,2.171), (−2.878,1.6819), (−2.5818,1.3871), (−2.4781,0.8082), (−2.1317,−0.7085), (−2.0052,0.087), (−1.7134,−0.2822), (−1.5571,−0.8963), (−1.2188,−0.6741), (−1.0109,−0.7167), (−0.8693,−0.6959), (−0.7269,−0.5353), (−0.3605,−0.5241), (−0.1158,−0.0925), (−0.04,−0.0432), (0.3285,0.513), (0.3485,0.333), (0.6673,0.6511), (0.9559,0.9799), (1.1838,1.0884), (1.2594,0.9756), (1.6323,0.5102), (1.6705,0.7575), (2.0398,0.1408), (2.2986,0.3369), (2.5218,−1.5442), (2.688,−2.5904), (2.78,−1.0592), (3.0102,−1.9569), (3.2074,−2.065), (3.4105,−3.2242), (3.6498,−1.431), (3.8785,−1.0431), (4.1274,2.0409) e (4.3616,4.5214)
Em seguida, calcule p(x) para os seguintes valores de x:
    x=−3.5521, x=−3.3737, x=0.4938, x=0.5037  e  x=2.0214
"""

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

def f(a0,a1,a2,a3,a4,a5,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3+a4*x**4+a5*x**5

if __name__ == '__main__':
    x = [-4.3467, -4.1158, -3.9037, -3.6958, -3.5859, -3.2499, -3.0068, -2.7749, -2.5473, -2.5019, -2.1601, -2.0693, -1.7979, -1.6406, -1.3995, -1.052, -0.9628, -0.6466, -0.4516, -0.1887, -0.0189, 0.2614, 0.5249, 0.6328, 0.7787, 1.1549, 1.2206, 1.4388, 1.7726, 1.9326, 2.1702, 2.386, 2.6525, 2.9312, 3.0742, 3.3419, 3.4254, 3.6574, 3.9743, 4.1544, 4.3225]
    y = [-2.4513, -0.5316, 0.291, 1.3365, 1.2481, 1.8924, 1.564, 0.488, 1.3753, 0.8075, 0.1061, -1.5694, -0.1204, -0.5581, 0.4673, -0.6019, -0.7938, -1.4012, 1.5056, -0.2282, 0.0235, 0.2807, 0.3272, 0.3074, 0.7523, 0.4822, 1.6642, 0.5418, 0.3078, 0.5917, -0.6935, -0.5876, -1.243, -2.2726, -1.345, -1.6974, -1.5513, -1.1777, -0.1694, 0.9048, 1.5457]
    values = [-2.9969, -2.9398, -1.9265, -1.777, 4.282]
    z = []

    a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',',a4,',',a5,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3,a4,a5, i)) #nao esqueça de colocar aqui tb

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')