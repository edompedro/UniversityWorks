#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FRASE 100

int main(){

    char frase[MAX_FRASE],compare[MAX_FRASE], *words, *palavras[MAX_FRASE];
    int flag = 0,counter = 0;

    printf("insira uma frase: \n");
    fgets(frase, MAX_FRASE, stdin);
    printf("insira uma palavra: \n");
    fgets(compare, MAX_FRASE, stdin);

    words = strtok(frase, " ");

    for(int i = 0; words != NULL; i++) { 
        palavras[i] = words;

        for(int c = 0; c < strlen(palavras[i]); c++){

            for(int t = 0; t < strlen(compare); t++){

                if(palavras[i][c+t] == compare[t]){
                    flag++;

                    if(flag == strlen(compare)-1){
                        counter++;
                        flag = 0;
                    } 

                }else{flag = 0;}
            }
        }
        words = strtok(NULL, " ");
    }
    printf("Existem %d ocorrencias da palavra na frase.\n", counter);
    return 0;
}
