//Tem que fazer na mão
/*

    -cx.v + R + mx.g = mx.a

    Paraquedista 1:

    -11.96*7.95 + 84.58*9.81 - T = 84.58*a
    -84.58*a - T = -734,6478000000001

    Paraquedista 2:

    -16.05*7.95 - R + 71.14*9.81 + T = 71.14*a
    -R - 71.14*a + T = -570,2859000000001

    Paraquedista 3:

    -20.95*7.95 + R + 59.62*9.81 = 59.62*a
    R - 59.62*a = -418,3197

    R - 59.62*a + 0T= -418,3197
    -R - 71.14*a + T = -570,2859000000001
    0R -84.58*a - T = -734,6478000000001


*/
#include <stdio.h>

int main()
{
    double x1 = 3164850877500002981.0/53835000000000000.0;
    double x2 = 8616267000000001.0/1076700000000000.0;
    double x3 = 6223142340000002309.0/107670000000000000.0;
    printf("%.16f,\n", x1);
    printf("%.16f,\n", x2);
    printf("%.16f,\n", x3);
}