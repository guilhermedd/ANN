import math

'''Use o método de Romberg, com o h indicado, para encontrar uma aproximação 
com erro O(hk) para as integrais a seguir:'''

def trapz(nome_funcao, a, b, h):
    n = int((b-a)/h)
    soma = 0

    for k in range(1, n):
        soma += f(nome_funcao, a+k*h)

    return (h/2)*(f(nome_funcao, a) + 2*soma + f(nome_funcao, b))


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n-1):
        temp_col = [0] * (n-1-j)
        for i in range(n-1-j):
            power = j+1
            temp_col[i] = (4**power*coluna_f1[i+1]-coluna_f1[i])/(4**power-1)
        coluna_f1[:n-1-j] = temp_col
        #print(f'F_{j+2} = {temp_col}')
    return coluna_f1[0]




def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)


if __name__ == '__main__':
    func = ['math.cos(-x**2/3)', 'math.exp(x)*math.sin(x)/(1+x**2)', '(x+1/x)**2', 'math.sqrt(1+x**2)', 'math.exp(-x**2)']
    a = [0.908, 0.763, 0.616, 0.407, -1.169]
    b = [1.908, 1.763, 1.616, 1.407, -0.169]
    order = [8, 10, 8, 6, 8]
    n = [3, 5, 4, 5, 5]

    for i in range(len(func)):
        k = int(order[i]/2)
        h = float((b[i]-a[i])/n[i])
        hs = [h/2**i for i in range(k)]
        col1=[trapz(func[i],a[i],b[i],hi) for hi in hs]

       # print(f'F_1 = {col1}')

        r = romberg(col1)

        print(f'{r}, ')