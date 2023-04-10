#include <stdio.h>

#define L 3
#define C 3
#define SIZE 8


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
    double A[L][C]={{-6.31, 3.73, -1.05}, {-0.83, -4.48, 2.12}, {-3.97, -4.13, 9.62}};
    double B[L]={-1.27, 1.88, -0.23}; // result

    int iterations[SIZE] = {1, 5, 6, 7, 10, 12, 17, 19};

    double chute[L]={-1.06, 2.11, 0.46}; // x0
    int n=19;

    jacobi(A, B, chute, n, iterations);

    return 0;
}