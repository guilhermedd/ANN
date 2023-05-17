"""Encontre os coeficientes da parábola
        p(x)=a0+a1x+a2x2
que melhor se aproxima da seguinte lista de 36 pontos
    (0.0444,5.7912), (0.5041,5.4625), (0.7308,5.3431), (1.0678,4.9996), (1.2885,4.6561), (1.6037,4.7264), (1.6668,4.8078), (2.0258,4.5855), (2.3293,4.1601), (2.5123,4.1244), (2.9969,3.8997), (3.098,3.6425), (3.5293,3.6673), (3.625,3.6749), (4.1475,3.5592), (4.3702,3.5189), (4.4522,3.5053), (4.8559,3.5051), (5.204,3.3781), (5.5368,3.4576), (5.5739,3.3949), (5.8534,3.46), (6.2876,3.4834), (6.4591,3.5174), (6.8598,3.5598), (6.9878,3.5904), (7.2971,3.6523), (7.6468,3.6904), (8.0542,4.0192), (8.0733,4.0132), (8.5871,4.2154), (8.7104,4.315), (8.914,4.4469), (9.2396,4.6732), (9.7179,5.2456) e (9.7989,5.3356)
Em seguida, calcule p(x) para os seguintes valores de x:
    x=0.2248, x=3.9807, x=4.2423, x=8.6162  e  x=9.664"""

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

def f(a0,a1,a2,x):
    return a0+a1*x+a2*math.pow(x,2) #mudar se necessario

if __name__ == '__main__':
    x = [0.1168, 0.4067, 0.7885, 0.9152, 1.2473, 1.5756, 1.6778, 2.0285, 2.4071, 2.5751, 2.8938, 3.1007, 3.4013, 3.8677, 3.9614, 4.3071, 4.524, 4.7283, 5.0485, 5.5427, 5.6789, 6.0341, 6.3126, 6.5641, 6.9055, 7.0477, 7.2884, 7.6909, 7.9253, 8.1079, 8.5567, 8.8662, 8.9654, 9.2951, 9.484, 9.9365]
    y = [5.9064, 5.6768, 5.3467, 5.5419, 5.1454, 4.9531, 4.8864, 4.5297, 4.5487, 4.4025, 4.3378, 4.2632, 4.1973, 4.0475, 4.1062, 3.8856, 4.0453, 3.9757, 4.0029, 3.7305, 4.0626, 4.1114, 4.0872, 4.1995, 4.3142, 4.4982, 4.8623, 4.5666, 4.6834, 4.7222, 4.9848, 5.1427, 5.246, 5.5822, 5.5501, 5.7271]
    values = [0.2196, 1.2275, 3.5214, 6.1144, 6.7644]
    z = []

    a0, a1, a2 = best_poly(x, y, 2) #2 é o grau da parabola
    
    print(a0, ',', a1,',',a2,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')