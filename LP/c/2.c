#include <stdio.h>

int main(){

    int num;
    printf("informe um numero: ");
    scanf("%d", &num);

    for (int i = 2; i <= num; i++){

        if((num % i) == 0 && i < num){
            printf("não é primo");
            break;
        }else{printf("é primo"); break;}
    }
    
    return 0;
}
