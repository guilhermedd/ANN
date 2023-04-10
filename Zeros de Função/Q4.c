#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define SIZE 20

void bis(double(*f)(double), double a, double b, int n, int s, int p[], tol)
{
    int iteracao = 1;
    double fa = f(a);
    double fb = f(b);
    if(fa * fb >= 0)
    {
        printf("Voce nao pode usar esse intervalo\n");
        return;
    }
    else
    {
        int i2 = 0;
        for(int i = 0; i < n; i++)
        {
            if(i2 <= s)
            {
                double m = 0.5 * (a + b);
                double fm = f(m);
                if(fm <= tol)
                {
                    printf("Voce encoutrou uma raiz r=%.16f\n", m);
                    return;
                }
                if(p[i2] == iteracao)
                {
                    printf("%i interacoes e m = %.7f,\n", iteracao, m);
                    i2++;
                }
                iteracao++;
                if(fa * fm < 0)
                {
                    b = m;
                }
                else
                {
                    a = m;
                    fa = fm;
                }
            }
        }
    }
}


int main()
{
    int iterations[SIZE] = {2, 4, 5, 6, 11, 12, 13, 16, 21, 22, 23, 24, 28, 29, 31, 33, 35, 36, 37, 38};
    double f(double x)
    {
        return x+1-3*math.sin(x);
    }

    double a = 1.126414
    double b = 3.241574
    int n = 38;
    double tol = 4.18126e-09
    bis(f, a, b, n, SIZE, iterations);

}
