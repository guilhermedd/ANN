#include <stdio.h>
#include <math.h>
#define SIZE1 4
#define SIZE2 3
#define SIZE3 3
#define SIZE4 4
#define PI 3.14159265359

void bis(double(*f)(double), double a, double b, int n, int p[])
{
    int iteracao = 1;
    int i2 = 0;
    double fa = f(a);
    double fb = f(b);
    if(fa * fb >= 0)
    {
        printf("Voce nao pode usar esse intervalo\n");
        return;
    }
    else
    {
        for(int i = 0; i < n; i++)
        {
            double m = 0.5 * (a + b);
            double fm = f(m);
            if(fm == 0)
            {
                printf("Voce encoutrou uma raiz r=%.16f\n", m);
                return;
            }
            if(iteracao == p[i2])
            {
                printf("%.16f,\n", m);
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
            printf("%.16f,\n", xi);
            i2++;
        }
        iteracao++;
        x0 = xi;
    }
}

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

void false_position (double (*f)(double), double a, double b, int n, int p[])
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
    return -31.86 + ((9.81 * x)/22.13) * (1 - exp(-1*(22.13/x) * 8.31));
}

double df(double x)
{
    return (981*(1-exp(-1839003/(10000*x))))/2213-(815211*exp(-1839003/(10000*x)))/(10000*x);
}

int main()
{
    int n = 12;
    double aB = 26.78;
    double bB = 193.22;
    double x0N = 29.87;
    double x0S = 26.53;
    double x1S = 35.45;
    double aPf = 36.5;
    double bPf = 186.78;

    int iterations_bissection[SIZE1] = {2,4,8,12};
    int iterations_newton[SIZE2] = {1,3,5};
    int iterations_secant[SIZE3] = {1,2,5};
    int iterations_falseposition[SIZE4] = {2,4,7,11};

    bis(f, aB, bB, n, iterations_bissection);
    newton(f, df, x0N, n, iterations_newton);
    secant(f, x0S, x1S, n, iterations_secant);
    false_position(f, aPf, bPf, n, iterations_falseposition);
}