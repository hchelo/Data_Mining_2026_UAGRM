import pandas as pd

# Leer el CSV original
df = pd.read_csv("sm2.csv", sep=";")

# Obtener productos únicos tal como están (con errores, espacios, etc.)
productos_con_errores = set()

for columna in df.columns:
    productos_con_errores.update(df[columna].dropna().astype(str).str.strip())

# Eliminar vacíos si los hay
productos_con_errores = {p for p in productos_con_errores if p != ''}

# Ordenar para mostrar bonito
productos_ordenados_error = sorted(productos_con_errores)

# Mostrar resultado
print(f"[ANTES DE LIMPIAR] Hay {len(productos_ordenados_error)} productos (con errores):")
print('\n '.join(productos_ordenados_error))

# Diccionario de correcciones conocidas
correcciones = {
    "Milk": "Leche",
    "Yougurt": "Yogur",
    "Mantequlla": "Mantequilla",
    "Mermedada": "Mermelada"
}

# Limpiar y corregir cada celda del DataFrame
for col in df.columns:
    df[col] = df[col].apply(
        lambda x: correcciones.get(str(x).strip(), str(x).strip()) if pd.notna(x) else x
    )

# Obtener productos únicos después de limpiar
productos_unicos = set()

for columna in df.columns:
    productos_unicos.update(df[columna].dropna().str.strip())

productos_unicos = {p for p in productos_unicos if p != ''}
productos_ordenados = sorted(productos_unicos)

# Mostrar resultado
print(f"Despues de la Limpieza hay {len(productos_ordenados)} productos que son:")
print('\n '.join(productos_ordenados))

# Guardar CSV corregido
df.to_csv("market_cleaned.csv", sep=";", index=False)
print("Archivo corregido guardado como 'market_cleaned.csv'")
