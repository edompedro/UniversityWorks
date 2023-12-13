//result: 2

#include <stdio.h>

void procedure(int a) {
    int b = 3;
    printf("%d\n", a + b);
}

int main() {
    procedure(2);
}