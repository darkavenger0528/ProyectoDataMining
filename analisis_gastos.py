import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_csv("gastos_personales_justin.csv", parse_dates=["fecha"])

print(df.head())
print(df.info())
print(df.describe())

# 2. Ver si hay nulos o duplicados
print("Nulos por columna:")
print(df.isnull().sum())
print("Duplicados:", df.duplicated().sum())

# 3. Gasto total y por categoría
gasto_total = df["monto"].sum()
print("Gasto total:", gasto_total)

gasto_categoria = df.groupby("categoria")["monto"].sum().sort_values(ascending=False)
print(gasto_categoria)

# 4. Gasto por método de pago
gasto_metodo = df.groupby("metodo_pago")["monto"].sum().sort_values(ascending=False)
print(gasto_metodo)

# 5. Gasto diario (serie temporal)
gasto_diario = df.groupby("fecha")["monto"].sum()

# 6. Nuevas variables agregadas
# Gasto total por día y categoría (tabla dinámica)
tabla_dia_cat = df.pivot_table(
    index="fecha",
    columns="categoria",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

# Gasto total por mes
df["mes"] = df["fecha"].dt.to_period("M")
gasto_mes = df.groupby("mes")["monto"].sum()
print(gasto_mes)
#Graficos 
plt.style.use("seaborn-v0_8")

# 1. Barras: gasto total por categoría
plt.figure(figsize=(8,4))
gasto_categoria.plot(kind="bar", color="skyblue")
plt.title("Gasto total por categoría")
plt.ylabel("Monto ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Barras: gasto por método de pago
plt.figure(figsize=(6,4))
gasto_metodo.plot(kind="bar", color="salmon")
plt.title("Gasto total por método de pago")
plt.ylabel("Monto ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Línea: gasto diario
plt.figure(figsize=(10,4))
gasto_diario.plot(kind="line", marker="o", linewidth=1)
plt.title("Gasto diario total")
plt.ylabel("Monto ($)")
plt.xlabel("Fecha")
plt.tight_layout()
plt.show()

# 4. Stacked area: gasto por categoría en el tiempo
plt.figure(figsize=(10,4))
tabla_dia_cat_sorted = tabla_dia_cat.sort_index()
plt.stackplot(
    tabla_dia_cat_sorted.index,
    [tabla_dia_cat_sorted[col] for col in tabla_dia_cat_sorted.columns],
    labels=tabla_dia_cat_sorted.columns
)
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.title("Evolución del gasto por categoría")
plt.ylabel("Monto ($)")
plt.xlabel("Fecha")
plt.tight_layout()
plt.show()

#Data Mining

# Top 3 categorías
top3_cat = gasto_categoria.head(3)
print("Top 3 categorías:\\n", top3_cat)

# Método de pago más usado
print("Gasto por método:\\n", gasto_metodo)

# Días con gasto muy alto (percentil 90)
umbral_alto = gasto_diario.quantile(0.9)
dias_alto_gasto = gasto_diario[gasto_diario >= umbral_alto]
print("Días con gasto muy alto (>= p90):")
print(dias_alto_gasto)
