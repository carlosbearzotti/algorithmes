def fizzBuzz(n, x, y):
    for i in range(1, n + 1):
        if i % x == 0 and i % y == 0:
            print("FizzBuzz")  # Ambos
        elif i % x == 0:
            print("Fizz")      # Múltiplo de x
        elif i % y == 0:
            print("Buzz")      # Múltiplo de y
        else:
            print(i)           # Não é múltiplo

# Exemplo de chamada padrão
fizzBuzz(10, 3, 5)