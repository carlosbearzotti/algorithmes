def calcular_comissao(valor_total, quantidade):
    if quantidade <= 0 or valor_total <= 0:
        return f"Venda invalida, revisar valor '{valor_total}' e Quantidade '{quantidade}' inseridos."

    valor_medio = valor_total / quantidade

    # Primeiro Caso: valor_total < 5000
    if valor_total < 5000:
        comissao = 100.0

    # Segundo Caso: 5000 <= valor_total <= 10000
    elif 5000 <= valor_total <= 10000:
        comissao = valor_total * 0.05 # 5% de comissao
        if valor_medio > 800:
            comissao += valor_total * 0.01 # 1% de comissao adicional

    # Terceiro Caso: 10000 < valor_total <= 20000
    elif 10000 < valor_total <= 20000:
        comissao = valor_total * 0.07 + 500 # 7% de comissao + 500 extra fixo
        if valor_medio > 1000:
            comissao += comissao * 0.10 # 10% de comissão adicional sobre o valor já calculado

    # Quarto Caso: valor_total > 20000
    else:  
        comissao = valor_total * 0.10 + 1000 # 10% de comissao + 1000 extra fixo
        if valor_medio > 1500:
            comissao += quantidade * 100 # quantidade de itens vendidos x 100 adicional

    return round(comissao, 2) # Arredonda para 2 casas decimais, limite de eficiencia da linguagem sem imports para números decimais em representacoes financeiras

Testes = [
    (0, 1),       # Remocao de vendas gratuitas do calculo de comissao.
    (4000, 0),    # Forçando o Erro
    (4000, 10),   # < 5000
    (8000, 5),    # 5000 ≤ total ≤ 10000, média > 800
    (8000, 20),   # 5000 ≤ total ≤ 10000, média ≤ 800
    (10000, 10),  # Exatamente 10000 e ficando no caso anterior
    (10001, 10),  # Adicionando 1 e indo para o caso seguinte
    (15000, 10),  # 10000 < total ≤ 20000, média > 1000
    (15000, 20),  # 10000 < total ≤ 20000, média ≤ 1000
    (25000, 10),  # > 20000, média > 1500
    (25000, 20)   # > 20000, média ≤ 1500
]

for valor_total, quantidade in Testes:
    resultado = calcular_comissao(valor_total, quantidade)
    if isinstance(resultado, str):
        # Caso invalido
        print(f"Valor Total={valor_total}, Quantidade={quantidade} => {resultado}")
    else:
        # Caso valido
        print(f"Valor Total={valor_total}, Quantidade={quantidade} => Comissao: R$ {resultado}")