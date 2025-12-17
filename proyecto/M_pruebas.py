import Aux_fun as af
import networkx as nx

#bw2c_2=af.comparar_arboles_m2("a1.csv","a2.csv")
#
#print(bw2c_2)


grafo=nx.read_gml("z_prueba_newman.gml")
af.newman(grafo)