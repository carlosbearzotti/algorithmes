import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo (x e y)
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)  # Relação perfeita: y = 2x

# Inicializando parâmetros (m = inclinação, b = intercepto)
m = 0.0
b = 0.0

# Taxa de aprendizado
alpha = 0.01

# Número de iterações
epochs = 1000

# Guardar histórico do erro
errors = []

# Gradiente Descendente
for _ in range(epochs):
    # Predição
    y_pred = m * x + b
    
    # Erro
    error = y - y_pred
    errors.append(np.mean(error**2))  # erro quadrático médio
    
    # Derivadas parciais
    dm = -(2/len(x)) * np.sum(x * error)
    db = -(2/len(x)) * np.sum(error)
    
    # Atualização dos parâmetros
    m = m - alpha * dm
    b = b - alpha * db

print(f"m final: {m:.2f}, b final: {b:.2f}")

# Plotando a reta ajustada
plt.scatter(x, y, color="blue", label="Dados")
plt.plot(x, m * x + b, color="red", label="Reta ajustada")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Plotando a evolução do erro
plt.plot(errors)
plt.xlabel("Iterações")
plt.ylabel("Erro quadrático médio")
plt.title("Convergência do Gradiente Descendente")
plt.show()
