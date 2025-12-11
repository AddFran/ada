import networkx as nx
import matplotlib.pyplot as plt
import Aux_fun as af

raiz="y" 
#x_12
#x_39

MST_b2c=nx.read_gml("MST_b2c.gml")
MST_b4c=nx.read_gml("MST_b4c.gml")
MST_b8c=nx.read_gml("MST_b8c.gml")
MST_b16c=nx.read_gml("MST_b16c.gml")

MST_w2c=nx.read_gml("MST_w2c.gml")
MST_w4c=nx.read_gml("MST_w4c.gml")
MST_w8c=nx.read_gml("MST_w8c.gml")
MST_w16c=nx.read_gml("MST_w16c.gml")

new_MST_b2c=nx.bfs_tree(MST_b2c,source=raiz)
new_MST_b4c=nx.bfs_tree(MST_b4c,source=raiz)
new_MST_b8c=nx.bfs_tree(MST_b8c,source=raiz)
new_MST_b16c=nx.bfs_tree(MST_b16c,source=raiz)
new_MST_w2c=nx.bfs_tree(MST_w2c,source=raiz)
new_MST_w4c=nx.bfs_tree(MST_w4c,source=raiz)
new_MST_w8c=nx.bfs_tree(MST_w8c,source=raiz)
new_MST_w16c=nx.bfs_tree(MST_w16c,source=raiz)

pos_b2c=af.tree_pos(new_MST_b2c,raiz)
pos_b4c=af.tree_pos(new_MST_b4c,raiz)
pos_b8c=af.tree_pos(new_MST_b8c,raiz)
pos_b16c=af.tree_pos(new_MST_b16c,raiz)
pos_w2c=af.tree_pos(new_MST_w2c,raiz)
pos_w4c=af.tree_pos(new_MST_w4c,raiz)
pos_w8c=af.tree_pos(new_MST_w8c,raiz)
pos_w16c=af.tree_pos(new_MST_w16c,raiz)

new_MST=new_MST_b2c
pos=pos_b2c

# Dibujar el MST
plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(new_MST, pos, node_size=500, node_color='lightgreen')
nx.draw_networkx_edges(new_MST, pos, width=2.0, edge_color='black')
nx.draw_networkx_labels(new_MST, pos, font_size=8)

# Dibujar etiquetas con pesos
edge_labels=nx.get_edge_attributes(new_MST, 'weight')
edge_labels={k: round(v, 3) for k, v in edge_labels.items()}
nx.draw_networkx_edge_labels(new_MST, pos, edge_labels=edge_labels, font_size=7, font_color='red')

plt.title(f"MST enraizado en la variable {raiz}")
plt.axis('off')
plt.show()

# Ejecutar DFS desde la raíz
print("Recorrido en profundidad:")
orden_dfs=af.dfs(new_MST,raiz)
print(orden_dfs)

print("Recorrido en anchura:")
orden_bfs=af.bfs(new_MST,raiz)
print(orden_bfs)

af.exportar_grafo_enraizado(new_MST_b2c, raiz, 'new_MST_b2c.gml')
af.exportar_grafo_enraizado(new_MST_b4c, raiz, 'new_MST_b4c.gml')
af.exportar_grafo_enraizado(new_MST_b8c, raiz, 'new_MST_b8c.gml')
af.exportar_grafo_enraizado(new_MST_b16c,raiz, 'new_MST_b16c.gml')

af.exportar_grafo_enraizado(new_MST_w2c, raiz, 'new_MST_w2c.gml')
af.exportar_grafo_enraizado(new_MST_w4c, raiz, 'new_MST_w4c.gml')
af.exportar_grafo_enraizado(new_MST_w8c, raiz, 'new_MST_w8c.gml')
af.exportar_grafo_enraizado(new_MST_w16c, raiz, 'new_MST_w16c.gml')