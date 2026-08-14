"""Cálculo de comissão de vendas por faixa de valor total.

Versão com funções auxiliares separadas por faixa de faturamento.
"""
def comissao_ate_5000(valor_total):
    return 100.0

def comissao_5000_a_10000(valor_total, valor_medio):
    comissao = valor_total * 0.05
    if valor_medio > 800:
        comissao += valor_total * 0.01
    return comissao

def comissao_10000_a_20000(valor_total, valor_medio):
    comissao = valor_total * 0.07 + 500
    if valor_medio > 1000:
        comissao += comissao * 0.10
    return comissao

def comissao_acima_20000(valor_total, quantidade, valor_medio):
    comissao = valor_total * 0.10 + 1000
    if valor_medio > 1500:
        comissao += quantidade * 100
    return comissao

def calcular_comissao(valor_total, quantidade):
    if quantidade <= 0:
        return "Venda inválida."

    valor_medio = valor_total / quantidade

    if valor_total < 5000:
        return round(comissao_ate_5000(valor_total), 2)

    if valor_total <= 10000:
        return round(comissao_5000_a_10000(valor_total, valor_medio), 2)

    if valor_total <= 20000:
        return round(comissao_10000_a_20000(valor_total, valor_medio), 2)

    return round(comissao_acima_20000(valor_total, quantidade, valor_medio), 2)


def main():
    casos_teste = [
        (4000, 0),    # Forçando o erro
        (4000, 10),   # < 5000
        (8000, 5),    # 5000 ≤ total ≤ 10000, média > 800
        (8000, 20),   # 5000 ≤ total ≤ 10000, média ≤ 800
        (10000, 10),  # Exatamente 10000
        (10001, 10),  # 10000 < total ≤ 20000
        (15000, 10),  # 10000 < total ≤ 20000, média > 1000
        (15000, 20),  # 10000 < total ≤ 20000, média ≤ 1000
        (25000, 10),  # > 20000, média > 1500
        (25000, 20)   # > 20000, média ≤ 1500
    ]

    for valor_total, quantidade in casos_teste:
        resultado = calcular_comissao(valor_total, quantidade)
        if isinstance(resultado, str):
            print(f"Valor Total={valor_total}, Quantidade={quantidade} => {resultado}")
        else:
            print(f"Valor Total={valor_total}, Quantidade={quantidade} => Comissão: R$ {resultado}")

if __name__ == "__main__":
    main()
