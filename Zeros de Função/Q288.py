import math
import sympy as sp

def g(x,t):
    3427673 * math.exp(x*t) + 254902 * math.exp(x*t)/x - 254902/x

def dg(x_value):
    x = sp.symbols('x')
    derivative = sp.diff(f, x)
    return derivative.subs(x, x_value).evalf()
     

def falsePositionAux(f, a, b,n):
    fa = abs(f(a,n))
    fb = abs(f(b,n))
    return (a*fb + b*fa)/(fa + fb)

def falsePosition(f, a, b, n):
    if(f(a,n)*f(b,n) > 0): 
        return

    for i in range(n):
        x = falsePositionAux(f, a, b,n)
        
        if(f(a,n)*f(x,n) < 0): 
            b = x
        else: 
            a = x

    print("%.17f" %(x))

def newton(f, df, m, n):

    for i in range(n):
        if(df(m) == 0): return
        m = m - (f(m,n)/df(m,n))
    
    print(m)

def bisection(f, a, b, n):
    if(f(a,n)*f(b,n) > 0):
        return
    for i in range(n):
        m = (a+b)/2
        if(f(a,n)*f(m,n) < 0):
            b = m
        else: 
            a = m
    
    print("%.17f"%(m))

def aproximateDerivative(f, x1, x0):
    return (f(x1)-f(x0))/(x1-x0)

def secante(f, x1, x0, n):
    for i in range(n):
        x2 = x0 - f(x0)/aproximateDerivative(f, x1, x0)
        #x2 = (x0*f(x1) - x1*f(x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
    print(x2)

print("\nPelo método da bisseção")
# Pelo método da bisseção:
a = 0.5
b = 57.37
vetor = [2, 4, 8, 12]
for n in vetor: bisection(g, a, b, n)

print("\nPelo método de Newton")
# Pelo método de Newton:
x_0 = 0.53
vetor = [1, 3, 5]
for n in vetor: newton(g, dg, x_0, n)

print("\nPelo método da secante")
# Pelo método da secante:
x_0 = 1.93
x_1 = 19.96
vetor = [1, 2, 5]
for n in vetor: secante(g, x_1, x_0, n)

print("\nPelo método da posição falsa")
# Pelo método da posição falsa:
a = 1.77
b = 55.28
vetor = [2, 4, 7, 11]
for n in vetor: falsePosition(g, a, b, n)