<?php
function fizzBuzz($n, $x, $y) {
    for ($i = 1; $i <= $n; $i++) {
        if ($i % $x == 0 && $i % $y == 0) {
            echo "FizzBuzz\n";  // Ambos
        } elseif ($i % $x == 0) {
            echo "Fizz\n";  // Múltiplo de x
        } elseif ($i % $y == 0) {
            echo "Buzz\n";  // Múltiplo de y
        } else {
            echo $i . "\n"; // Não é múltiplo
        }
    }
}

// Exemplo de chamada padrão
fizzBuzz(10, 3, 5);
?>