import math

# funçao f
def f(x):
    return  x * (x - 1) * (x - 2) + 0.42

# derivada da funçao f
def df(x):
    return 3*(x**2) - 6*x + 2

# algoritmo metodo de newton
def newton(f, df, x0, iterations, n):
    for i in range(n):
        fx0 = f(x0)
        dfx0 = df(x0)
        if dfx0 == 0: break
        x1 = x0 - fx0/dfx0
        #print("x {} = {:.16f}".format(i + 1, x1))
        if i + 1 in iterations:
            print("{:.7f},".format(x1))
        x0 = x1

x0 = 3.10731694
iterations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
n = max(iterations)
newton(f, df, x0, iterations, n)
