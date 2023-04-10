#include <stdio.h>
#include <math.h>
#define L 3
#define C 3
#define SIZE 8

void jacobi(double A[L][C], double B[L], double chute[L], int n, int p[]){
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
            chute[i]=bi;
        }
        if(iteracao == p[i2])
        {
            i2++;
        }
        iteracao++;
    }
}


// INSERIR O TAMANHO DA MATRIZ EM DEFINE
//***************************************************************************

int main(){
    double A[L][C]={{-5.31, -1.44, -2.79}, {0.56, 6.27, -4.63}, {1.41, -2.41, 4.9}};
    double B[L]={2.15, 2.47, -3.32}; // result

    double chute[L]= {0.5, -3.7, -2.99}; //x0
    int n=19;

    int iterations[SIZE] = { 7, 8, 11, 12, 15, 17, 18, 19};

    jacobi(A, B, chute, n, iterations);

    return 0;
}