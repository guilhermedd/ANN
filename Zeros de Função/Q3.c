#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define SIZE 10

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
                    printf("Iteracao: %d, resultado: %.7f,\n", iteracao, m);
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
    int iterations[SIZE] = {4, 11, 17, 22, 27, 29, 32, 36, 37, 39};
    double f(double x)
    {
        return pow(x,4)-2*pow(x,3)-3*pow(x,2)+3*x+2;
    }

    double a = -1.68212;
    double b = 1.91823;
    int n = 39;
    bis(f, a, b, n, SIZE, iterations);

}