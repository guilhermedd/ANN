#include <stdio.h>
#include <math.h>
#define SIZE 4
#define PI 3.14159265359

//incompleto

void secant (double (*f)(double), double a, double b, int n, int p[])
{
    int iteracao = 1;
    int i2 = 0;
    for(int i = 0; i < n; i++)
    {
        double fa = f(a);
        double fb = f(b);
        if(fa*fb >= 0)
        {
            printf("O teorema de Bolzano nao sabe dizer se existe\n");
            break;
        }
        double x1 = (a * fb - b * fa) / (fb - fa);
        if(iteracao == p[i2])
        {
            printf("%.16f,\n", x1);
            i2++;
        }
        iteracao++;
        double fx1 = f(x1);
        if(fa * fx1 < 0)
        {
            b = x1;
            fb = fx1;
        }
        else
        {
            a = x1;
            fa = fx1;
        }
    }
}

double f(double x)
{
    return  -2651000 + 1270776 * exp(x) + (209614/x) * (exp(x) - 1);
}

int main()
{
    int iterations[SIZE] = {2, 4, 7, 11};
    double a = 0.1;
    double b = 1.49;
    int n = 18;
    secant(f, a, b, n, iterations);
}