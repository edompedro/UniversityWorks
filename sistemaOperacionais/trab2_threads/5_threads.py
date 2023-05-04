from collections import Counter
import os
import threading

direct = input("informe o diretorio para a leitura dos arquivos: \n")
arquivos = os.listdir(direct)

def vogalConso(document):
    with open("test/"+arquivo, "r", encoding="utf-8") as document:
        
        delet = []
        vogais, consoantes = 0, 0
        texto = document.read()
        words = Counter(texto).most_common()

        for i in range(len(words)):
            if('a' in words[i][0]):
                vogais += words[i][1]
            elif('e' in words[i][0]):
                vogais += words[i][1]
            elif('i' in words[i][0]):
                vogais += words[i][1]
            elif('o' in words[i][0]):
                vogais += words[i][1]
            elif('u' in words[i][0]):
                vogais += words[i][1]
            elif('\n'  in words[i][0]):
                delet.append(i)
            elif(' ' in words[i][0]):
                delet.append(i)
            else:
                consoantes += words[i][1]
                
        for c in range(len(delet)):
            del words[delet[c]]  
                    
        print("\nnumero de vogais = ", vogais)
        print("numero de consoantes = ", consoantes)
        print("a letra que mais se repete é :: ", words[0])
        
    document.close()

        
def word(arquivo): 
    with open("test/"+arquivo, "r", encoding="utf-8") as document: 
        
        words = []  
        texto = document.readlines()
        
        for i in range(len(texto)):
                palavras = texto[i].split(' ')
                for c in range(len(palavras)):
                    if('\n' in palavras[c]):
                        words.append(palavras[c].split('\n')[0])
                    else:
                        words.append(palavras[c])   
                                         
        print("palavra que mais aparece é: ",Counter(words).most_common()[0][0])
        
    document.close()

def write(arquivo):
    
    texto2 = []
    
    with open(direct +"/"+ arquivo, "r", encoding="utf-8") as document:
        with open(direct + "/Upper"+arquivo, "w") as arquivo:
            texto = document.read()
            for i in range(len(texto)):
                texto2.append(texto[i].upper())
                arquivo.write(texto2[i])
                
    document.close()
    arquivo.close()
    
for arquivo in arquivos:
        
        threads = [] #armazena os descritores das threads

        wordThread = threading.Thread(target=word, args=(arquivo,)) #inicializa a thread, informa o nome da função e os parâmetros
        wordThread.start()
        threads.append(wordThread)
        
        threadVogalConso = threading.Thread(target=vogalConso, args=(arquivo,)) #inicializa a thread, informa o nome da função e os parâmetros
        threadVogalConso.start()
        threads.append(threadVogalConso)
        
        threadWrite = threading.Thread(target=write, args=(arquivo,))
        threadWrite.start()
        threads.append(threadWrite)

    #sincroniza as threads
        for t in threads:
            t.join()