import matplotlib.pyplot as plt
import networkx as nx

# Algoritmo
alg="prim"
# Agregar por algoritmo PRIM <-

G_b2c=nx.read_gml("G_b2c.gml")
G_b4c=nx.read_gml("G_b4c.gml")
G_b8c=nx.read_gml("G_b8c.gml")
G_b16c=nx.read_gml("G_b16c.gml")

G_w2c=nx.read_gml("G_w2c.gml")
G_w4c=nx.read_gml("G_w4c.gml")
G_w8c=nx.read_gml("G_w8c.gml")
G_w16c=nx.read_gml("G_w16c.gml")

# Mejores
MST_b2c=nx.minimum_spanning_tree(G_b2c,weight='weight',algorithm=alg)
MST_b4c=nx.minimum_spanning_tree(G_b4c,weight='weight',algorithm=alg)
MST_b8c=nx.minimum_spanning_tree(G_b8c,weight='weight',algorithm=alg)
MST_b16c=nx.minimum_spanning_tree(G_b16c,weight='weight',algorithm=alg)

# Peores
MST_w2c=nx.minimum_spanning_tree(G_w2c,weight='weight',algorithm=alg)
MST_w4c=nx.minimum_spanning_tree(G_w4c,weight='weight',algorithm=alg)
MST_w8c=nx.minimum_spanning_tree(G_w8c,weight='weight',algorithm=alg)
MST_w16c=nx.minimum_spanning_tree(G_w16c,weight='weight',algorithm=alg)

# Mejores
pos_b2c=nx.spring_layout(MST_b2c,seed=42)
pos_b4c=nx.spring_layout(MST_b4c,seed=42)
pos_b8c=nx.spring_layout(MST_b8c,seed=42)
pos_b16c=nx.spring_layout(MST_b16c,seed=42)

# Peores
pos_w2c=nx.spring_layout(MST_w2c,seed=42)
pos_w4c=nx.spring_layout(MST_w4c,seed=42)
pos_w8c=nx.spring_layout(MST_w8c,seed=42)
pos_w16c=nx.spring_layout(MST_w16c,seed=42)

MSTb=MST_b16c
posb=pos_b16c

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(MSTb, posb, node_size=500, node_color='lightgreen')
nx.draw_networkx_edges(MSTb, posb, width=2.0, edge_color='black')
nx.draw_networkx_labels(MSTb, posb, font_size=8)
plt.title("Árbol de Expansión Mínima")
plt.axis('off')
plt.show()

nx.write_gml(MST_b2c, "MST_b2c.gml")
nx.write_gml(MST_b4c, "MST_b4c.gml")
nx.write_gml(MST_b8c, "MST_b8c.gml")
nx.write_gml(MST_b16c, "MST_b16c.gml")

nx.write_gml(MST_w2c, "MST_w2c.gml")
nx.write_gml(MST_w4c, "MST_w4c.gml")
nx.write_gml(MST_w8c, "MST_w8c.gml")
nx.write_gml(MST_w16c, "MST_w16c.gml")