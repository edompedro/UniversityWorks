package main
import "fmt"

func main() {
    n := 0
    fmt.Println("Informe um inteiro positivo: ")
    fmt.Scanf("%d",&n)
    for i:=1; i<n; i+=2{
		fmt.Println(i)
    }
}
