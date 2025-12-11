import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import seaborn as sns
import Aux_fun as af

# Aplicar comunidades a cada particion no solo a una

MST_b2c=nx.read_gml("MST_b2c.gml")
MST_b4c=nx.read_gml("MST_b4c.gml")
MST_b8c=nx.read_gml("MST_b8c.gml")
MST_b16c=nx.read_gml("MST_b16c.gml")

MST_w2c=nx.read_gml("MST_w2c.gml")
MST_w4c=nx.read_gml("MST_w4c.gml")
MST_w8c=nx.read_gml("MST_w8c.gml")
MST_w16c=nx.read_gml("MST_w16c.gml")

pos_b2c=af.tree_pos(MST_b2c,'y')
pos_b4c=af.tree_pos(MST_b4c,'y')
pos_b8c=af.tree_pos(MST_b8c,'y')
pos_b16c=af.tree_pos(MST_b16c,'y')

pos_w2c=af.tree_pos(MST_w2c,'y')
pos_w4c=af.tree_pos(MST_w4c,'y')
pos_w8c=af.tree_pos(MST_w8c,'y')
pos_w16c=af.tree_pos(MST_w16c,'y')

# Cambiar segun corresponda
MST_b=MST_b16c
pos_b=pos_b16c

comunidades=list(greedy_modularity_communities(MST_b))

plt.figure(figsize=(8, 6))
colors=sns.color_palette('hls',len(comunidades))
color_map={}
for color,nodes in zip(colors,comunidades):
    for node in nodes:
        color_map[node]=color

node_colors=[color_map[node] for node in MST_b.nodes]

nx.draw_networkx(MST_b,pos_b,node_color=node_colors,with_labels=True,node_size=600)
plt.title("Comunidades detectadas (Greddy)")
plt.axis('off')
plt.show()

mod=nx.algorithms.community.modularity(MST_b,comunidades,weight='weight')
print(f"\nModularidad total: {mod:.4f}")