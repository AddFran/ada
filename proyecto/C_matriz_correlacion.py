import seaborn as sns
import matplotlib.pyplot as plt
import Aux_fun as af

# df=pd.read_csv("tabla_first_025_desc.csv")
# corr_matrix=df.corr(method='pearson')
#corr_matrix=matriz_correlacion("tabla_first_025_desc.csv")

# Mejores
corr_matrix_b2c=af.matriz_correlacion("tabla_first_05_desc.csv")
corr_matrix_b4c=af.matriz_correlacion("tabla_first_025_desc.csv")
corr_matrix_b8c=af.matriz_correlacion("tabla_first_0125_desc.csv")
corr_matrix_b16c=af.matriz_correlacion("tabla_first_00625_desc.csv")

# Peroes
corr_matrix_w2c=af.matriz_correlacion("tabla_first_05_asc.csv")
corr_matrix_w4c=af.matriz_correlacion("tabla_first_025_asc.csv")
corr_matrix_w8c=af.matriz_correlacion("tabla_first_0125_asc.csv")
corr_matrix_w16c=af.matriz_correlacion("tabla_first_00625_asc.csv")

plt.figure(figsize=(10,8))
sns.heatmap(
    corr_matrix_b4c,
    annot=True,
    cmap='coolwarm',
    fmt=".1f",
    annot_kws={"size": 5}
)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.title("Matriz de correlación")
plt.show()

# Mejores
corr_abs_b2c=corr_matrix_b2c.abs()
corr_abs_b4c=corr_matrix_b4c.abs()
corr_abs_b8c=corr_matrix_b8c.abs()
corr_abs_b16c=corr_matrix_b16c.abs()

# Peores
corr_abs_w2c=corr_matrix_w2c.abs()
corr_abs_w4c=corr_matrix_w4c.abs()
corr_abs_w8c=corr_matrix_w8c.abs()
corr_abs_w16c=corr_matrix_w16c.abs()

plt.figure(figsize=(10,8))
sns.heatmap(
    corr_abs_b4c,
    annot=True,
    cmap='coolwarm',
    fmt=".1f",
    annot_kws={"size": 5}
)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.title("Matriz de correlación (valores absolutos)")
plt.show()

# Mejores
corr_abs_b2c.to_csv("corr_abs_b2c.csv", index=True)
corr_abs_b4c.to_csv("corr_abs_b4c.csv", index=True)
corr_abs_b8c.to_csv("corr_abs_b8c.csv", index=True)
corr_abs_b16c.to_csv("corr_abs_b16c.csv", index=True)

# Peores
corr_abs_w2c.to_csv("corr_abs_w2c.csv", index=True)
corr_abs_w4c.to_csv("corr_abs_w4c.csv", index=True)
corr_abs_w8c.to_csv("corr_abs_w8c.csv", index=True)
corr_abs_w16c.to_csv("corr_abs_w16c.csv", index=True)