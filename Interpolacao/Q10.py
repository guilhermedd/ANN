import math
import numpy as np

def lagrange(x, y):
    for i in range(len(x)):
        a = 1
        for j in range(len(x)):
            if i != j:
                a *= (x[i]-x[j])
        print(y[i]/a, ",")


if __name__ == '__main__':
    # x = [-1.823, -0.45, 0.724, 1.497, 2.787, 3.853, 5.34, 6.035]  # coordenadas x do ponto
    # y = [0.564, 0.967, 0.941, 0.732, -0.161, -0.891, -0.611, 0.007]  # coordenadas y do ponto

    x = []
    y = []
    z = [1.641, 4.729, 8.001]  #o valor dado na questão que é a lista x substitui em z mesmo

    def f(x):
        return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)

    for i in z:
        x.append(i)
        y.append(f(i))

    lagrange(x, y)