import logging
from random import randint
import threading
import time

def thread_function(acount, operationValue, operationType):
    
    # # # # # # # # # VERIFICA QUAL O TIPO DE OPREÇÃO # # # # # # # # #
    if(operationType == "credit") or (operationType == "debit"):
        acount[1][1].acquire()                                                                                          # trava o lock
        logging.info("conta %d entrou na operação de %s com saldo = $%d", acount[0][0], operationType, acount[0][1])
        
        if(acount[1][0]._value == 5 and operationType == "debit"):                                                      # verifica se o semaforo ta vazio
            
            if acount[0][1] < operationValue:                                                                           # verifica se tem saldo na conta
                logging.info("conta %d não tem saldo suficinte. Saldo = $%d", acount[0][0], acount[0][1] )
            else:
                acount[0][1] -= operationValue                                                                          # realiza o débito
                logging.info("conta %d realizou a operação. Saldo = $%d", acount[0][0], acount[0][1] )
            acount[1][1].release()                                                                                      # libera o lock
            
        elif(acount[1][0]._value == 5 and operationType == "credit"):                                                   # verifca se o semaforo ta vazio
            acount[0][1] += operationValue                                                                              # realiza ocrédito
            logging.info("conta %d realizou a operação. Saldo = $%d", acount[0][0], acount[0][1] )
            acount[1][1].release()                                                                                      # libera o lock

        else:                                                                                                           # se o semaforo ta cheio ñ faz nada
            logging.info("conta %d não pode realizar a operação. Saldo = $%d", acount[0][0], acount[0][1])
            acount[1][1].release()                                                                                      # libera o lock sem fazer operacao
    
    else:                                                                                                               # entre na operacao de consulta
        acount[1][0].acquire()                                                                                          # add +1 ao semaforo
        logging.info("conta %d operação de %s", acount[0][0], operationType)
        # time.sleep(1)                                                                                                 # sleep para observar melhor a atuacao do semaforo
        logging.info("conta %d realizou a consulta", acount[0][0])
        acount[1][0].release()                                                                                          # libera -1 ao semaforo

if __name__ == "__main__":

    # # LISTAS AUXILIARES # #
    acountList = []
    threads = [] 

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # # # # # # # #    CRIA N CONTAS PARA SEREM MANIPULADAS    # # # # # # # # # #
    for i in range(5):
        cash = 0
        acount = [i, cash]
        acountList.append([acount,[threading.Semaphore(5), threading.Lock()]])
    
    
    # # # # # # # #   CRIA N OPERAÇÕES À SEREM REALIZADAS    # # # # # # # # # # # 
    for i in range(10):
        operacao = randint(0,4)        
        if operacao == 1: operationType = "consulta"        # DEFINE
        elif operacao == 2: operationType = "credit"        # AS
        elif operacao == 3: operationType = "debit"         # OPERAÇÕES
        else: operationType = "consulta"
        
        conta = randint(0,4)                                # SELECIONA A CONTA
        operationValue = randint(0,20000)                   # DEFINE O VALOR DA OPERAÇÃO
        
        t = threading.Thread(target=thread_function, args=(acountList[conta], operationValue, operationType))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    logging.info("Main    : all done")