"""A tabela a seguir mostra leituras do velocímetro de um carro, durante um período de 60.0 
segundos, numa corrida na Daytona International Speedway, Flórida."""

import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'Area aproximadamente: {soma}')

#def f(x):
 #   return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'{somas}')


x = [0.0, 5.0/3600, 10.0/3600, 15.0/3600	,20.0/3600	,25.0/3600	,30.0/3600	,35.0/3600	,40.0/3600	,45.0/3600	,50.0/3600	,55.0/3600	,60.0/3600	]
y = [213.3 ,142.07,108.8,184.44,120.25,240.68,263.28,286.53,199.35,232.78,157.36,174.23,281.14]


trapzPonto(x, y)