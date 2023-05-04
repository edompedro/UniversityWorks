package main
import "fmt"

func main() {
    f := 0.0
    fmt.Println("Informe uma temperatura em Fahrenheit: ")
    fmt.Scanf("%f",&f)
    fmt.Println(((f-32)*5)/9)
}