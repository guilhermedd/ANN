import math

# define a função do volume
def V(l):
    return l * (16.53 - 2*l) * (9.18 - 2*l)

# define o intervalo inicial e a precisão desejada
a = 0
b = 4.59
tolerance = 0.0001

# aplica o método da bisseção
for i in [2, 4, 8, 12]:
    n = 0
    while (b - a) / 2 > tolerance and n < i:
        c = (a + b) / 2
        if V(c) == 0:
            break
        elif V(c) * V(a) < 0:
            b = c
        else:
            a = c
        n += 1
    print("Iterações: {}, Lado: {}, Volume: {}".format(n, c, V(c)))

def f(x):
    return (16.53-2*x)*(9.18-2*x)*x

def f_deriv(x):
    return -6*x**2 + 52.62*x - 148.944

def newton_method(f, f_deriv, x0, epsilon, max_iter):
    i = 0
    while abs(f(x0)) > epsilon and i < max_iter:
        x0 = x0 - f(x0)/f_deriv(x0)
        i += 1
    return x0, i

x0 = 2.82
epsilon = 1e-6
max_iter = 5

root, num_iter = newton_method(f, f_deriv, x0, epsilon, max_iter)

print("Raiz encontrada:", root)
print("Número de iterações:", num_iter)

def f(x):
    return (16.53-2*x)*(9.18-2*x)*x

def secant_method(f, x0, x1, epsilon, max_iter):
    i = 0
    while abs(f(x1)) > epsilon and i < max_iter:
        x2 = x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))
        x0 = x1
        x1 = x2
        i += 1
    return x1, i

x0 = 0.9
x1 = 3.68
epsilon = 1e-6
max_iter = 5

root, num_iter = secant_method(f, x0, x1, epsilon, max_iter)

print("Raiz encontrada:", root)
print("Número de iterações:", num_iter)

def f(x):
    return (16.53-2*x)*(9.18-2*x)*x

def false_position_method(f, a, b, epsilon, max_iter):
    i = 0
    while abs(f(b)) > epsilon and i < max_iter:
        c = (a*f(b) - b*f(a))/(f(b) - f(a))
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
        i += 1
    return b, i

a = 0
b = 4.59
epsilon = 1e-6
max_iter = 11

root, num_iter = false_position_method(f, a, b, epsilon, max_iter)

print("Raiz encontrada:", root)
print("Número de iterações:", num_iter)


