public class CalculaComissao {

    public static Object calcular_comissao(double valor_total, int quantidade) {
        if (quantidade <= 0 || valor_total <= 0) {
            return String.format("Venda invalida, revisar valor '%.2f' e Quantidade '%d' inseridos.", valor_total, quantidade);
        }

        double valor_medio = valor_total / quantidade;
        double comissao;

        // Primeiro Caso: valor_total < 5000
        if (valor_total < 5000) {
            comissao = 100.0;

        // Segundo Caso: 5000 <= valor_total <= 10000
        } else if (valor_total >= 5000 && valor_total <= 10000) {
            comissao = valor_total * 0.05; // 5% de comissao
            if (valor_medio > 800) {
                comissao += valor_total * 0.01; // 1% adicional
            }

        // Terceiro Caso: 10000 < valor_total <= 20000
        } else if (valor_total > 10000 && valor_total <= 20000) {
            comissao = valor_total * 0.07 + 500; // 7% + 500 fixo
            if (valor_medio > 1000) {
                comissao += comissao * 0.10; // 10% adicional sobre a comissão já calculada
            }

        // Quarto Caso: valor_total > 20000
        } else {
            comissao = valor_total * 0.10 + 1000; // 10% + 1000 fixo
            if (valor_medio > 1500) {
                comissao += quantidade * 100; // 100 por item
            }
        }

        return Math.round(comissao * 100.0) / 100.0; // Arredonda para 2 casas decimais
    }

    public static void main(String[] args) {
        Object[][] Testes = {
            {0.0, 1},
            {4000.0, 0},
            {4000.0, 10},
            {8000.0, 5},
            {8000.0, 20},
            {10000.0, 10},
            {10001.0, 10},
            {15000.0, 10},
            {15000.0, 20},
            {25000.0, 10},
            {25000.0, 20}
        };

        for (Object[] teste : Testes) {
            double valor_total = (double) teste[0];
            int quantidade = (int) teste[1];
            Object resultado = calcular_comissao(valor_total, quantidade);

            if (resultado instanceof String) {
                System.out.printf("Valor Total=%.0f, Quantidade=%d => %s%n", valor_total, quantidade, resultado);
            } else {
                System.out.printf("Valor Total=%.0f, Quantidade=%d => Comissao: R$ %.2f%n", valor_total, quantidade, (double) resultado);
            }
        }
    }
}
