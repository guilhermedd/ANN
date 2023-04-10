/* Na mão









x_1(100) = 1.2950000002058526 | x_2(100) = 1.9762677527290293 | x_3(100) = 2.3292345498506046

*/

#include <stdio.h>
#include <math.h>
#define L 3
#define C 3

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            chute[i]=bi;
        }
        printf("\n");
    }
}



// INSERIR O TAMANHO DA MATRIZ EM DEFINE
//***************************************************************************
int main() {
    double m1 = 2.35,
            m2 = 3.24,
            m3 = 4.8,
            k1 = 60.64,
            k2 = 51.7,
            k3 = 52.87,
            g = 9.81;

    // Seidel input
    double a[L][C] = {{k1+k2, -k2, 0},
                            {-k2, k2+k3, -k3},
                            {0, -k3, k3}
    };

    double b[L] = {m1*g, m2*g, m3*g};

    double chute[C] = {8, 10, 10};

    int n = 100; //deu certo na interação 100, não sei o porquê

    jacobi(a,b,chute,n);

    return 0;
}