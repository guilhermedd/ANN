#include <stdio.h>

#define L 4
#define C 4
#define SIZE 12


//so funciona para sistemas nxn
void jacobi(double A[L][C], double B[L], double chute[L], int n, int p[]){
    double next[L];
    int iteracao = 1;
    int i2 = 0;
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            if(iteracao == p[i2])
            {
                printf("%.16f,\n", bi);
            }
            next[i]=bi;
        }
        if(iteracao == p[i2])
        {
            i2++;
        }
        iteracao++;
        //atualizar o chute
        for(int i=0;i<L;i++) chute[i]=next[i];
    }
}

int main(){
    double A[L][C]={{9.75, -3.86, 3.68, 0.28}, {-3.29, 7.95, -0.87, 1.87}, {0.71, -3.71, -10.98, -4.63}, {1.8, 2.49, -1.45, 7.65}};
    double B[L]={-0.66, 1.06, -0.46, 2.56}; // result

    int iterations[SIZE] = {3, 6, 8, 10, 11, 15, 16, 19, 23, 24, 26, 29};

    double chute[L]={2.45, 1.97, 2.28, 1.4}; // x0
    int n=29;

    jacobi(A, B, chute, n, iterations);

    return 0;
}