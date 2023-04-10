#include <stdio.h>
#include <math.h>

#define SIZE 3
#define PI 3.14159265359

void secant(double (*f)(double), double x0, double x1, int n, int p[])
{
    int iteracoes = 1;
    int i2 = 0;
    for(int i = 0; i < n; i++)
    {
        double fx0 = f(x0);
        double fx1 = f(x1);
        if(fx0 == fx1)
        {
            break;
        }
        double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
        if(iteracoes == p[i2])
        {
            printf("%.16f,\n", x2);
            i2++;
        }
        iteracoes++;
        x0 = x1;
        x1 = x2;
    }
}

double f(double x)
{
    return 2*(x+1)*(x-0.5)*(x-1);
}

int main()
{
    int iterations[SIZE] = {1,3,5};
    double x0 = -0.15621;
    double x1 = 0.8037;
    int n = 5;

    secant(f, x0, x1, n, iterations);
}