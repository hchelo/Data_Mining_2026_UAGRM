import matplotlib.pyplot as plt

# Productos y cantidades reales
productos = [
    "Leche", "Mermelada", "Cafe Instantaneo", "Yogur", "Pan",
    "Dulce de leche", "Azucar", "Mantequilla", "Queso", "Jamon"
]
cantidades = [5526, 5510, 5509, 5503, 5484, 5483, 5482, 5481, 5476, 5440]

# Escalar valores entre 10% y 100%
min_val = min(cantidades)
max_val = max(cantidades)
valores_escalados = [10 + (x - min_val) * (100 - 10) / (max_val - min_val) for x in cantidades]

# Crear gráfico
plt.figure(figsize=(10, 6))
barras = plt.bar(productos, valores_escalados, color='skyblue', edgecolor='black')

# Agregar porcentajes encima de las barras
for bar, valor in zip(barras, cantidades):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f"{valor:.1f}", ha='center', va='bottom', fontsize=9)

# Títulos y etiquetas
plt.title("Popularidad de productos (escalada 10%–100%)")
plt.ylabel("Popularidad relativa (%)")
plt.xticks(rotation=45)
plt.ylim(0, 110)  # Para dejar espacio arriba del 100%

plt.tight_layout()
plt.show()
