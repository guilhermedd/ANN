#include <stdio.h>
#include <math.h>
#define SIZE 3
#define PI 3.14159265359

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
        if(p[i2] == iteracao)
        {
            printf("%.16f,\n", xi);
            i2++;
        }
        iteracao++;
        x0 = xi;
    }
}

int main()
{
    int iterations[SIZE] = {1, 3, 5};

    double f(double x)
    {
        return PI*x-exp(x);
    }

    double df(double x)
    {
        return PI - exp(x);
    }

    double x0 = 0.93248;
    int n = 5;
    newton(f, df, x0, n, iterations);
}