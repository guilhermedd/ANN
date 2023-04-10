#include <stdio.h>
#include <math.h>
#define SIZE 3

void newton(double (*f)(double),double (*df)(double), double x0, int n, int p[])
{
    int iteracao = 1;
    int i2 = 0;
    for(int i = 0; i < n; i++)
    {
        double dfx0 = df(x0);
        if(dfx0 == 0)
        {
            break;
        }
        double xi = x0 - f(x0)/dfx0;
        if(iteracao == p[i2])
        {
            printf("%.16f,\n", i+1, xi);
            i2++;
        }
        iteracao++;
        x0 = xi;
    }
}

    double f(double x)
    {
        return -2651000 + 1270776 * exp(x) + (209614/x) * (exp(x) - 1);
    }

    double df(double x)
    {
        return 1270776 * exp(x) + 209614 * (exp(x) * x - exp(x) + 1)/(x*x) ;
    }
int main()
{
    int iterations[SIZE] = {1,3,5};
    double x0 = 1.76;
    int n = 12;
    newton(f, df, x0, n, iterations);
}