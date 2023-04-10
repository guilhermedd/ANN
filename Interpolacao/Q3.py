from weakref import ProxyTypes
import numpy as np


def poly(x,y):
    n = len(x)-1
    A =[]
    B =[]
    for xi in x:
        row = [1]
        for j in range(1, n+1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A, y)

def func_poly(x, coeffs):
    first=coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])

if __name__ == '__main__':
    #exemplo 1

    x=[0.419, 0.965, 1.346, 1.918, 2.858, 3.129, 3.642, 4.454, 4.807, 5.506, 6.01, 6.94]
    y=[4.401, 4.791, 4.914, 4.818, 4.008, 3.686, 3.078, 2.372, 2.234, 2.288, 2.526, 3.005]

    coeffs = poly(x,y)
    #print(coeffs)

    for x in (coeffs):
        print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)

#    print("%.16f" %p(4.879))
 #   print("%.16f" %p(5.113))
  #  print("%.16f" %p(5.202))




#visulaizar
#import matplotlib.pylab as plt

#plt.scatter(x,y)
#t = np.linspace(min(x),  max(x), 200)
#pt = [p(ti) for ti in t]

#função seno
# st=np.sin(t)
# plt.plot(t, pt)
# plt.plot(t, st)

#plt.plot(t, pt)
#plt.savefig('interp.png')