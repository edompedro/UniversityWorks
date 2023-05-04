import logging
import random
import threading
import time

def thread_function(vec1, vec2,start,end):
    global result
    soma = []
    for i in range(start,end):
        for c in range(len(vec1[i])):
            soma.append(vec1[i][c] + vec2[i][c])
        result.append(soma)

    time.sleep(2)
    # logging.info("\nThread %s: finishing", id)
    
size_vec = int(input("informe o tamanho dos vetores\n"))
size_threads = int(input("informe a quantidade de threads\n"))
vec1 = []
vec2 = []
matriz1 = []
matriz2 = []
for i in range(size_vec):
    for i in range(size_vec):
        vec1.append(random.randint(0,10))
        vec2.append(random.randint(0,10))
    matriz2.append(vec2)
    matriz1.append(vec1)
    vec1 = []
    vec2 = []
#o programa distribui as somas que sobram entre as threads, dessa forma nenhuma fica sobrecarregada
#exemplo: se temos um vetor de 19 tamanho e a ultima recebe todos os restos, a ultima thread vai ficar com
#9 somas enquanto as outras vão ficar com 1. Do jeito que fiz no programa se sobram 9 somas ele distribui
#uma a mais para cada e assim balanceia o numero de tarefas.
 
if(size_threads >= size_vec):
    gap = 1
    resto = 0
else:
    gap = int(size_vec/size_threads)
    resto = (size_vec%size_threads)
start = 0
end = 0

if __name__ == "__main__":
    threads = [] #armazena os descritores das threads
    result = []

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


    for id in range(size_threads):
        start = end
        if(resto > 0 and id < resto):
            end += gap+1 
        else:
            end += gap

        t = threading.Thread(target=thread_function, args=(matriz1,matriz2, start, end)) #inicializa a thread, informa o nome da função e os parâmetros
        # logging.info("Main    : before running thread %d", id)
        t.start()
        threads.append(t)
        # logging.info("Main    : wait for the thread to finish")

    for t in threads:
        t.join()

    print("m1 =", matriz1)
    print("m2", matriz2)
    print("result = ", result)

    logging.info("Main    : all done")