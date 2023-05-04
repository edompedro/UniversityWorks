#include<stdio.h>
#include<pthread.h>		//gcc exemplo.1 - lpthread
#define N 20

//Deve ser declarado como ponteiro para função
void *hello(void *i){

	long id;

	id = (long)i;

	printf("Olá, sou a thread %ld\n", id);		//escalonador q decide a ordem q as threads vão ser executadas 
												//logo não vai estar em ordem esses prints.

	pthread_exit(NULL);

}


int main(){

	pthread_t threads[N]; //handlers das threads
	long i;

	for(i=0;i<N;i++){
		//(handler, atributos, função a ser executada, parâmetro da função)
		printf("Criando thread %ld\n", i);
		pthread_create(&threads[i],NULL,&hello,(void *)i);
	}

	//Deve ser chamada para sincronizar as threads no final
	for(i=0;i<N;i++){
		pthread_join(&threads[i],NULL);
	}

}
