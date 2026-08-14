import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Dados: altura e peso
X = np.array([
    [150, 50],
    [160, 55],
    [170, 65],
    [180, 80],
    [190, 85]
])

# Criar KMeans com 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Labels (cluster de cada ponto)
print("Clusters atribuídos:", kmeans.labels_)

# Centroides
print("Centroides:", kmeans.cluster_centers_)

# Visualização
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], 
            color='black', marker='X', s=200, label='Centroides')
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.legend()
plt.show()
