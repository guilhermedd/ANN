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


int main()
{
    int iterations[SIZE] = {1,3,5};
    double f(double x)
    {
        return PI * x - exp(x);
; 
    }

    double x0 = 1.28478;
    double x1 = 1.95604;
    int n = 5;

    secant(f, x0, x1, n, iterations);
}