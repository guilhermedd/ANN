#include <stdio.h>
#include <math.h>
#define SIZE 3

void secant(double (*f)(double), double x0, double x1, int n, int p[])
{
    int iteracao = 1;
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
        if(iteracao == p[i2])
        {
            printf("%.16f,\n", x2);
            i2++;
        }
        iteracao++;
        x0 = x1;
        x1 = x2;
    }
}

double f(double x)
{
    return -2651000 + 1270776 * exp(x) + (209614/x) * (exp(x) - 1);
}

int main()
{
    int iterations[SIZE] = {1,2,5};
    double x0 = 0.1;
    double x1 = 1.6;
    int n = 5;

    secant(f, x0, x1, n, iterations);
}