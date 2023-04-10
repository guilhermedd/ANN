def dif_div(x, y):
    num = len(x)
    Y = [yi for yi in y]
    coefs = [y[0]]
    for j in range(num -1):
        for i in range(num - 1 - j):
            numerador = Y[i + 1] - Y[i]
            denominador = x[i + 1 + j] - x[i]
            div = numerador / denominador
            Y[i] = div
        coefs.append(Y[0])
    return coefs

def poly(t, x, coefs):
    val = 0
    num = len(coefs)
    for i in range(num):
        prod = 1
        for j in range(i):
            prod *= (t - x[j])
        val += coefs[i] * prod
    return val

def build_func(x, coefs):
    def temp(t):
        return poly(t, x, coefs)
    return temp


if __name__ == '__main__':

    #ex
    
    x = [0.191, 0.803, 1.127, 1.534, 2.005, 2.713, 3.133, 3.634, 4.054, 4.271, 5.008, 5.42, 5.714, 6.407, 6.864]
    y = [4.946, 4.219, 3.71, 3.132, 2.597, 2.091, 2.0, 2.119, 2.388, 2.573, 3.291, 3.65, 3.842, 3.992, 3.836]

    coefs = dif_div(x, y)

    #polinomio interpolador da lista de pontos
    p = build_func(x, coefs)

    print(coefs)