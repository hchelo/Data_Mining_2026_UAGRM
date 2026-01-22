import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos
data = {
    'antecedents': ['Cafe Instantaneo', 'Dulce de leche', 'Azucar', 'Azucar', 'Cafe Instantaneo'],
    'consequents': ['Mermelada', 'Pan Molde', 'Mantequilla', 'Leche', 'Yogur'],
    'support': [0.205812, 0.205652, 0.205253, 0.204614, 0.203976],
    'confidence': [0.467962, 0.469816, 0.468989, 0.467530, 0.463787],
    'lift': [1.063827, 1.083379, 1.071805, 1.059769, 1.055677]
}

df = pd.DataFrame(data)
df['rule'] = df['antecedents'] + " → " + df['consequents']
df_sorted = df.sort_values(by='lift', ascending=False).reset_index(drop=True)

# Configuración
n = len(df_sorted)
ind = np.arange(n)
width = 0.25

# Crear figura
fig, ax = plt.subplots(figsize=(14, 6))

# Paleta personalizada
colors = ['#4C72B0', '#55A868', '#C44E52']

# Dibujar barras con bordes
bars1 = ax.bar(ind - width, df_sorted['support'], width, label='Support', color=colors[0], edgecolor='black')
bars2 = ax.bar(ind, df_sorted['confidence'], width, label='Confidence', color=colors[1], edgecolor='black')
bars3 = ax.bar(ind + width, df_sorted['lift'], width, label='Lift', color=colors[2], edgecolor='black')

# Mostrar valores encima
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.3f}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

autolabel(bars1)
autolabel(bars2)
autolabel(bars3)

# Títulos y etiquetas
ax.set_title('Comparación de métricas para reglas de asociación (ordenadas por Lift)', fontsize=14, fontweight='bold')
ax.set_xlabel('Reglas de Asociación', fontsize=12)
ax.set_ylabel('Valor', fontsize=12)
ax.set_xticks(ind)
ax.set_xticklabels(df_sorted['rule'], rotation=45, ha='right', fontsize=10)

# Leyenda fuera del gráfico
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Líneas de fondo
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ajustar límites
ax.set_ylim(0, max(df_sorted[['support', 'confidence', 'lift']].max()) + 0.1)

plt.tight_layout()
plt.show()
