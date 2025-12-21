import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import Aux_fun as af
import json

theshold=1

g=nx.read_gml("new_MST_b2c.gml")

# Mejores
b2c_before,b2c=af.analizar_arbol("new_MST_b2c.gml",g.graph["root"],theshold)
b4c_before,b4c=af.analizar_arbol("new_MST_b4c.gml",g.graph["root"],theshold)
b8c_before,b8c=af.analizar_arbol("new_MST_b8c.gml",g.graph["root"],theshold)
b16c_before,b16c=af.analizar_arbol("new_MST_b16c.gml",g.graph["root"],theshold)

# Peores
w2c_before,w2c=af.analizar_arbol("new_MST_w2c.gml",g.graph["root"],theshold)
w4c_before,w4c=af.analizar_arbol("new_MST_w4c.gml",g.graph["root"],theshold)
w8c_before,w8c=af.analizar_arbol("new_MST_w8c.gml",g.graph["root"],theshold)
w16c_before,w16c=af.analizar_arbol("new_MST_w16c.gml",g.graph["root"],theshold)

# De cada particion 0.5 0.25... ()
# interseccion
# 
# lista_b2c =af.unir_listas(af.bfs(b2c,g.graph["root"]),af.dfs(b2c,g.graph["root"]))
# lista_w2c =af.unir_listas(af.bfs(w2c,g.graph["root"]),af.dfs(w2c,g.graph["root"]))
# lista_b4c =af.unir_listas(af.bfs(b4c,g.graph["root"]),af.dfs(b4c,g.graph["root"]))
# lista_w4c =af.unir_listas(af.bfs(w4c,g.graph["root"]),af.dfs(w4c,g.graph["root"]))
# lista_b8c =af.unir_listas(af.bfs(b8c,g.graph["root"]),af.dfs(b8c,g.graph["root"]))
# lista_w8c =af.unir_listas(af.bfs(w8c,g.graph["root"]),af.dfs(w8c,g.graph["root"]))
# lista_b16c=af.unir_listas(af.bfs(b16c,g.graph["root"]),af.dfs(b16c,g.graph["root"]))
# lista_w16c=af.unir_listas(af.bfs(w16c,g.graph["root"]),af.dfs(w16c,g.graph["root"]))

lista_b2c = list(set(af.bfs(b2c,g.graph["root"]) ) & set(af.dfs(b2c,g.graph["root"])))
lista_w2c = list(set(af.bfs(w2c,g.graph["root"]) ) & set(af.dfs(w2c,g.graph["root"])))
lista_b4c = list(set(af.bfs(b4c,g.graph["root"]) ) & set(af.dfs(b4c,g.graph["root"])))
lista_w4c = list(set(af.bfs(w4c,g.graph["root"]) ) & set(af.dfs(w4c,g.graph["root"])))
lista_b8c = list(set(af.bfs(b8c,g.graph["root"]) ) & set(af.dfs(b8c,g.graph["root"])))
lista_w8c = list(set(af.bfs(w8c,g.graph["root"]) ) & set(af.dfs(w8c,g.graph["root"])))
lista_b16c= list(set(af.bfs(b16c,g.graph["root"])) & set(af.dfs(b16c,g.graph["root"])))
lista_w16c= list(set(af.bfs(w16c,g.graph["root"])) & set(af.dfs(w16c,g.graph["root"])))

lista_bw2c =list(set(lista_b2c) & set(lista_w2c)) 
lista_bw4c =list(set(lista_b4c) & set(lista_w4c)) 
lista_bw8c =list(set(lista_b8c) & set(lista_w8c)) 
lista_bw16c=list(set(lista_b16c) & set(lista_w16c)) 

union_t=af.unir_listas(af.unir_listas(lista_bw2c,lista_bw4c),af.unir_listas(lista_bw8c,lista_bw16c))
#pos1=graphviz_layout(b2c, prog='dot')
pos1=af.tree_pos(b2c,g.graph["root"])
pos2=af.tree_pos(w2c,g.graph["root"])
pos3=af.tree_pos(b4c,g.graph["root"])
pos4=af.tree_pos(w4c,g.graph["root"])
pos5=af.tree_pos(b8c,g.graph["root"])
pos6=af.tree_pos(w8c,g.graph["root"])
pos7=af.tree_pos(b16c,g.graph["root"])
pos8=af.tree_pos(w16c,g.graph["root"])

pos1b=af.tree_pos(b2c_before,g.graph["root"])
pos2b=af.tree_pos(w2c_before,g.graph["root"])
pos3b=af.tree_pos(b4c_before,g.graph["root"])
pos4b=af.tree_pos(w4c_before,g.graph["root"])
pos5b=af.tree_pos(b8c_before,g.graph["root"])
pos6b=af.tree_pos(w8c_before,g.graph["root"])
pos7b=af.tree_pos(b16c_before,g.graph["root"])
pos8b=af.tree_pos(w16c_before,g.graph["root"])


plt.figure(figsize=(14,6))
# Arbol B2C
plt.subplot(1,2,1)
nx.draw_networkx(b2c, pos1, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5 )
plt.title(f"Grafo recortado")
plt.axis('off')

# Arbol W2C
plt.subplot(1,2,2)
nx.draw_networkx(b2c_before, pos1b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5 )
plt.title(f"Grafo orignal")
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
nx.draw_networkx(b2c_before, pos1b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B2C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,2)
nx.draw_networkx(b4c, pos3, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B4C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,6)
nx.draw_networkx(b4c_before, pos3b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B4C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,3)
nx.draw_networkx(b8c, pos5, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B8C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,7)
nx.draw_networkx(b8c_before, pos5b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B8C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,4)
nx.draw_networkx(b16c, pos7, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("B16C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,8)
nx.draw_networkx(b16c_before, pos7b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
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
nx.draw_networkx(w2c_before, pos2b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W2C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,2)
nx.draw_networkx(w4c, pos4, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W4C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,6)
nx.draw_networkx(w4c_before, pos4b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W4C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,3)
nx.draw_networkx(w8c, pos6, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W8C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,7)
nx.draw_networkx(w8c_before, pos6b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W8C antes")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,4)
nx.draw_networkx(w16c, pos8, with_labels=True, node_color='lightgreen', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W16C")
plt.axis('off')

# Arbol W2C
plt.subplot(2,4,8)
nx.draw_networkx(w16c_before, pos8b, with_labels=True, node_color='lightblue', edge_color='black',node_size=100,font_size=5,width=0.5)
plt.title("W16C antes")
plt.axis('off')

plt.show()

print("B2C :",lista_b2c)
print("W2C :",lista_w2c)
print("B4C :",lista_b4c)
print("W4C :",lista_w4c)
print("B8C :",lista_b8c)
print("W8C :",lista_w8c)
print("B16C:",lista_b16c)
print("W16C:",lista_w16c)
print("################################")
print("Interseccion 0.5   : ",lista_bw2c)
print("Interseccion 0.25  : ",lista_bw4c)
print("Interseccion 0.125 : ",lista_bw8c)
print("Interseccion 0.0625: ",lista_bw16c)
print("################################")
print("Union con raíz     : ",union_t)

with open("z_resultado_raiz.json", "w") as f:
    json.dump(union_t, f)
