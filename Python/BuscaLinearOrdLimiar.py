def analise_limiar(predicoes, limiares):
    n = len(predicoes)
    resultado = []
    i = 0
    for limiar in limiares:
        while i < n and predicoes[i] < limiar:
            i += 1
        resultado.append(i)
    return resultado

# Exemplo de uso:
predicoes = [0.1, 0.45, 0.57, 0.65, 0.87, 0.92]
limiares = [0.5, 0.6, 0.7, 0.8, 0.9]
print(analise_limiar(predicoes, limiares))  # Saída: [2, 3, 4, 4, 5]