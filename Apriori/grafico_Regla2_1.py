import pandas as pd
import matplotlib.pyplot as plt

# Nuevos datos
data = {
    'antecedents': [
        ('Jamon', 'Dulce de leche'),
        ('Pan Molde', 'Dulce de leche'),
        ('Yogur', 'Leche'),
        ('Mantequilla', 'Azucar'),
        ('Cafe Instantaneo', 'Dulce de leche'),
    ],
    'consequents': ['Pan Molde', 'Mantequilla', 'Cafe Instantaneo', 'Yogur', 'Pan Molde'],
    'support': [0.100750, 0.099553, 0.098755, 0.098595, 0.098276],
    'confidence': [0.504396, 0.484084, 0.492240, 0.480358, 0.493189],
    'lift': [1.163120, 1.106301, 1.119224, 1.093397, 1.137277]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Crear etiquetas con salto de línea
df['label'] = df['antecedents'].apply(lambda x: '\n'.join(x)) + '\n→\n' + df['consequents']

# Escalar tamaño de puntos por lift (opcional: multiplicador ajustable)
sizes = (df['lift'] - df['lift'].min()) / (df['lift'].max() - df['lift'].min()) * 300 + 100

# Graficar
plt.figure(figsize=(10, 7))
scatter = plt.scatter(
    df['support'],
    df['confidence'],
    c=df['lift'],
    cmap='viridis',
    s=sizes,
    edgecolors='k'
)
plt.colorbar(scatter, label='Lift')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Scatter Plot de Reglas de Asociación')
plt.grid(True)

# Etiquetas
for i in range(len(df)):
    plt.text(
        df['support'][i] + 0.0002,
        df['confidence'][i] + 0.0002,
        df['label'][i],
        fontsize=9,
        ha='left'
    )

plt.tight_layout()
plt.show()
