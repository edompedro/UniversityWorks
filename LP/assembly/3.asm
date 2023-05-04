%include "io.inc"

section .text
global CMAIN

CMAIN:

;declarando as variaveis
    MOV EAX, 1
    MOV ECX, [numero]

;função para ver se é impar
    nums_impar:

        PRINT_UDEC 4, EAX
        ADD EAX,2
        LOOP nums_impar

    ret

;numero para teste
section .data
    numero DD 9