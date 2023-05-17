"""Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=1.27502 e y0=0.40276. Use o método de Ralston para estimar 
o valor da solução exata desse PVI nos pontos
x1=1.29926, x2=1.36265, x3=1.39941, x4=1.44869, x5=1.50579, x6=1.5644, 
x7=1.59091, x8=1.64149, x9=1.69974, x10=1.74931, x11=1.78936, x12=1.83277, 
x13=1.91358, x14=1.94088, x15=2.01872, x16=2.05629, x17=2.11855, x18=2.14775, 
x19=2.18381 e x20=2.25921."""

def ralston_h_variavel(f, x0, y0, n,b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
     vals = []
     for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + 3/4 *h, y0 + m1 *3/4 * h )
        y0 += (1 *m1 + m2*2)*h/3
        x0 += h
        vals.append([x0, y0])
     return vals

#Q10 Prova:
def f(x,y):
    return y * (2 - x) + x + 1

n = 20
b = 2/3
x0 = 1.64195
y0 = 2.98337
x_values = [1.66372, 1.72527, 1.77705, 1.81063, 1.85619, 1.93557, 1.96601, 2.01033, 2.06137, 2.12112, 2.15414, 2.20865, 2.2528, 2.2995, 2.36817, 2.42115, 2.45596, 2.51449, 2.56109, 2.61722]
e = ralston_h_variavel(f,x0,y0,n, b, x_values)
for xi, yi in e:
    print(f'{yi},')