def lagrange(x,y):
    #retorna yi dividido pelo denominador do polinomio Li
    num=len(x)
    coefs = []
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(x[i] - x[j])
        ci=y[i]/prod
        coefs.append(ci)
    return coefs

def pl(t,x,coefs) -> float:
    soma=0
    num = len(coefs)
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(t-x[j])
        prod*= coefs[i]
        soma+=prod
    return soma


def poly(x, coefs):
    def f(t):
        return pl(t,x, coefs)
    return f


if __name__ == '__main__':
    x=[1.039, 1.577, 2.877]
    y=[1.457, 1.943, 0.16]
    
    # x=[-0.691, 0.247, 0.681]
    # y=[0.07729752396, 0.39600431644 ,0.07940273264]
    
    # x=[1,3]
    # y=[1,-1]
    c = lagrange(x,y)
    print(c)
    lagr=poly(x, c)
    # print(lagrange(x, y))
    print(lagr(0))