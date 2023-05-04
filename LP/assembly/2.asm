%include "io.inc"

section .text
global CMAIN

CMAIN:

;declaração de variaveis
    MOV AL, [numero]
    MOV BL, [divisor]

    CMP AL, 2
    CMP AL, 1

    JMP primo

;função de checagem primo
primo:
    CMP AL, BL
    xor AH, AH     
    div BL 

    CMP AH, 0
    MOV AL, [numero]
    inc BL

    JMP primo

;numero para teste
section .data
    numero DB 11
    divisor DB 2
