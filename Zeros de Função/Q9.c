#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define SIZE 20

void bis(double(*f)(double), double a, double b, int n, int s, int p[])
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
                if(fm == 0)
                {
                    printf("Voce encoutrou uma raiz r=%.16f\n", m);
                    return;
                }
                if(p[i2] == iteracao)
                {
                    printf("Numero: %d = %.7f,\n",p[i2], m);
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
    int iterations[SIZE] = {1, 3, 5};
    double f(double x)
    {
        return log(x*x)-0.7;
    }

    double a = 0.8045;
    double b = 2.3791;
    int n = 39;
    bis(f, a, b, n, SIZE, iterations);

}
