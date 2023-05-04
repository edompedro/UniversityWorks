#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main()
{

    pid_t newPid, me, parent, x;
    int status, size_vec,flag1 ,flag2 ;

    newPid = fork();    //cria um processo filho
    me = getpid();      //retorna o id do processo q fez a requisição
    parent = getppid(); //retorna o id do processo que é pai daquele q fez a requisição

    printf("%d, %d, %d\n", me, parent, newPid);

    if (newPid != 0){   //newPid != 0 significa que ele possui algum filho
        
        if((newPid % 2) == 0){ 

            printf("Esperando filho pid %d\n", newPid); 
            x = waitpid(newPid, &status, 0); 
            printf("Filho %d terminou\n", x);

        }else{
            printf("não to esperando filho pid %d\n", newPid);
        }

    }else{  //newPid == 0 significa que é filho

        if((parent % 2) == 0){flag2 = 1;}else{flag2 = 0;}
        if((me % 2) == 0){flag1 = 1;}else{flag1 = 0;}

        printf("pai: %d\n filho: %d\n", parent, me);
        printf("Sou o filho\n informe o tamanho do vetor: \n");
        scanf("%d", &size_vec);

        int vector1[size_vec], vector2[size_vec], vectorResult[size_vec], vectorResult2[size_vec], vectorResult3[size_vec];
        
        for (int i = 0; i < size_vec; i++){
            
            vector1[i] == rand();
            vector2[i] == rand();
            
            if((flag1 == 1) && (flag2 == 1)){
                // printf("ambos par\n");
                vectorResult[i] = vector1[i] * vector2[i];
            }
            else if((flag1 == 1) && (flag2 == 0)){
                // printf("filho par e pai impar\n");
                vectorResult[i] = vector1[i] + vector2[i];
            }
            else if((flag1 == 0) && (flag2 == 0)){
                // printf("ambos imparz\n");
                vectorResult[i] = vector1[i] - vector2[i];
            }
            else if((flag1 == 0) && (flag2 == 1)){
                // printf("filho impar e pai par\n");
                vectorResult[i] = vector1[i] * vector2[i];
                vectorResult2[i] = vector1[i] + vector2[i];
                vectorResult3[i] = vector1[i] - vector2[i];
            }

        }        
        sleep(2);
        for (int c = 0; c < size_vec; c++){
            printf("vector1[%d] = %d\n", c, vector1[c]);
            printf("vector2[%d] = %d\n", c, vector2[c]);
            printf("vectorResult[%d] = %d\n\n", c, vectorResult[c]);
        }
    }
    return 0;
}