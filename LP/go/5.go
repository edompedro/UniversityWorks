package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    counter := 0
    fmt.Println("Digite uma frase:")
    scanner.Scan()
    frase := scanner.Text()

    fmt.Println("Digite uma palavra para procurar:")
    scanner.Scan()
    palavra := scanner.Text()

    palavras := strings.Split(frase, " ")
    for i := 0; i< len(palavras); i++{
        counter += contarOcorrencias(palavras[i], palavra)
    }
    fmt.Printf("A palavra '%s' ocorre %d vezes na frase.\n", palavra, counter)
}

func contarOcorrencias(frase, palavra string) int {
   
    ocorrencias := 0
    index := strings.Index(frase, palavra)

    for index != -1 {
        ocorrencias++
        index = strings.Index(frase[index+1:], palavra)
        if index != -1 {
            index += ocorrencias * len(palavra)
        }
    }
    return ocorrencias
}