public class FizzBuzz {
    public static void fizzBuzz(int n, int x, int y) {
        for (int i = 1; i <= n; i++) {
            if (i % x == 0 && i % y == 0) {
                System.out.println("FizzBuzz");  // Ambos
            } else if (i % x == 0) {
                System.out.println("Fizz");      // Múltiplo de x
            } else if (i % y == 0) {
                System.out.println("Buzz");      // Múltiplo de y
            } else {
                System.out.println(i);           // Não é múltiplo
            }
        }
    }

    public static void main(String[] args) {
        fizzBuzz(10, 3, 5);  // Exemplo de chamada padrão
    }
}