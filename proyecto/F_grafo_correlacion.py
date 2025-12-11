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

pos_b2c=nx.spring_layout(G_b2c,seed=42)
pos_b4c=nx.spring_layout(G_b4c,seed=42)
pos_b8c=nx.spring_layout(G_b8c,seed=42)
pos_b16c=nx.spring_layout(G_b16c,seed=42)
pos_w2c=nx.spring_layout(G_w2c,seed=42)
pos_w4c=nx.spring_layout(G_w4c,seed=42)
pos_w8c=nx.spring_layout(G_w8c,seed=42)
pos_w16c=nx.spring_layout(G_w16c,seed=42)

#######################
G=G_w2c
pos=pos_w2c
########################

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.7)
nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
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