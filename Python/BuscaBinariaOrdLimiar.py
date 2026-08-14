import bisect

def analise_limiar_binaria(predicoes, limiares):
    """
    Retorna a quantidade de elementos em 'predicoes' menores que cada limiar em 'limiares'.
    Complexidade: O(m log n)
    """
    # Certifique-se que predicoes esteja ordenada
    predicoes.sort()  # se já estiver ordenada, pode remover

    resultado = []
    for limiar in limiares:
        # bisect_right retorna o índice do primeiro elemento > limiar
        count = bisect.bisect_left(predicoes, limiar)
        resultado.append(count)

    return resultado

predicoes = [0.1, 0.3, 0.4, 0.6, 0.8]
limiares = [0.2, 0.5, 0.7]

print(analise_limiar_binaria(predicoes, limiares))
