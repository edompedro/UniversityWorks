%include "io.inc"

section .text
global CMAIN

CMAIN:

;declaração das variaveis
    MOV EAX,[x]
    MOV EBX, 1
    MOV ECX,[y]

;função que realiza a exponenciação
    exp:

        imul EBX,EAX    ;multiplicação
    LOOP exp
    
; print do resultado
    PRINT_UDEC 4, EBX
    ret
    
section .data

;valores de teste
x DD 2
y DD 3