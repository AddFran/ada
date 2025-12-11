import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
import pandas as pd

#dist_matrix=1-corr_abs

corr_abs_b2c=pd.read_csv("corr_abs_b2c.csv", index_col=0)
corr_abs_b4c=pd.read_csv("corr_abs_b4c.csv", index_col=0)
corr_abs_b8c=pd.read_csv("corr_abs_b8c.csv", index_col=0)
corr_abs_b16c=pd.read_csv("corr_abs_b16c.csv", index_col=0)

corr_abs_w2c=pd.read_csv("corr_abs_b2c.csv", index_col=0)
corr_abs_w4c=pd.read_csv("corr_abs_b4c.csv", index_col=0)
corr_abs_w8c=pd.read_csv("corr_abs_b8c.csv", index_col=0)
corr_abs_w16c=pd.read_csv("corr_abs_b16c.csv", index_col=0)

# Mejores
dist_matrix_b2c=1-corr_abs_b2c
dist_matrix_b4c=1-corr_abs_b4c
dist_matrix_b8c=1-corr_abs_b8c
dist_matrix_b16c=1-corr_abs_b16c

# Mejores
dist_matrix_w2c=1-corr_abs_w2c
dist_matrix_w4c=1-corr_abs_w4c
dist_matrix_w8c=1-corr_abs_w8c
dist_matrix_w16c=1-corr_abs_w16c

plt.figure(figsize=(10,8))
sns.heatmap(
    dist_matrix_b4c,
    annot=True,
    cmap='coolwarm',
    fmt=".1f",
    annot_kws={"size": 5}
)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.title("Matriz de distancia")
plt.show()

Z=linkage(squareform(dist_matrix_b4c), method='average')
dendrogram(Z,labels=corr_abs_b4c.columns,leaf_font_size=6)
plt.show()

# Mejores
dist_matrix_b2c.to_csv("dist_matrix_b2c.csv", index=True)
dist_matrix_b4c.to_csv("dist_matrix_b4c.csv", index=True)
dist_matrix_b8c.to_csv("dist_matrix_b8c.csv", index=True)
dist_matrix_b16c.to_csv("dist_matrix_b16c.csv", index=True)

# Peores
dist_matrix_w2c.to_csv("dist_matrix_w2c.csv", index=True)
dist_matrix_w4c.to_csv("dist_matrix_w4c.csv", index=True)
dist_matrix_w8c.to_csv("dist_matrix_w8c.csv", index=True)
dist_matrix_w16c.to_csv("dist_matrix_w16c.csv", index=True)