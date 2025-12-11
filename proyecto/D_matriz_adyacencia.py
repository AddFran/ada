import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import Aux_fun as af

corr_abs_b2c=pd.read_csv("corr_abs_b2c.csv", index_col=0)
corr_abs_b4c=pd.read_csv("corr_abs_b4c.csv", index_col=0)
corr_abs_b8c=pd.read_csv("corr_abs_b8c.csv", index_col=0)
corr_abs_b16c=pd.read_csv("corr_abs_b16c.csv", index_col=0)

corr_abs_w2c=pd.read_csv("corr_abs_b2c.csv", index_col=0)
corr_abs_w4c=pd.read_csv("corr_abs_b4c.csv", index_col=0)
corr_abs_w8c=pd.read_csv("corr_abs_b8c.csv", index_col=0)
corr_abs_w16c=pd.read_csv("corr_abs_b16c.csv", index_col=0)

# adj_matrix=(corr_abs>=0.6).astype(int)
# np.fill_diagonal(adj_matrix.values,0)
#adj_matrix=matriz_adyacencia(corr_matrix,0.6)
theshold_adj=0.6

# Mejores
adj_matrix_b2c=af.matriz_adyacencia(corr_abs_b2c,theshold_adj)
adj_matrix_b4c=af.matriz_adyacencia(corr_abs_b4c,theshold_adj)
adj_matrix_b8c=af.matriz_adyacencia(corr_abs_b8c,theshold_adj)
adj_matrix_b16c=af.matriz_adyacencia(corr_abs_b16c,theshold_adj)

# Peroes
adj_matrix_w2c=af.matriz_adyacencia(corr_abs_w2c,theshold_adj)
adj_matrix_w4c=af.matriz_adyacencia(corr_abs_w4c,theshold_adj)
adj_matrix_w8c=af.matriz_adyacencia(corr_abs_w8c,theshold_adj)
adj_matrix_w16c=af.matriz_adyacencia(corr_abs_w16c,theshold_adj)

plt.figure(figsize=(10,8))
sns.heatmap(
    adj_matrix_b4c,
    annot=True,
    cmap='coolwarm',
    fmt=".1f",
    annot_kws={"size": 5}
)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.title("Matriz de adyacencia (threshold aplicado)")
plt.show()

# Mejores
adj_matrix_b2c.to_csv("adj_matrix_b2c.csv", index=True)
adj_matrix_b4c.to_csv("adj_matrix_b4c.csv", index=True)
adj_matrix_b8c.to_csv("adj_matrix_b8c.csv", index=True)
adj_matrix_b16c.to_csv("adj_matrix_b16c.csv", index=True)

# Peores
adj_matrix_w2c.to_csv("adj_matrix_w2c.csv", index=True)
adj_matrix_w4c.to_csv("adj_matrix_w4c.csv", index=True)
adj_matrix_w8c.to_csv("adj_matrix_w8c.csv", index=True)
adj_matrix_w16c.to_csv("adj_matrix_w16c.csv", index=True)