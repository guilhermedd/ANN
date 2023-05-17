import math
import numpy as np



def euler_mid(f, x0, y0, x_values, n):
    vals = []
    for k in range(n):
        if k == 0:
            h = x_values[0] - x0
        else:
            h = x_values[k] - x_values[k-1]
        
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += + h * m2
        x0 += + h
        print(f'{y0},')
        vals.append([x0, y0])
    return vals

if __name__ == '__main__':

    #def f(x, y):
    #     return k*y

    #x0, y0 = 0.0, 1185514 # x0 = t, y0 = indivíduos
   # h = 0.0625
    #n = int(1/h)
    #k = 0.0712

    #P3.7
    def f(x, y):
        return y*(2 - x) + x + 1

    x0 = 0.97468
    y0 = 0.70898
    x_values = [1.01746, 1.06905, 1.09132, 1.14606, 1.21461, 1.26336, 1.3159, 1.33167, 1.38879, 1.45183, 1.51419, 1.55778, 1.59887, 1.63037, 1.71536, 1.7505, 1.8184, 1.83258, 1.89336, 1.9509]
    n = 20
    resposta = euler_mid(f, x0, y0, x_values, n)

    # def y(x):
    #     return 5 * math.exp(x - 1) - x - 2

    # t = np.linspace(x0, x0 + n * h, 100)
    # yt = [y(i) for i in t]

    # cx, cy = zip(*resposta)
    # plt.plot(t, yt)
    # plt.scatter(cx, cy)
    # plt.show()
