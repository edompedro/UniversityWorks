#include <stdio.h>
#include <math.h>

int main(){

    double n,x;
    printf("informe um inteiro: "); scanf("%lf", &x);
    printf("informe um inteiro não-negativo: "); scanf("%lf", &n);
    printf("resultado = %lf", pow(x, n));

    return 0;
}
