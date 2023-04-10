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

void false_position(double (*f)(double),double a,double b,int n, int p[]){
    double fa = f(a);
    double fb = f(b);
    int iteracao = 1;
    int i2 = 0;
    if(fa * fb >= 0){
        printf("O Teorema de Bolzano não sabe dizer se existe raiz para f no intervalo [%.16f, %.16f]",a,b);
        return;
    }else {
        double x;
        for(int i =0;i<n;i++){
            x = (a *fb - b * fa) / (fb - fa);
            if(iteracao == p[i2])
            {
                printf("%.16lf,\n",x);
                i2++;
            }
            iteracao++;
            double fx = f(x);
            if(fx == 0){
                printf("Encontramos uma raiz para f, ela é x = %.16lf",x);
                return;
            }
            if(fa * fx < 0){
                b = x;
                fb = fx;
            }else{
                a = x;
                fa = fx;
            }
        }
    }
}

double f(double x)
{
    return -36.04 + ((9.81 * x)/20.73) * (1 - exp(-1*(20.73/x) * 9.38));
}

double df(double x)
{
    return 0.47322 * (-exp(-1*(194.4474/x)) -1 * (194.4474 * exp(-1 * 194.4474/x)/x) + 1);
}

int main()
{
    int n = 12;
    double aB = 35.45;
    double bB = 184.26;
    double x0N = 28.06;
    double x0S = 25.7;
    double x1S = 39.5;
    double aPf = 30.05;
    double bPf = 201.22;

    int iterations_bissection[SIZE1] = {2,4,8,12};
    int iterations_newton[SIZE2] = {1,3,5};
    int iterations_secant[SIZE3] = {1,2,5};
    int iterations_falseposition[SIZE4] = {2,4,7,11};

    bis(f, aB, bB, n, iterations_bissection);
    newton(f, df, x0N, n, iterations_newton);
    secant(f, x0S, x1S, n, iterations_secant);
    false_position(f, aPf, bPf, n, iterations_falseposition);
}