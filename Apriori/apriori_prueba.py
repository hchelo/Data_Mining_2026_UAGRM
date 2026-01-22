import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from collections import Counter
import matplotlib.pyplot as plt

# Leer CSV (usa tu ruta si es distinta)
df = pd.read_csv("market_cleaned.csv", sep=';')
#df = pd.read_csv("Supermercado2.csv", sep=',')

# Recorrer cada fila y recolectar productos no vacíos
todos_los_productos = []
for i in range(len(df)):
    fila = df.iloc[i].dropna().tolist()
    fila = [item.strip() for item in fila if item.strip() != '']  # Eliminar vacíos
    todos_los_productos.extend(fila)

# Contar ocurrencias
conteo = Counter(todos_los_productos)
# Mostrar los productos más frecuentes
print("Productos más frecuentes:")
for producto, cantidad in conteo.most_common(10):
    print(f"{producto}: {cantidad} veces")
#___

# Convertir cada fila en una lista de productos, ignorando vacíos
transactions = []
for i in range(len(df)):
    transaction = df.iloc[i].dropna().tolist()  # Elimina NaN
    transaction = [item for item in transaction if item != '']  # Elimina vacíos ''
    transactions.append(transaction)

# Transformar a formato booleano para Apriori
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)

# Aplicar Apriori
frequent_itemsets = apriori(df_trans, min_support=0.098, use_colnames=True)

# Reglas de asociación
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
rules = rules.sort_values(by='support', ascending=False)

rules = rules.drop_duplicates(subset='support', keep='first')

# Mostrar resultados
print("\nFrequent itemsets:")
#print(frequent_itemsets)
print(frequent_itemsets.sort_values(by='support', ascending=False).head(10))

#___



print("\nAssociation rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))

# Mostrar itemsets de 3 productos ordenados por support

rules_3_items = rules[rules['antecedents'].apply(len) == 2]
top10_3items_by_support = rules_3_items.sort_values(by='support', ascending=False).head(10)
print(top10_3items_by_support[['antecedents', 'consequents', 'support', 'confidence', 'lift']])