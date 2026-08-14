import numpy as np
import matplotlib.pyplot as plt

# Dados
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Inicialização de parâmetros
m = 0.0
b = 0.0

alpha = 0.01  # taxa de aprendizado
epochs = 1000
n = len(x)

# Guardar histórico para visualizar
history_m = []
history_b = []
history_J = []

for _ in range(epochs):
    y_pred = m * x + b
    error = y - y_pred
    
    # Gradientes
    dm = -(2/n) * np.sum(x * error)
    db = -(2/n) * np.sum(error)
    
    # Atualização
    m = m - alpha * dm
    b = b - alpha * db
    
    # Guardar histórico
    history_m.append(m)
    history_b.append(b)
    history_J.append(np.mean(error**2))

print(f"Reta final: y = {m:.2f}x + {b:.2f}")

# Plot dos dados e reta ajustada
plt.scatter(x, y, color='blue', label='Dados')
plt.plot(x, m*x + b, color='red', label='Reta ajustada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Evolução do erro
plt.plot(history_J)
plt.xlabel('Iterações')
plt.ylabel('Erro quadrático médio')
plt.title('Convergência do Gradiente Descendente')
plt.show()
