#include <stdio.h>
#include <math.h>
void bis(double(*f)(double), double a, double b, int n)
{
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
            printf("Iteracao: %d, resultado: %.16f\n", n, m);
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
    double f(double x) {
        return x*x - 3
    }

    double j = 1.67292;
    double b = 2.76364;
    int n = 7;
    bis(f, j, b, n);

}
