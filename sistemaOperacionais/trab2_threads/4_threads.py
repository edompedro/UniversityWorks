import logging
import random
import threading
import time

def thread_function(m1, m2,row_start,row_end):
    global result
    soma = 0
    new_row = []
    for i in range(row_start, row_end):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                soma += m1[i][k] * m2[k][j]
            new_row.append(soma)
            soma = 0
        result.append(new_row)
        new_row = []
        
    
    time.sleep(2)
    # logging.info("\nThread %s: finishing", id)
    

#criando as matrizes
size_m1 = int(input("informe o tamanho da 1 matriz\n"))
size_m2 = int(input("informe o tamanho da 2 matriz\n"))
size_threads = int(input("informe a quantidade de threads\n"))
m1 = []
m2 = []
matriz1 = []
matriz2 = []

for i in range(size_m1):
    for i in range(size_m1):
        m1.append(random.randint(0,10))
    matriz1.append(m1)
    m1 = []
for i in range(size_m2):
    for i in range(size_m2):
        m2.append(random.randint(0,10))
    matriz2.append(m2)
    m2 = []
    
#o programa distribui as somas que sobram entre as threads, dessa forma nenhuma fica sobrecarregada
#exemplo: se temos um vetor de 19 tamanho e a ultima recebe todos os restos, a ultima thread vai ficar com
#9 somas enquanto as outras vão ficar com 1. Do jeito que fiz no programa se sobram 9 somas ele distribui
#uma a mais para cada e assim balanceia o numero de tarefas.
 
 
#difisão de tarefas da thread
if(size_m1 > size_m2):
    size = size_m1
else: 
    size = size_m2
if(size_threads >= size):
    gap = 1
    resto = 0
else:
    gap = int(size/size_threads)
    resto = (size%size_threads)
    
row_start = 0
row_end = 0

#main
if __name__ == "__main__":
    threads = [] #armazena os descritores das threads
    result = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


    for id in range(size_threads):
        
        row_start = row_end
        if(resto > 0 and id < resto):
            row_end += gap+1 
        else:
            row_end += gap

        t = threading.Thread(target=thread_function, args=(matriz1,matriz2, row_start, row_end)) #inicializa a thread, informa o nome da função e os parâmetros
        t.start()
        threads.append(t)

    #sincroniza as threads
    for t in threads:
        t.join()

    #printa os resultados
    print("m1 =", matriz1)
    print("m2", matriz2)
    print("result = ", result)

    logging.info("Main    : all done")