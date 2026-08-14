from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Exemplo de dataset
data = pd.DataFrame({
    'X1': [2, 4, 6, 8],
    'X2': [1, 3, 5, 7],
    'X3': [2, 2, 2, 2]
})

# Normalizar os dados
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Aplicar PCA
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

print("Componentes principais:\n", data_pca)
print("Variância explicada:", pca.explained_variance_ratio_)
