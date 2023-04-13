def bisection(f, a, b, n):
  fa, fb = f(a), f(b)
  if fa * fb >= 0:
    print(
      "Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo."
    )
  else:
    for k in range(n):
      m = 0.5 * (a + b)
      fm = f(m)
      if fm == 0:
        print(f"Encontrei uma raiz em x_{k + 1}={m}")
        return
      if fa * fm < 0:
        b = m
      else:
        a = m
        fa = fm
    print(f"{m},")
  return
  


T = [450, 1250, 1650]
p = [40, 50, 70]
R = 0.08205736608096

a = [5.3457287, 3.1892131]
b = [0.06504, 0.0487]

n = 50
ac = 0.001
bc = 200

def newton(f, df, m, n):

    for i in range(n):
        if(df(m) == 0): return
        m = m - (f(m,n)/df(m,n))
    
    print(m)

def df(v):
    -1 * (p + 2*a/v**2) + 2 * a * b/v**3

for i in range(len(T)):
  for j in range(len(p)):
    g = R * T[i] / p[j]
    print(f"{g},")
    for k in range(len(a)):
      vw = lambda v: R * T[i] - (p[j] + a[k] / v**2) * (v - b[k])
    #   newton(vw, df, 80, 20)
      bisection(vw, ac, bc, n)