#include <stdio.h>
#include <math.h>
#define SIZE 4

void bis(double(*f)(double), double a, double b, int n, int p[])
{
    int iteracao = 1;
    int i2 = 0;
    double fa = f(a);
    double fb = f(b);
    if(fa * fb >= 0)
    {
        printf("Voce nao pode usar esse intervalo\n");
        return;
    }
    else
    {
        for(int i = 0; i < n; i++)
        {
            double m = 0.5 * (a + b);
            double fm = f(m);
            if(fm == 0)
            {
                printf("Voce encoutrou uma raiz r=%.16f\n", m);
                return;
            }
            if(iteracao == p[i2])
            {
                printf("%.16f,\n", n, m);
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

    double f(double x)
    {
        return -2651000 + 1270776 * exp(x) + (209614/x) * (exp(x) - 1);
    }
int main()
{
    int iterations[SIZE] = {2, 4, 8, 12};
    double a = 0.1;
    double b = 1.51;
    int n = 12;
    bis(f, a, b, n, iterations);

}