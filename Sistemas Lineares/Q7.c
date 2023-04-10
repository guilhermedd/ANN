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
    double A[L][C]={{8.81, -2.35, 4.87}, {-0.58, 5.02, -2.86}, {2.72, 0.49, 4.8}};
    double B[L]={-2.79, -3.61, -4.05}; // result

    double chute[L]= {-1.97, 0.42, -2.53}; //x0
    int n=25;

    int iterations[SIZE] = {1, 5, 7, 10, 12, 15, 17, 18};

    jacobi(A, B, chute, n, iterations);

    return 0;
}