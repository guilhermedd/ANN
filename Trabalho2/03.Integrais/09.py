'''A seguinte lista de 21 pontos
(0.293,2.226), (0.762,2.999), (1.231,2.557), (1.686,2.098), (2.141,2.02), 
(2.2745,2.075), (2.408,2.166), (2.556,2.304), (2.704,2.476), (2.749,2.532), 
(2.794,2.589), (2.925,2.755), (3.056,2.898), (3.271,2.999), (3.486,2.804), 
(3.5355,2.706), (3.585,2.589), (3.96,1.356), (4.335,1.261), (4.645,2.654) e (4.955,2.639)
vive no gráfico de uma função f. Use a regra de Simpson para aproximar a 
área embaixo do gráfico de f no intervalo [0.293,4.955].'''

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')


x = [0.235, 0.8735, 1.512, 1.886, 2.26, 2.5025, 2.745, 2.825, 2.905, 3.0945,
     3.284, 3.504, 3.724, 3.7725, 3.821, 3.8295, 3.838, 3.864, 3.89, 4.423, 4.956]
y = [2.026, 2.955, 2.236, 2.013, 2.068, 2.25, 2.527, 2.629, 2.73, 2.931,
     2.997, 2.77, 2.169, 2.0, 1.826, 1.796, 1.766, 1.673, 1.583, 1.599, 2.634]


simpsPonto(x, y)