using System;

class Program {
    static void FizzBuzz(int n, int x, int y) {
        for (int i = 1; i <= n; i++) {
            if (i % x == 0 && i % y == 0) {
                Console.WriteLine("FizzBuzz");  // Ambos
            } else if (i % x == 0) {
                Console.WriteLine("Fizz");      // Múltiplo de x
            } else if (i % y == 0) {
                Console.WriteLine("Buzz");      // Múltiplo de y
            } else {
                Console.WriteLine(i);           // Não é múltiplo
            }
        }
    }

    static void Main() {
        FizzBuzz(10, 3, 5);  // Exemplo de chamada padrão
    }
}
