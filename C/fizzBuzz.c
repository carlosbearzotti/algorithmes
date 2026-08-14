#include <stdio.h>

void fizzBuzz(int n, int x, int y) {
    for (int i = 1; i <= n; i++) {
        if (i % x == 0 && i % y == 0) {
            printf("FizzBuzz\n");  // Ambos
        } else if (i % x == 0) {
            printf("Fizz\n");      // Múltiplo de x
        } else if (i % y == 0) {
            printf("Buzz\n");      // Múltiplo de y
        } else {
            printf("%d\n", i);     // Não é múltiplo
        }
    }
}

int main() {
    fizzBuzz(10, 3, 5);  // Exemplo de chamada padrão
    return 0;
}