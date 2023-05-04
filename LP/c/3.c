#include <stdio.h>

int main(){
    
    int num;
    printf("informe um numero natural: ");
    scanf("%d", &num);

    if((num % 2)==0){
        num--;
        for (int i = num; i > 0 ; i--){
            i--;
            printf("%d\n", num);
            num = num -2;
        }  
    }else{         
        for (int i = num; i > 0 ; i--){
            printf("%d\n", num);
            i--; num = num-2;
        }  
    }
    return 0;
}
