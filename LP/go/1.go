package main
import "fmt"

func main() {
    x, n := 0,0
    fmt.Println("Informe um inteiro: ")
    fmt.Scanf("%d",&x)
    result := x
    fmt.Println("Informe um inteiro positivo: ")
    fmt.Scanf("%d",&n)
    for i:=1; i<n; i++{
        result *= x
    }
    fmt.Println("resultado = ", result)
}
