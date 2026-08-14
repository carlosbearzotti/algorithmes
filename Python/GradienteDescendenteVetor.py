import numpy as np

# Função de custo (opcional para visualização)
def J(theta):
    theta1, theta2 = theta
    return theta1**2 + 2*theta2**2

# Gradiente
def grad_J(theta):
    theta1, theta2 = theta
    return np.array([2*theta1, 4*theta2])

# Parâmetros iniciais
theta = np.array([1.0, 1.0])
alpha = 0.1
epochs = 10

# Guardar histórico
history = []

for i in range(epochs):
    history.append(theta.copy())
    theta = theta - alpha * grad_J(theta)
    print(f"Iteração {i+1}: theta = {theta}, J(theta) = {J(theta):.4f}")

# Mostrar histórico final
history = np.array(history)