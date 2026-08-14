<?php
function calcular_comissao($valor_total, $quantidade) {
    if ($quantidade <= 0 || $valor_total <= 0) {
        return "Venda invalida, revisar valor '$valor_total' e Quantidade '$quantidade' inseridos.";
    }

    $valor_medio = $valor_total / $quantidade;

    // Primeiro Caso: valor_total < 5000
    if ($valor_total < 5000) {
        $comissao = 100.0;

    // Segundo Caso: 5000 <= valor_total <= 10000
    } elseif ($valor_total >= 5000 && $valor_total <= 10000) {
        $comissao = $valor_total * 0.05; // 5% de comissao
        if ($valor_medio > 800) {
            $comissao += $valor_total * 0.01; // 1% adicional
        }

    // Terceiro Caso: 10000 < valor_total <= 20000
    } elseif ($valor_total > 10000 && $valor_total <= 20000) {
        $comissao = $valor_total * 0.07 + 500; // 7% + 500 fixo
        if ($valor_medio > 1000) {
            $comissao += $comissao * 0.10; // 10% adicional sobre a comissão já calculada
        }

    // Quarto Caso: valor_total > 20000
    } else {
        $comissao = $valor_total * 0.10 + 1000; // 10% + 1000 fixo
        if ($valor_medio > 1500) {
            $comissao += $quantidade * 100; // 100 por item
        }
    }

    return round($comissao, 2); // Arredonda para 2 casas decimais
}

$Testes = [
    [0, 1],
    [4000, 0],
    [4000, 10],
    [8000, 5],
    [8000, 20],
    [10000, 10],
    [10001, 10],
    [15000, 10],
    [15000, 20],
    [25000, 10],
    [25000, 20]
];

foreach ($Testes as $teste) {
    $valor_total = $teste[0];
    $quantidade = $teste[1];
    $resultado = calcular_comissao($valor_total, $quantidade);

    if (is_string($resultado)) {
        echo "Valor Total=$valor_total, Quantidade=$quantidade => $resultado\n";
    } else {
        echo "Valor Total=$valor_total, Quantidade=$quantidade => Comissao: R$ $resultado\n";
    }
}
?>
