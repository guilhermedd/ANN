#include <stdio.h>
#include <math.h>
#define SIZE 8
#define PI 3.14159265359

double f(double x)
{
    return x/2.0 + 1.0/x;
}

void fixed_point(double (*f)(double), double x0, int n, int p[])
{
    int iteracao = 1;
    int i2 = 0;
    for(int i = 0; i < n; i++)
    {
        double x1 = f(x0);
        if(iteracao == p[i2])
        {
            printf("%.16f,\n", x1);
            i2++;
        }
        iteracao++;
        x0 = x1;
    }
}

int main()
{
    int iterations[SIZE] = {1, 2, 3, 4, 5, 6, 7, 8};
    int n = 100;
    double x0 = 1.82514;

    fixed_point(f, x0, n, iterations);
}