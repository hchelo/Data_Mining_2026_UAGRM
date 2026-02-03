

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# URL del conjunto de datos de vino en el UCI Repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
# Nombres de las columnas
column_names = ['Class', 'Alcohol', 'MalicAcid', 'Ash', 'AlcalinityOfAsh', 'Magnesium', 'TotalPhenols', 'Flavanoids', 'NonflavanoidPhenols', 'Proanthocyanins', 'ColorIntensity', 'Hue', 'OD280_OD315', 'Proline']
# Cargar los datos en un DataFrame de pandas
data = pd.read_csv(url, names=column_names)

# Dividir los datos en características (X) y etiquetas (y)
X = data.drop('Class', axis=1)  # Características
y = data['Class']  # Etiquetas

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reducción de dimensionalidad con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Mostrar los datos en un scatter plot
plt.figure(figsize=(8, 6))
for label in range(1, 4):
    plt.scatter(X_pca[y == label, 0], X_pca[y == label, 1], label=f'Class {label}')

plt.title('Visualización de las clases de vinos')
plt.xlabel('Componente principal 1')
plt.ylabel('Componente principal 2')
plt.legend()
plt.grid(True)
plt.show()


import numpy as np

# Obtener los nombres de las características originales
features = X.columns

# Obtener los componentes principales
loadings = pca.components_

# Convertir en DataFrame para visualizar mejor
loading_df = pd.DataFrame(np.abs(loadings), columns=features, index=['PC1', 'PC2'])

# Mostrar las características ordenadas por su importancia en cada componente
for pc in loading_df.index:
    print(f"\nImportancia de caracteristicas en {pc}:")
    print(loading_df.loc[pc].sort_values(ascending=False))
    
plt.figure(figsize=(8,6))
for label in range(1, 4):
    plt.scatter(data[data['Class'] == label]['Flavanoids'],
                data[data['Class'] == label]['ColorIntensity'],
                label=f'Class {label}')
plt.xlabel('Flavanoids')
plt.ylabel('ColorIntensity')
plt.title('Separación de clases usando Flavanoids vs ColorIntensity')
plt.legend()
plt.grid(True)
plt.show()