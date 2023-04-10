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
                    printf("%.7f,\n",p[i2], m);
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
    int iterations[SIZE] = {2, 3, 6, 7, 8, 9, 10, 15, 16, 19, 22, 23, 27, 28, 29, 30, 32, 36, 38, 39};
    double f(double x)
    {
        return x*x -3.364 * x + 1.3026 ;
    }

    double a = 1.2878;
    double b = 5.76;
    int n = 51;
    bis(f, a, b, n, SIZE, iterations);

}