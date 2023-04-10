#include <stdio.h>
#include <math.h>

#define ROW 3
#define COL 3

void imprimeMatriz(double matriz[ROW][COL]){
    for(int row = 0; row < ROW; row++){
        for(int col = 0; col < COL; col++){
            printf("%.16f, ", matriz[row][col]);
        }
        printf("\n");
    }
}

void trocaLinha(double matriz[ROW][COL], int r1, int r2){
        for(int k=0;k<COL;k++){
        double temp = matriz[r1][k];
        matriz[r1][k] = matriz[r2][k];
        matriz[r2][k] = temp;
    }
}

void operacaoEmLinha(double matriz[ROW][COL], int row, double num){
    for(int i = 0; i < COL; i++){
        matriz[row][i] *= num; 
    }
}

void opercaoEmDuasLinhas(double matriz[ROW][COL], int target, int r2, double num){
    for(int i = 0; i < COL; i++){
        matriz[target][i] = (num*matriz[r2][i]) + matriz[target][i];
    }
}

/* Esplicação de como usar o codigo do mauricio :)
  /*
	L1 0
    L2 1
    L3 2
	L4 3
	-3/2.L4 → L4
	operacaoEmLinha(matriz, 3, (-3.0/2.0));
	7/9.L3 → L3
	operacaoEmLinha(matriz, 2, (7.0/9.0));
    −4/7⋅L4+L2→L2
    opercaoEmDuasLinhas(matriz, 1, 3, (-4.0/7.0));
	-3/7.L1 + L4 → L4
	opercaoEmDuasLinhas(matriz, 3, 0, (-3.0/7.0));
	***quem soma vem primeiro
	
	//1/6⋅L3+L4→L4
	opercaoEmDuasLinhas(matriz, 3, 2, (1.0/6.0) );
	//L1↔L2
	trocaLinha(matriz, 0, 1);
	//8/3⋅L2→L2
	operacaoEmLinha(matriz, 1, (8.0/3.0));
	//L1↔L4
	trocaLinha(matriz, 0, 3);
	//−3/4⋅L1→L1
	operacaoEmLinha(matriz, 0, (-3.0/4.0));
	//4/5⋅L2+L1→L1
	opercaoEmDuasLinhas(matriz, 0, 1, (4.0/5.0));
*/
void operacoes(double matriz[ROW][COL]){
    opercaoEmDuasLinhas(matriz, 1, 0, 8.0);
    opercaoEmDuasLinhas(matriz, 2, 0, -1.0);
    opercaoEmDuasLinhas(matriz, 2, 1, (1.0/12.0));
    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
		{1, -4, 3}, {-8, -4, -7}, {1, -1, -7}
    };

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}