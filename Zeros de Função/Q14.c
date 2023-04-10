#include <stdio.h>
#include <math.h>
#define SIZE 16
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
    int iterations[SIZE] = {1, 25, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700};

    double f(double x)
    {
        return exp(5*x) - 2;
    }

    double df(double x)
    {
        return 5*exp(5*x);
    }

    double x0 = -1.16460629;
    int n = 700;
    newton(f, df, x0, n, iterations);
}