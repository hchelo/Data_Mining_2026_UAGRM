import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo
data = {
    'antecedents': ['Mermelada', 'Dulce de leche', 'Azucar', 'Leche', 'Cafe Instantaneo',
                    'Pan', 'Mantequilla', 'Leche', 'Queso', 'Mermelada'],
    'consequents': ['Cafe Instantaneo', 'Pan Molde', 'Mantequilla', 'Azucar', 'Yogur',
                    'Jamon', 'Dulce de leche', 'Pan Molde', 'Yogur', 'Mantequilla'],
    'support': [0.205812, 0.205652, 0.205253, 0.204614, 0.203976,
                0.203337, 0.203018, 0.202698, 0.202140, 0.201980],
    'confidence': [0.467877, 0.469816, 0.468989, 0.463807, 0.463787,
                   0.464442, 0.463966, 0.459464, 0.462381, 0.459165],
    'lift': [1.063827, 1.083379, 1.071805, 1.059769, 1.055677,
             1.069412, 1.059939, 1.059509, 1.052478, 1.049353]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['support'], df['confidence'],
                      c=df['lift'], cmap='viridis', s=100, edgecolor='k')
plt.colorbar(scatter, label='Lift')
for i, row in df.iterrows():
    plt.text(row['support'], row['confidence'], f"{row['antecedents']}→{row['consequents']}",
             fontsize=8, ha='right')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Asociación de Reglas: Support vs Confidence (color = Lift)')
plt.grid(True)
plt.tight_layout()
plt.show()



# Grafico 2
# Escalar lift para el tamaño de los puntos (multiplicador ajustable)
# Normalizar lift y escalar para tamaño visible
lift_min = df['lift'].min()
lift_max = df['lift'].max()
df['lift_scaled'] = (df['lift'] - lift_min) / (lift_max - lift_min)  # rango 0 a 1
df['lift_scaled'] = df['lift_scaled'] * 400 + 100  # rango ajustado para tamaño

# Crear el scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['support'], df['confidence'],
                      c=df['lift'], cmap='viridis', s=df['lift_scaled'],
                      edgecolor='k', alpha=0.8)
plt.colorbar(scatter, label='Lift')

# Etiquetas
for i, row in df.iterrows():
    label = f"{row['antecedents']}→{row['consequents']}"
    plt.text(row['support'] + 0.0001, row['confidence'] + 0.0001,
             label, fontsize=8, ha='left')

plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Asociación de Reglas: Soporte vs Confianza (Tamaño y Color = Lift)')
plt.grid(True)
plt.tight_layout()
plt.show()