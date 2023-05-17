import math

def richardson(col_1):
    n = len(col_1)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]

if __name__ == '__main__':

    #exemplo 1

    def func(x):
        return x**2*math.tan(math.sin(x/math.pi))

    h = 0.30262
    x0 = -1.97127
  
    err_order = [2,3,4,5,6]

    def F1(h):
        return (func(x0 + h) - func(x0)) / h
    for i in range(len(err_order)):
        hs = [h, h/2, h/4, h/8]
        col_F1 = [F1(h/2**i) for i in range(err_order[i])]

        approx = richardson(col_F1)

        print(f'{approx}, ')

    richardson(col_F1)