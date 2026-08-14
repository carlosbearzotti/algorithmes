import numpy as np

# Dados simples (x -> y = 2x)
x = np.array([[1],[2],[3],[4],[5]], dtype=float)
y = np.array([[2],[4],[6],[8],[10]], dtype=float)

# Inicializar peso e viés
w = np.random.randn(1,1)
b = np.random.randn(1)

alpha = 0.01
epochs = 1000

for i in range(epochs):
    # Forward
    y_pred = x.dot(w) + b
    
    # Erro
    error = y_pred - y
    J = np.mean(error**2)
    
    # Gradiente
    dw = (2/len(x)) * x.T.dot(error)
    db = (2/len(x)) * np.sum(error)
    
    # Atualizar pesos
    w = w - alpha * dw
    b = b - alpha * db
    
print(f"Peso final: {w[0][0]:.2f}, viés final: {b[0]:.2f}")
