#include <stdio.h>
#include <math.h>
void bis(double(*f)(double), double a, double b, int n)
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
        for(int i = 0; i < n; i++)
        {
            double m = 0.5 * (a + b);
            double fm = f(m);
            if(fm == 0)
            {
                printf("Voce encoutrou uma raiz r=%.16f\n", m);
                return;
            }
            printf("Iteracao: %d, resultado: %.16f\n", iteracao, m);
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


int main()
{
    double f(double x)
    {
        return x+1-3*math.sin(x);
    }

    double a = 0.083;
    double b = 1.13687;
    int n = 18;
    bis(f, a, b, n);

}
