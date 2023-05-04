package main

import (
    "fmt"
    "math"
)

func main() {
    var n int
    var raiz int
    flag:= true 
    fmt.Print("Digite um número inteiro positivo: ")
    fmt.Scanln(&n)

    if n <= 1 {
        fmt.Print("não é primo.")
    }else{
        raiz = int(math.Sqrt(float64(n)))
        for i := 2; i <= raiz; i++ {
            if n%i == 0 {
                fmt.Print("não é primo")
                flag = false
            }
        }
        if flag{
            fmt.Print("é primo")
            
        }
    }
}