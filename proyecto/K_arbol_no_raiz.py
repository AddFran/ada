import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import Aux_fun as af
import json

# Mejores
before_b2c,b2c=af.analizar_arbol_nr("tabla_first_05_desc.csv")
before_b4c,b4c=af.analizar_arbol_nr("tabla_first_025_desc.csv")
before_b8c,b8c=af.analizar_arbol_nr("tabla_first_0125_desc.csv")
before_b16c,b16c=af.analizar_arbol_nr("tabla_first_00625_desc.csv")

# Peroes
before_w2c,w2c=af.analizar_arbol_nr("tabla_first_05_asc.csv")
before_w4c,w4c=af.analizar_arbol_nr("tabla_first_025_asc.csv")
before_w8c,w8c=af.analizar_arbol_nr("tabla_first_0125_asc.csv")
before_w16c,w16c=af.analizar_arbol_nr("tabla_first_00625_asc.csv")

# Guardar arboles finales
af.exportar_grafo_no_enraizado(b2c, "final_nr_b2c.gml")
af.exportar_grafo_no_enraizado(b4c, "final_nr_b4c.gml")
af.exportar_grafo_no_enraizado(b8c, "final_nr_b8c.gml")
af.exportar_grafo_no_enraizado(b16c, "final_nr_b16c.gml")
af.exportar_grafo_no_enraizado(w2c, "final_nr_w2c.gml")
af.exportar_grafo_no_enraizado(w4c, "final_nr_w4c.gml")
af.exportar_grafo_no_enraizado(w8c, "final_nr_w8c.gml")
af.exportar_grafo_no_enraizado(w16c, "final_nr_w16c.gml")

pos1=af.tree_pos(b2c,'y')
pos2=af.tree_pos(w2c,'y')
pos3=af.tree_pos(b4c,'y')
pos4=af.tree_pos(w4c,'y')
pos5=af.tree_pos(b8c,'y')
pos6=af.tree_pos(w8c,'y')
pos7=af.tree_pos(b16c,'y')
pos8=af.tree_pos(w16c,'y')

pos1b=af.tree_pos(before_b2c,'y')
pos2b=af.tree_pos(before_w2c,'y')
pos3b=af.tree_pos(before_b4c,'y')
pos4b=af.tree_pos(before_w4c,'y')
pos5b=af.tree_pos(before_b8c,'y')
pos6b=af.tree_pos(before_w8c,'y')
pos7b=af.tree_pos(before_b16c,'y')
pos8b=af.tree_pos(before_w16c,'y')

##############################

plt.figure(figsize=(14,6))
# Arbol B2C
plt.subplot(1,2,1)
nx.draw_networkx(b8c, pos5, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=6,width=0.5)
plt.title("Contraparte mejor")
plt.axis('off')

# Arbol W2C
plt.subplot(1,2,2)
nx.draw_networkx(w8c, pos6, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=6,width=0.5)
plt.title("Contraparte peor")
plt.axis('off')

plt.show()

##############################

# Conparacion antes despues
plt.figure(figsize=(14,6))
# Arbol B2C
plt.subplot(2,4,1)
nx.draw_networkx(b2c, pos1, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B2C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,5)
nx.draw_networkx(before_b2c, pos1b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B2C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,2)
nx.draw_networkx(b4c, pos3, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B4C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,6)
nx.draw_networkx(before_b4c, pos3b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B4C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,3)
nx.draw_networkx(b8c, pos5, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B8C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,7)
nx.draw_networkx(before_b8c, pos5b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B8C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,4)
nx.draw_networkx(b16c, pos7, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B16C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,8)
nx.draw_networkx(before_b16c, pos7b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B16C antes")
plt.axis('off')

plt.show()


##########################


plt.figure(figsize=(14,6))
# Arbol B2C
plt.subplot(2,4,1)
nx.draw_networkx(w2c, pos2, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W2C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,5)
nx.draw_networkx(before_w2c, pos2b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W2C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,2)
nx.draw_networkx(w4c, pos4, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("w4C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,6)
nx.draw_networkx(before_w4c, pos4b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W4C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,3)
nx.draw_networkx(w8c, pos6, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("w8C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,7)
nx.draw_networkx(before_w8c, pos6b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W8C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,4)
nx.draw_networkx(w16c, pos8, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("w16C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,8)
nx.draw_networkx(before_w16c, pos8b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W16C antes")
plt.axis('off')

plt.show()

af.gml_to_dist_matrix("final_nr_b2c.gml","dist_top_matrix_b2c.csv")
af.gml_to_dist_matrix("final_nr_b4c.gml","dist_top_matrix_b4c.csv")
af.gml_to_dist_matrix("final_nr_b8c.gml","dist_top_matrix_b8c.csv")
af.gml_to_dist_matrix("final_nr_b16c.gml","dist_top_matrix_b16c.csv")
af.gml_to_dist_matrix("final_nr_w2c.gml","dist_top_matrix_w2c.csv")
af.gml_to_dist_matrix("final_nr_w4c.gml","dist_top_matrix_w4c.csv")
af.gml_to_dist_matrix("final_nr_w8c.gml","dist_top_matrix_w8c.csv")
af.gml_to_dist_matrix("final_nr_w16c.gml","dist_top_matrix_w16c.csv")

# Comparacion entre arboles
bw2c=af.comparar_arboles(b2c,w2c)
bw4c=af.comparar_arboles(b4c,w4c)
bw8c=af.comparar_arboles(b8c,w8c)
bw16c=af.comparar_arboles(b16c,w16c)

bw2c_2=af.comparar_arboles_m2("dist_top_matrix_b2c.csv","dist_top_matrix_w2c.csv")
bw4c_2=af.comparar_arboles_m2("dist_top_matrix_b4c.csv","dist_top_matrix_w4c.csv")
bw8c_2=af.comparar_arboles_m2("dist_top_matrix_b8c.csv","dist_top_matrix_w8c.csv")
bw16c_2=af.comparar_arboles_m2("dist_top_matrix_b16c.csv","dist_top_matrix_w16c.csv")

print("Resultado (metodo propio):")
print("Difieren 0.5   : ",bw2c)
print("Difieren 0.25  : ",bw4c)
print("Difieren 0.125 : ",bw8c)
print("Difieren 0.0625: ",bw16c)
print("Resultado (metodo matriz):")
print("Difieren 0.5   : ",bw2c_2)
print("Difieren 0.25  : ",bw4c_2)
print("Difieren 0.125 : ",bw8c_2)
print("Difieren 0.0625: ",bw16c_2)

union_t2=af.unir_listas(af.unir_listas(bw2c,bw4c),af.unir_listas(bw8c,bw16c))
print("Union sin raíz : ",union_t2)

with open("z_resultado_no_raiz.json", "w") as f:
    json.dump(union_t2, f)