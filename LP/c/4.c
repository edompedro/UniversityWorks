#include <stdio.h>

int main()
{
    double f, c;
    printf("informe uma temperatura em Fahrenheit: ");
    scanf("%lf", &f);

    printf("A conversão de Fahrenheit para Celsus é: %lf", (((f-32)*5)/9));
    return 0;
}
