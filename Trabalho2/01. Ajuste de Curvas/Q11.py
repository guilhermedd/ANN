from ntpath import join
from traceback import print_last
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

def matriz_Coeffs(x,y,k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
    return A

def matrix_TermosIndepents(x,y,k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    B = []
    for i in range (k + 1):
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return B

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
    x = [0.8, 1.5051, 2.1595, 2.5768, 3.4199, 4.284, 5.239, 6.1181, 6.7453, 7.9122, 8.6749, 9.4409]
    y = [4.7801, 4.2617, 3.8243, 3.6523, 3.3944, 3.144, 3.087, 3.2255, 3.4398, 4.0406, 4.5185, 5.1021]
    values = [5.0291, 5.3835, 7.5179]   
    z = []

    a0, a1, a2 = best_poly(x, y, 2) #2 é o grau da parabola
    
    #print(a0, ',', a1,',',a2,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    #
    print('\**nRetire os colchetes somente e coloque virgulas quando necessario**')
    A = matriz_Coeffs(x,y,2)
    print(*A,sep=','+'\n')

    print(a0, ',', a1,',',a2,',')

    B = matrix_TermosIndepents(x,y,2)
    print(*B,sep=', ')

    for i in values:
        print(p(i,coefs),',')