import logging
from random import randint
from struct import Struct
import threading
import time

def thread_function(acount, operationValue):

    if(acount[2] == "credit") or (acount[2] == "debit"):
        
        # diferenciar as operações de credit e debit para somar ou subtrair o valor
        
        lock.acquire()
        logging.info("Thread %d entrou na operação de %s com saldo = $%d", acount[0], acount[2], acount[1])
        if(S._value == 5):
            acount[1] += operationValue
            # time.sleep(5)
            logging.info("Thread realizou a operação. Saldo = %d", acount[1] )
            lock.release()
        else:
            logging.info("Thread %d não pode realizar a operação. Saldo = %d", acount[0], acount[1])
            lock.release()
    
    else:  
        
        # ajustar para só permitir 5 consultas ao mesmo tempo
        
        S.acquire()
        logging.info("Thread %d operação de %s", acount[0], acount[2])
        time.sleep(3)
        logging.info("Thread %s realizou a consulta", acount[0])
        # logging.info("thread saiu do semaforo, vagas disponiveis :::   %d", S._value+1)
        S.release()


lock = threading.Lock()
S = threading.Semaphore(5)

if __name__ == "__main__":

    
    threads = [] #armazena os descritores das threads

    # numOfThread = randint(0,4)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    for i in range(10):
        operacao = randint(0,4)
        operationValue = randint(0,20000)
        operationType = None
        cash = 0
        
        if operacao == 1: operationType = "consulta"
        elif operacao == 2: operationType = "credit"
        elif operacao == 3: operationType = "debit"
        else: operationType = "consulta"
        
        acount = [i, cash, operationType]
        t = threading.Thread(target=thread_function, args=(acount, operationValue))
        
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    logging.info("Main    : all done")