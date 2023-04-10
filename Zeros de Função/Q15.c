#include <stdio.h>
#include <math.h>
#define SIZE 39
#define PI 3.14159265359

//Atualmente n funciona *************************

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
    int iterations[SIZE] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195};

    double f(double x)
    {
        return x*(x-1)*(x-2)+0.42;
    }

    double df(double x)
    {
        return 3*x*x -6*x + 2;
    }

    double x0 = 3.10731694;
    int n = 195;
    newton(f, df, x0, n, iterations);
}