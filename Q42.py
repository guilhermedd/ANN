import math


def bisection(f, a, b, lista):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
        n = max(lista)
        for k in range(n):
            m = 0.5 * (a + b)
            if (k + 1) in lista:
                print(f"{m:.7f},")
            fm = f(m)
            if fm == 0:
                print(f"Encontrei uma raiz em x_{k + 1}={m}")
                return
            if fa * fm < 0:
                b = m
            else:
                a = m
                fa = fm


def newton(f,df,x0,lista):
    n = max(lista)
    raiz = x0
    for i in range(n):
        if df(raiz) != 0: # se a derivada for zero sai    
            raiz=raiz-f(raiz)/df(raiz)
        if (i + 1) in lista:
            print(f"{raiz:.7f},")
#        if(raiz == 0):
#          print(f"Encontrei uma raiz em x_{i + 1}={raiz}");
    return 


def secante(f,x_0, x_1, lista):
    n = max(lista)
    raiz = x_0
    for i in range(n):
        if f(x_0) - f(x_1) != 0: # se a derivada for zero sai    
            raiz= (x_0*f(x_1) - x_1*f(x_0)) / (f(x_1) - f(x_0))
        if (i + 1) in lista:
            print(f"{raiz:.7f},")
        
        x_0 = x_1
        x_1 = raiz
    return 


def pos_falsa(f, a, b, lista):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
        n = max(lista)
        for k in range(n):
            x1 = (a*f(b) - b*f(a)) / (f(b) - f(a))

            if (k+1) in lista:
                print(f"{x1:.7f},")
            if f(a)*f(x1) < 0:
                a, b = a, x1
            if f(x1)*f(b) < 0:
                a, b = x1, b
    return 
"""
#Q28 CALCULO DA POPULAÇÃO
P_0 = 1863409
P_1 = 3463185
v = 101698
# x = lambda
def P(x):
    result = P_0*math.exp(x) + (v/x)*(math.exp(x)-1) - P_1
    return result.real
def dP(x):
    result = P_0*math.exp(x) + (v/x)*math.exp(x) - (v/(x**2))*math.exp(x) + v/(x**2)
    return result.real
print('b')
bisection(P, 0.1, 1.67, [2,4,8,12])
print('n')
newton(P, dP, 1.48, [1,3,5])
print('s')
secante(P, 0.1, 1.35, [1,2,5])
print('p')
pos_falsa(P, 0.1, 1.06, [2,4,7,11])
"""

"""
#Q29 CALCULO DA MASSA
G = 9.81
t = 8.36
c = 24.23
v = 34.0
# x = lambda
def g(x):
    result =  G*x/c - (G*x/c)*math.exp(-c*t/x) - v
    return result.real
def dg(x):
    result = G*(1 - math.exp(-c*t/x)*(c*t+x)/x)/c
    return result.real
print('b')
bisection(g, 20.21, 195.56, [2,4,8,12])
print('n')
newton(g, dg, 28.77, [1,3,5])
print('s')
secante(g, 22.82, 34.34, [1,2,5])
print('p')
pos_falsa(g, 20.64, 189.03, [2,4,7,11])
"""

"""
#Q30 CALCULO DO COEF DE ARRASTO
G = 9.81
t = 9.94
m = 83.85
v = 47.31
# x = lambda
def g(x):
    result = G*m/x - (G*m/x)*math.exp(-x*t/m) - v
    return result.real
def dg(x):
    result = -G*m/(x**2) + (G*t/x)*math.exp(-x*t/m) + (G*m/(x**2))*math.exp(-x*t/m)
    return result.real
print('b')
bisection(g, 1.09, 53.02, [2,4,8,12])
print('n')
newton(g, dg, 0.51, [1,3,5])
print('s')
secante(g, 1.82, 18.58, [1,2,5])
print('p')
pos_falsa(g, 1.25, 50.38, [2,4,7,11])
"""

"""
#Q31 CÁLCULO DA PROFUNDIDADE CILINDRO
v = 8.65
g = 9.81
t = 6.2
L = 9.22
H = lambda x: math.sqrt(2*g*x)*math.tanh(math.sqrt(2*g*x)*t/(2*L)) - v
def sech(x):
    result = 1/(math.cosh(x))
    return result.real
dH = lambda x: (g/2)*( math.sqrt(2)*math.tanh(t*math.sqrt(g*x)/math.sqrt(2)*L)/math.sqrt(g*x) + (t*sech(t*math.sqrt(g*x/2)/L)**2/L))
print('b')
bisection(H, 0.46, 17.91, [2,4,8,12])
print('n')
newton(H, dH, 0.58, [1,3,5])
print('s')
secante(H, 1.46, 16.85, [1,2,5])
print('p')
pos_falsa(H, 0.01, 19.87, [2,4,7,11])
"""

"""
#Q32 CANAL TRAPEZIODAL ALTURA
Q = 136.52
g = 9.81
def A(y):
    return 5.66*y + (y**2)/2
def L(y):
    return 5.66 + y
def f(y):
    result = 1 - L(y)*(Q**2)/(g*(A(y)**3))
    return result.real
def df(y):
    result = -((Q**3)/g)*((-3*L(y))/(A(y)**4) + A(y)**(-3)) 
    return result.real
print('b')
bisection(f, 0.78, 9.53, [2,4,8,12])
print('p')
pos_falsa(f, 0.35, 8.69, [2,4,7,11])
"""

"""
#Q33 ALTURA TANQUE ESFÉRICO
V = 49.56
R = 3.73
def f(x):
    result = math.pi*(x**2)*R - (math.pi/3)*(x**3) - V
    return result.real
def df(x):
    result = 2*math.pi*x*R - math.pi*(x**2)
    return result.real
print('b')
bisection(f, 0, 7.46, [2,4,8,12])
print('n')
newton(f, df, 4.14, [1,3,5])
print('s')
secante(f, 1.55, 6.75, [1,2,5])
print('p')
pos_falsa(f, 0, 7.46, [2,4,7,11])
"""

"""
#Q34 PRINCÍPIO DE ARQUÍMEDES ESFERA
r = 6.4
ps = 408.27
pw = 1000
def f(x):
    return pw*((4/3)*(r**3) - (x**2)*r + (x**3)/3)- ps*(4*(r**3)/3)
def df(x):
    result = pw*( -2*x*r + x**2)
    return result
print('b')
bisection(f, 0, 12.8, [2,4,8,12])
print('n')
newton(f, df, 6.72, [1,3,5])
print('s')
secante(f, 2.62, 10.09, [1,2,5])
print('p')
pos_falsa(f, 0, 12.8, [2,4,7,9])
"""

"""
#Q35 PRINCÍPIO DE ARQUÍMEDES TRONCO DE CONE
r1 = 1.44
r2 = 7.55
H = 7.97
pt = 476.34
pw = 1000
x = (H*r1)/(r2-r1)
def f(h):
    return pt*H*((r1**2) + (r2**2) + (r1*r2)) - pw*(H-h)*((r1**2) + 2*(r1**2)*h/x + (h**2)*(r1**2)/(x**2) + (r2**2) + (r1*r2) + (h*r1*r2)/x)
def df(h):
    result = -pw*(H-h)*(2*(r1**2)/x + 2*h*(r1**2)/(x**2) + (r1*r2)/x) + pw((r1**2) + 2*(r1**2)*h/x + (h**2)*(r1**2)/(x**2) + (r2**2) + (r1*r2) + (h*r1*r2)/x) 
    return result
print('b')
bisection(f, 0, 7.97, [2,4,8,12])
print('n')
secante(f, 0.1, 6.58, [1,2,5])
print('p')
pos_falsa(f, 0, 7.97, [2,4,7,11])
"""

"""
#Q36 COCHO
r = 4.97
L = 8.83
V = 265.64
def f(h):
    result = L*((0.5*math.pi*(r**2)) - (r**2)*math.asin(h/r) - h*(math.sqrt((r**2) - (h**2)))) - V
    return result.real
print('b')
bisection(f, 0, 4.97, [2,4,8,12])
print('n')
secante(f, 0.22, 3.86, [1,2,5])
print('p')
pos_falsa(f, 0, 4.97, [2,4,7,11])
"""

"""
#Q37 PLANO INCLINADO
g = 9.81
x = 4.36
t = 1.08
f = lambda w: -(g/(2*(w**2)))*(math.sinh(w*t) - math.sin(w*t)) -x
df = lambda x: g*(-2*math.sin(t*x)+t*x*math.cos(t*x)+2*math.sinh(t*x)-t*x*math.cosh(t*x))/(2*(x*x*x))
print('b')
bisection(f, -5.09, 0.36, [2,4,8,12])
print('n')
newton(f, df, -1.82, [1,3,5])
print('s')
secante(f, -4.6, -1.89, [1,2,5])
print('p')
pos_falsa(f, -5.43, 0.89, [2,4,7,11])
"""

"""
#Q38 MONTAR UMA CAIXA
A = 15.14
B = 9.65
# x = lambda
def f(l):
    result = A*B - 4*l*A - 4*l*B + 12*(l**2)
    return result.real
def df(l):
    result = -4*A -4*B + 24*l
    return result.real
print('b')
bisection(f, 0, 4.83, [2,4,8,12])
print('n')
newton(f, df, 2.42, [1,3,5])
print('s')
secante(f, 1.04, 4.06, [1,2,5])
print('p')
pos_falsa(f, 0, 4.83, [2,4,7,11])
"""

"""
#Q39 POPULAÇÃO CONTAGIADA POR GRIPE
n = 105839731
l = 1.41e-10
f = lambda t: (n+1)/(1+n*math.exp(-l*(n+1)*t)) - n*0.25
a = 0
b = 2477
print('b')
bisection(f, a, b, [2,4,8,12])
print('p')
pos_falsa(f, a, b, [2,5,7])
"""


#Q42 CÁLCULO DA DISTÂNCIA A PARTIR DA CONSERVAÇÃO DE ENERGIA

k1 = 59100
k2 = 71
m = 106
g = 9.81
h = 0.85

f = lambda d: 2*k2*pow(d, 5/2)/5 + k1*d**2/2 - m*g*d - m*g*h
df = lambda d: k2*pow(d, 3/2) + k1*d - m*g

# print('b')
bisection(f, 0, 1.52, [1,4,7,10])
# print('n')
newton(f, df, 0.82, [1,3,6])
# print('s')
secante(f, 1.17, 1.82, [1,2,5,8])
# print('p')
pos_falsa(f, 0, 1.39, [2,5,7,11])