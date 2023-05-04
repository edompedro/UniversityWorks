#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void collatz(int n) {   //cria a conjectura
    // printf("processo numero: %d", getpid());
    printf("Collatz para %d: ",n);
    while (n != 1) {
        printf("%d ",n);
        if(n%2 == 0){n /= 2;} else{n = 3 * n + 1;}
    }
    printf("1\n");
    // sleep(2);
}

int main() {
    
    int numproc;
    printf("informe o numero de processos: \n");
    scanf("%d", &numproc);

    for(int i = 1; i <= numproc; i++){
        pid_t pid = fork();
        
        if(pid == -1) {
            exit(EXIT_FAILURE);
        }else if(pid == 0){
            printf("processo numero: %d\n", getpid());
            char numero = ((getpid()/100)%10 * 100 + (getpid()%100)/10 *10) /10;    //calcula dezena e centena do processo
            collatz(numero);
            exit(EXIT_SUCCESS);
        }
    }

    for(int i = 1; i <= numproc; i++){
        wait(NULL);
    }
    return 0;
}
