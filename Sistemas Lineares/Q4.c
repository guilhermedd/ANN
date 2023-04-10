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
    double A[L][C]={{10.29, -4.45, 4.35}, {-3.24, 5.22, -0.49}, {0.06, -4.06, 5.61}};
    double B[L]={-3.16, 0.15, -0.31}; // result

    int iterations[SIZE] = {1, 5, 7, 10, 12, 15, 17, 18};

    double chute[L]={1.23, 0.22, 2.55}; // x0
    int n=60;

    jacobi(A, B, chute, n, iterations);

    return 0;
}