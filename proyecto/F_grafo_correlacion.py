import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import Aux_fun as af

adj_matrix_b2c=pd.read_csv("adj_matrix_b2c.csv", index_col=0)
adj_matrix_b4c=pd.read_csv("adj_matrix_b4c.csv", index_col=0)
adj_matrix_b8c=pd.read_csv("adj_matrix_b8c.csv", index_col=0)
adj_matrix_b16c=pd.read_csv("adj_matrix_b16c.csv", index_col=0)

adj_matrix_w2c=pd.read_csv("adj_matrix_b2c.csv", index_col=0)
adj_matrix_w4c=pd.read_csv("adj_matrix_b4c.csv", index_col=0)
adj_matrix_w8c=pd.read_csv("adj_matrix_b8c.csv", index_col=0)
adj_matrix_w16c=pd.read_csv("adj_matrix_b16c.csv", index_col=0)


dist_matrix_b2c=pd.read_csv("dist_matrix_b2c.csv", index_col=0)
dist_matrix_b4c=pd.read_csv("dist_matrix_b4c.csv", index_col=0)
dist_matrix_b8c=pd.read_csv("dist_matrix_b8c.csv", index_col=0)
dist_matrix_b16c=pd.read_csv("dist_matrix_b16c.csv", index_col=0)

dist_matrix_w2c=pd.read_csv("dist_matrix_b2c.csv", index_col=0)
dist_matrix_w4c=pd.read_csv("dist_matrix_b4c.csv", index_col=0)
dist_matrix_w8c=pd.read_csv("dist_matrix_b8c.csv", index_col=0)
dist_matrix_w16c=pd.read_csv("dist_matrix_b16c.csv", index_col=0)

# Mejores
G_b2c=af.grafo_correlacion(adj_matrix_b2c,dist_matrix_b2c)
G_b4c=af.grafo_correlacion(adj_matrix_b4c,dist_matrix_b4c)
G_b8c=af.grafo_correlacion(adj_matrix_b8c,dist_matrix_b8c)
G_b16c=af.grafo_correlacion(adj_matrix_b16c,dist_matrix_b16c)

# Mejores
G_w2c=af.grafo_correlacion(adj_matrix_w2c,dist_matrix_w2c)
G_w4c=af.grafo_correlacion(adj_matrix_w4c,dist_matrix_w4c)
G_w8c=af.grafo_correlacion(adj_matrix_w8c,dist_matrix_w8c)
G_w16c=af.grafo_correlacion(adj_matrix_w16c,dist_matrix_w16c)

pos=nx.spring_layout(G_b4c,seed=42)

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G_b4c, pos, node_size=500, node_color='skyblue')
nx.draw_networkx_edges(G_b4c, pos, width=1.0, alpha=0.7)
nx.draw_networkx_labels(G_b4c, pos, font_size=8, font_color='black')
plt.title("Grafo de correlaciones")
plt.axis('off')
plt.show()

nx.write_gml(G_b2c, "G_b2c.gml")
nx.write_gml(G_b4c, "G_b4c.gml")
nx.write_gml(G_b8c, "G_b8c.gml")
nx.write_gml(G_b16c, "G_b16c.gml")

nx.write_gml(G_w2c, "G_w2c.gml")
nx.write_gml(G_w4c, "G_w4c.gml")
nx.write_gml(G_w8c, "G_w8c.gml")
nx.write_gml(G_w16c, "G_w16c.gml")