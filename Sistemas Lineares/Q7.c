#include <stdio.h>
#include <math.h>
#define L 4
#define C 4
#define SIZE 12

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
    double A[L][C]={{7.47, -0.93, -0.69, 4.24}, {2.64, 7.93, -3.15, -0.55}, {2.69, 3.93, -13.03, -4.81}, {4.66, -2.82, -2.06, 11.14}};
    double B[L]={4.28, -2.19, 4.48, 4.2}; // result

    double chute[L]= {0.41, 4.14, -1.54, 1.6}; //x0
    int n=25;

    int iterations[SIZE] = {1, 3, 4, 5, 6, 7, 11, 12, 16, 17, 23, 25};

    jacobi(A, B, chute, n, iterations);

    return 0;
}