from collections import deque
import networkx as nx
import pandas as pd
import numpy as np
import itertools

########### Algoritmos de ordenamiento ########################

def bfs(G,inicio):
    visitados=set()
    cola=deque([inicio])
    visitados.add(inicio)
    orden=[]

    while cola:
        nodo=cola.popleft()
        orden.append(nodo)
        for vecino in G.successors(nodo):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return orden


def dfs(G,inicio):
    visitados=set()
    pila=[inicio]
    visitados.add(inicio)
    orden=[]

    while pila:
        nodo=pila.pop()
        orden.append(nodo)
        for vecino in G.successors(nodo):
            if vecino not in visitados:
                visitados.add(vecino)
                pila.append(vecino)
    return orden

############## Algoritmos de Ordenamiento ####################3

def bubble_sort(lista,ascendente):
    lista=lista.copy()
    n=len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if(ascendente and lista[j]>lista[j+1]) or (not ascendente and lista[j]<lista[j+1]):
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

def selection_sort(lista,ascendente):
    lista=lista.copy()
    n=len(lista)
    for i in range(n):
        k = i
        menor=lista[i]
        for j in range(i+1,n):
            if (ascendente and lista[j]<menor) or (not ascendente and lista[j]>menor):
                menor=lista[j]
                k=j
        lista[k],lista[i]=lista[i],lista[k]
    return lista

def insertion_sort(lista,ascendente):
    lista=lista.copy()
    n=len(lista)
    for i in range(1, n):
        temp=lista[i]
        j=i-1
        while j>=0 and ((ascendente and temp<lista[j]) or (not ascendente and temp>lista[j])):
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=temp
    return lista

def shell_sort(lista,ascendente):
    lista=lista.copy()
    n=len(lista)
    salto=n//2

    while salto > 0:
        for i in range(salto, n):
            temp=lista[i]
            j=i
            while j>=salto and ((ascendente and temp<lista[j-salto]) or (not ascendente and temp>lista[j-salto])):
                lista[j]=lista[j-salto]
                j -= salto
            lista[j] = temp
        salto//=2
    return lista

def cycle_sort(lista,ascendente):
    lista=lista.copy()
    writes=0
    n=len(lista)

    for cycle_start in range(0,n-1):
        item=lista[cycle_start]
        pos=cycle_start

        for i in range(cycle_start+1,n):
            if (ascendente and lista[i]<item) or (not ascendente and lista[i]>item):
                pos+=1

        if pos==cycle_start:
            continue

        while pos<n and item==lista[pos]:
            pos+=1
        if pos<n:
            lista[pos],item=item,lista[pos]
            writes+=1

        while pos!=cycle_start:
            pos=cycle_start
            for i in range(cycle_start+1,n):
                if (ascendente and lista[i]<item) or (not ascendente and lista[i]>item):
                    pos+=1
            while pos<n and item==lista[pos]:
                pos+=1
            if pos<n:
                lista[pos], item = item, lista[pos]
                writes += 1
    return lista


def quick_sort(lista,ascendente):
    lista=lista.copy()

    def _quick_sort(left,right):
        i,j=left,right
        x=(lista[left]+lista[right])/2
        while i<=j:
            if ascendente:
                while lista[i]<x:
                    i+=1
                while lista[j]>x:
                    j-=1
            else:
                while lista[i]>x:
                    i+=1
                while lista[j]<x:
                    j-=1

            if i<=j:
                lista[i],lista[j]=lista[j],lista[i]
                i+=1
                j-=1

        if left<j:
            _quick_sort(left,j)
        if i<right:
            _quick_sort(i,right)

    _quick_sort(0,len(lista)-1)
    return lista


def merge_sort(lista,ascendente=True):
    lista=lista.copy()

    def merge(left,mid,right):
        L=lista[left:mid+1]
        R=lista[mid+1:right+1]

        i=j=0
        k=left

        while i<len(L) and j<len(R):
            if (ascendente and L[i]<=R[j]) or (not ascendente and L[i]>=R[j]):
                lista[k]=L[i]
                i+=1
            else:
                lista[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            lista[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            lista[k]=R[j]
            j+=1
            k+=1

    def _merge_sort(left,right):
        if left<right:
            mid=left+(right-left)//2
            _merge_sort(left,mid)
            _merge_sort(mid + 1,right)
            merge(left,mid,right)

    _merge_sort(0,len(lista)-1)
    return lista

def counting_sort(arr):
    if not arr:
        return []

    max_val=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max_val:
            max_val=arr[i]

    cnt_arr=[0]*(max_val+1)

    for val in arr:
        cnt_arr[val]+=1

    for i in range(1,len(cnt_arr)):
        cnt_arr[i]+=cnt_arr[i-1]

    aux=[0]*len(arr)

    for i in range(len(arr)-1,-1,-1):
        v=arr[i]
        aux[cnt_arr[v]-1]=v
        cnt_arr[v]-=1

    return aux

############### Matrices y grafos ########################

def matriz_correlacion(le_dataframe):
    df=pd.read_csv(le_dataframe)
    corr_matrix=df.corr(method='pearson')
    return corr_matrix

def matriz_adyacencia(corr_abs,th):
    adj_matrix=(corr_abs>=th).astype(int)
    np.fill_diagonal(adj_matrix.values,0)
    return adj_matrix

def grafo_correlacion(adj_m,dist_m):
    G=nx.from_pandas_adjacency(adj_m)
    isolated_nodes=list(nx.isolates(G))
    G.remove_nodes_from(isolated_nodes)

    for i in G.nodes:
        for j in G.nodes:
            if i!=j and G.has_edge(i,j):
                peso=dist_m.loc[i, j]
                G[i][j]['weight']=float(peso)
    return G

def gml_to_dist_matrix(gml_file,output_csv):
    # Cargar grafo desde archivo GML
    G=nx.read_gml(gml_file)

    # Obtener lista ordenada de nodos
    nodes=list(G.nodes())

    # Crear matriz vacía
    dist_matrix=pd.DataFrame(index=nodes, columns=nodes)

    # Rellenar con distancias (número de aristas)
    for i in nodes:
        # distancias desde i a todos los demás
        lengths=nx.single_source_shortest_path_length(G, i)
        
        for j in nodes:
            dist_matrix.loc[i, j] = lengths.get(j, float('inf'))

    # Guardar como CSV
    dist_matrix.to_csv(output_csv)

################## Enraizamiento ############################

def exportar_grafo_enraizado(G,root,filename):
    # Marcar la raíz como atributo del grafo
    G.graph['root']=root
    # Convertir valores NumPy a tipo nativo Python
    for _, attrs in G.nodes(data=True):
        for k, v in attrs.items():
            if isinstance(v,np.generic):
                attrs[k]=v.item()
    for _, _, attrs in G.edges(data=True):
        for k,v in attrs.items():
            if isinstance(v,np.generic):
                attrs[k]=v.item()

    # Exportar a GML
    nx.write_gml(G, filename)
    print(f"Grafo exportado correctamente como '{filename}' con raíz '{root}'.")

def exportar_grafo_no_enraizado(G,filename):
    # Convertir valores NumPy a tipo nativo Python
    for _, attrs in G.nodes(data=True):
        for k, v in attrs.items():
            if isinstance(v,np.generic):
                attrs[k]=v.item()
    for _, _, attrs in G.edges(data=True):
        for k, v in attrs.items():
            if isinstance(v, np.generic):
                attrs[k]=v.item()

    # Exportar a GML
    nx.write_gml(G,filename)
    print(f"Grafo exportado correctamente como '{filename}'.")


############### Analisis de arboles ######################

def unir_listas(lista1,lista2):
    nueva_lista=[]
    for elem in lista1:
        nueva_lista.append(elem)
    for elem in lista2:
        repetido=False
        for existente in nueva_lista:
            if elem==existente:
                repetido=True
                break

        if not repetido:
            nueva_lista.append(elem)
    return nueva_lista


# Analisis para arbol con raiz
def analizar_arbol_original(archivo_csv,raiz,threshold):
    df=pd.read_csv(archivo_csv)
    corr_matrix=df.corr(method='pearson')
    corr_abs=corr_matrix.abs()
    dist_matrix=1-corr_abs
    adj_matrix=(corr_abs>=0.6).astype(int)
    np.fill_diagonal(adj_matrix.values,0)

    G=nx.from_pandas_adjacency(adj_matrix)
    isolated_nodes=list(nx.isolates(G))
    G.remove_nodes_from(isolated_nodes)

    # Si la raiz no esta, conectarla con la variable mas correlacionada
    if 'y' not in G.nodes:
        corr_with_y=corr_abs['y'].drop('y').sort_values(ascending=False)
        G.add_node('y')
        for var,corr_value in corr_with_y.items():
            if var in G.nodes:
                G.add_edge('y',var,weight=1-corr_value)
                break

    # Asignar pesos de distancia
    for i in G.nodes:
        for j in G.nodes:
            if i!=j and G.has_edge(i,j):
                G[i][j]['weight']=dist_matrix.loc[i,j]

    MST=nx.minimum_spanning_tree(G,weight='weight',algorithm='kruskal')

    # Hasta aca tenemos el MST inicial, con la variable objetivo 'y' incluida en el

    # Agregamos el peso a cada arista
    new_MST=nx.bfs_tree(MST,source=raiz) # Analisis con BFS -------------------------------------------------------------
    for i in new_MST.nodes:
        for j in new_MST.nodes:
            if i!=j and new_MST.has_edge(i,j):
                new_MST[i][j]['weight']=dist_matrix.loc[i,j]

    niveles=nx.single_source_shortest_path_length(new_MST,source=raiz) # Diccionario que empareja el nodo con su distancia a la raiz
    nodos_a_mantener=[n for n, lvl in niveles.items() if lvl<=threshold] # Lista donde se almacenan el nombre de los nodos que cumplan la condicion (thres)
    pruned_tree=new_MST.subgraph(nodos_a_mantener).copy() # Asigna una copia del subgrafo con solo los nodos que pasan el threshold a una nueva variable


    pruned_tree=nx.bfs_tree(pruned_tree,source=raiz) # Convertimos en grafo en uno dirigido
    # Asignamos nuevamente los pesos
    for i in pruned_tree.nodes:
        for j in pruned_tree.nodes:
            if i!=j and pruned_tree.has_edge(i,j):
                pruned_tree[i][j]['weight']=dist_matrix.loc[i,j]

    return MST,pruned_tree

def analizar_arbol(archivo_gml,raiz,threshold):
    # Cargar el grafo desde el archivo .gml
    G=nx.read_gml(archivo_gml)
    # Asegurar que los nodos estén en formato string
    G=nx.relabel_nodes(G, lambda x: str(x))
    
    # Convertir a BFS-tree desde la raíz
    if raiz not in G.nodes:
        raise ValueError(f"La raíz '{raiz}' no está en el archivo GML.")

    original_tree=nx.bfs_tree(G,source=raiz)
    # Calcular niveles (distancias desde la raíz)
    niveles=nx.single_source_shortest_path_length(original_tree,source=raiz)
    # Lista de nodos dentro del threshold original
    nodos_a_mantener=[n for n,lvl in niveles.items() if lvl<=threshold]
    # Subgrafo podado 
    pruned_tree=original_tree.subgraph(nodos_a_mantener).copy()
    # Convertirlo de nuevo en árbol BFS dirigido
    pruned_tree=nx.bfs_tree(pruned_tree, source=raiz)
    # Retornar ambos arboles
    return original_tree, pruned_tree

################################3

def analizar_arbol2(archivo_csv, raiz,threshold,metodo="dfs"):
    df=pd.read_csv(archivo_csv)
    corr_matrix=df.corr(method='pearson')
    corr_abs=corr_matrix.abs()
    dist_matrix=1-corr_abs
    adj_matrix=(corr_abs>=0.6).astype(int)
    np.fill_diagonal(adj_matrix.values,0)

    G = nx.from_pandas_adjacency(adj_matrix)
    isolated_nodes = list(nx.isolates(G))
    G.remove_nodes_from(isolated_nodes)

    # Conectar raíz si no existe
    if raiz not in G.nodes:
        corr_with_root = corr_abs[raiz].drop(raiz).sort_values(ascending=False)
        G.add_node(raiz)
        for var, corr_value in corr_with_root.items():
            if var in G.nodes:
                G.add_edge(raiz, var, weight=1-corr_value)
                break

    # Asignar pesos a las aristas
    for u, v in G.edges():
        G[u][v]["weight"] = dist_matrix.loc[u, v]
    # MST inicial
    MST = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')
    # Convertir a árbol dirigido
    new_MST = nx.bfs_tree(MST, source=raiz)
    # Asignar pesos de distancia
    for u, v in new_MST.edges():
        new_MST[u][v]["weight"] = dist_matrix.loc[u, v]
    if metodo == "bfs":
        # Distancia REAL en niveles
        niveles = nx.single_source_shortest_path_length(new_MST, source=raiz)
    elif metodo == "dfs":
        # Distancia según profundidad DFS
        niveles = {}
        for depth, node in enumerate(nx.dfs_preorder_nodes(new_MST, source=raiz)):
            niveles[node] = depth
    else:
        raise ValueError("El método debe ser 'bfs' o 'dfs'.")

    # Filtrar nodos por umbral
    nodos_a_mantener = [n for n, nivel in niveles.items() if nivel <= threshold]

    # Subgrafo resultante
    pruned_tree = new_MST.subgraph(nodos_a_mantener).copy()

    # Convertir nuevamente a árbol dirigido (por si hubo cortes)
    pruned_tree = nx.bfs_tree(pruned_tree, source=raiz)

    # Reasignar pesos
    for u, v in pruned_tree.edges():
        pruned_tree[u][v]["weight"] = dist_matrix.loc[u, v]

    return MST, pruned_tree
##################################33

# Analisis de arbol sin raiz
def analizar_arbol_nr(archivo_csv):
    df=pd.read_csv(archivo_csv)
    corr_matrix=df.corr(method='pearson')
    corr_abs=corr_matrix.abs()
    dist_matrix=1-corr_abs
    adj_matrix=(corr_abs>=0.6).astype(int)
    np.fill_diagonal(adj_matrix.values,0)

    G=nx.from_pandas_adjacency(adj_matrix)
    isolated_nodes=list(nx.isolates(G))
    G.remove_nodes_from(isolated_nodes)

    # Forzar inclusión de 'y' si no está
    if 'y' not in G.nodes:
        corr_with_y=corr_abs['y'].drop('y').sort_values(ascending=False)
        G.add_node('y')
        for var,corr_value in corr_with_y.items():
            if var in G.nodes:
                G.add_edge('y',var,weight=1-corr_value)
                break

    # Asignar pesos
    for i in G.nodes:
        for j in G.nodes:
            if i!=j and G.has_edge(i,j):
                G[i][j]['weight']=dist_matrix.loc[i,j]

    MST=nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')

    all_pairs=dict(nx.all_pairs_shortest_path_length(MST))

    max_len=0
    node_u=node_v=None
    for u,dists in all_pairs.items():
        for v, dist in dists.items():
            if dist>max_len:
                max_len=dist
                node_u,node_v=u,v

    diam_path=nx.shortest_path(MST,source=node_u,target=node_v)
    num_edges=len(diam_path)-1

    if num_edges%2==0:
        middle_edge_idx=num_edges//2
    else:
        middle_edge_idx=(num_edges+1)//2

    node_a=diam_path[middle_edge_idx-1]
    node_b=diam_path[middle_edge_idx]
    G_cut=MST.copy()
    G_cut.remove_edge(node_a,node_b)

    components=list(nx.connected_components(G_cut))
    target='y'

    selected_component=[c for c in components if target in c][0]
    subtree=G_cut.subgraph(selected_component).copy()
    new_G=subtree.copy()  # subgrafo resultante
    return MST,new_G

def comparar_arboles(G1,G2,inicio='y'):
    # Crear las listas y conjuntos
    nodos_G1=list(G1.nodes())
    nodos_G2=list(G2.nodes())
    recorridos=[]
    diferentes=set()  # usar conjunto para evitar duplicados

    # Comenzar por el nodo inicial si existe en alguno de los grafos
    if inicio in nodos_G1 or inicio in nodos_G2:
        nodos_G1=[inicio]+[n for n in nodos_G1 if n!=inicio]
        nodos_G2=[inicio]+[n for n in nodos_G2 if n!=inicio]
    else:
        print(f"Nodo '{inicio}' no encontrado en ninguno de los grafos.")

    # Recorrer los nodos de G1
    for nodo in nodos_G1:
        if nodo not in recorridos:
            if nodo in nodos_G2:
                ady_G1=set(G1.neighbors(nodo))
                ady_G2=set(G2.neighbors(nodo))

                # Comparar adyacencias
                dif_ady=(ady_G1-ady_G2) | (ady_G2-ady_G1)

                # Agregar diferencias y marcarlas como recorridas
                for d in dif_ady:
                    diferentes.add(d)
                    if d not in recorridos:
                        recorridos.append(d)
            else:
                # Nodo no existe en G2
                diferentes.add(nodo)
                recorridos.append(nodo)

            # Marcar nodo como recorrido
            recorridos.append(nodo)

    # Repetir el proceso para los nodos de G2
    for nodo in nodos_G2:
        if nodo not in recorridos:
            if nodo in nodos_G1:
                ady_G1 = set(G1.neighbors(nodo))
                ady_G2 = set(G2.neighbors(nodo))
                dif_ady = (ady_G1 - ady_G2) | (ady_G2 - ady_G1)

                for d in dif_ady:
                    diferentes.add(d)
                    if d not in recorridos:
                        recorridos.append(d)
            else:
                diferentes.add(nodo)
                recorridos.append(nodo)

            recorridos.append(nodo)

    # Retornar lista de diferencias sin duplicados
    return list(diferentes)

def comparar_arboles_m(csv1,csv2): # funciona en algunos casos, en otros no (b2c)
    # Cargar matrices de distancias
    M1=pd.read_csv(csv1,index_col=0)
    M2=pd.read_csv(csv2,index_col=0)

    nodos1=set(M1.index)
    nodos2=set(M2.index)
    nodos_dif=set()

    # Nodos que faltan en alguna matriz
    nodos_dif.update(nodos1-nodos2)
    nodos_dif.update(nodos2-nodos1)

    # Nodos comunes, pero con distancias diferentes
    nodos_comunes=nodos1 & nodos2

    for i in nodos_comunes:
        for j in nodos_comunes:
            if i == j: 
                continue
            d1=M1.loc[i,j]
            d2=M2.loc[i,j]

            # Si difiere la distancia, ambos nodos se marcan como diferentes
            if d1 != d2:
                nodos_dif.add(i)
                nodos_dif.add(j)

    # Convertir a lista ordenada antes de retornar
    return list(nodos_dif)

# Version matriz (v1.0)
def comparar_arboles_m2(csv1,csv2):
    # Cargar matrices
    M1=pd.read_csv(csv1,index_col=0)
    M2=pd.read_csv(csv2,index_col=0)
    
    nodos1=list(M1.index)
    nodos2=list(M2.index)

    # Diferencias
    nodos_dif=set()

    # Nodos que existen en un dataframe pero no en el otro
    nodos_dif.update(set(nodos1)-set(nodos2))
    nodos_dif.update(set(nodos2)-set(nodos1))

    # Nodos comunes
    nodos_comunes=sorted(list(set(nodos1) & set(nodos2)))

    # Comparar distancia entre pares sin repetir
    for idx_i in range(len(nodos_comunes)):
        i = nodos_comunes[idx_i]
        for idx_j in range(idx_i+1,len(nodos_comunes)):
            j=nodos_comunes[idx_j]

            d1=M1.loc[i,j]
            d2=M2.loc[i,j]

            if d1!=d2:
                nodos_dif.add(j)   # Se agrega el nodo que difiere según tu regla

    return list(nodos_dif)

########################## Graficar Grafo ####################################

def radial_tree(G, root):
    levels=nx.single_source_shortest_path_length(G, root)

    max_lvl=max(levels.values())
    level_nodes = {lvl: [] for lvl in range(max_lvl + 1)}

    for node, lvl in levels.items():
        level_nodes[lvl].append(node)

    pos = {}
    for lvl, nodes in level_nodes.items():
        r = lvl * 2  # radio del anillo
        n = len(nodes)
        for i, node in enumerate(nodes):
            angle = 2 * np.pi * i / n
            pos[node] = (r * np.cos(angle), r * np.sin(angle))

    return pos

def tree_pos(G, root=None):
    import networkx as nx

    # Detectar componentes del grafo
    if isinstance(G, nx.DiGraph):
        components = list(nx.weakly_connected_components(G))
    else:
        components = list(nx.connected_components(G))

    pos = {}
    offset = 0  # para separar cada componente horizontalmente

    # Procesar cada componente como un árbol independiente
    for comp in components:
        subg = G.subgraph(comp)

        # Si la raíz está en este componente, usarla;
        # si no, elegir una raíz cualquiera del componente.
        if root in subg.nodes:
            comp_root = root
        else:
            comp_root = list(comp)[0]  # un nodo arbitrario

        # Layout para este componente
        comp_pos = pos_f(subg, comp_root)

        # Ajustar posiciones con offset para que no se superpongan
        for n, (x, y) in comp_pos.items():
            pos[n] = (x + offset, y)

        offset += 2  # separar componentes horizontalmente

    return pos


def pos_f(G,root,width=1.,vert_gap=0.2,vert_loc=0,xcenter=0.5,pos=None,parent=None):
    if pos is None:
        pos={root: (xcenter,vert_loc)}
    else:
        pos[root]=(xcenter,vert_loc)

    neighbors=list(G.neighbors(root))

    if parent is not None and parent in neighbors:
        neighbors.remove(parent)

    if len(neighbors)!=0:
        dx=width/len(neighbors)
        nextx=xcenter-width/2-dx/2

        for neighbor in neighbors:
            nextx+=dx
            pos=pos_f(
                G,neighbor,width=dx,vert_gap=vert_gap,
                vert_loc=vert_loc-vert_gap,xcenter=nextx,
                pos=pos,parent=root
            )
    return pos


# Algoritmo Newman para detectar comunidades (v1.0)
def links_between(A,B,G):
    l=0
    for u,v in G.edges():
        if (u in A and v in B) or (u in B and v in A):
            l+=1
    return l

def degree_sum(community,G):
    return sum(G.degree(n) for n in community)

def modularity(communities,G,m):
    Q=0.0
    for c in communities:
        l_c=0
        for u,v in G.edges():
            if u in c and v in c:
                l_c+=1
        d_c=degree_sum(c,G)
        Q+=(l_c/m)-(d_c/(2*m))**2 # Formulita
    return Q

def newman(G):
    m=G.number_of_edges()
    if m==0:
        print("El grafo no tiene aristas.")
        return

    # Comunidades iniciales
    communities=[{node} for node in G.nodes()]

    # Algoritmo newman
    improved=True

    while improved and len(communities)>1:
        improved=False
        best_delta_Q=0
        best_pair=None

        # Probar todas las fusiones posibles
        for i,j in itertools.combinations(range(len(communities)),2):
            A=communities[i]
            B=communities[j]
            l_AB=links_between(A,B,G)
            if l_AB==0:
                continue 
            dA=degree_sum(A,G)
            dB=degree_sum(B,G)

            delta_Q=(l_AB/m)-((dA*dB)/(2*m*m)) # formulita

            if delta_Q>best_delta_Q:
                best_delta_Q=delta_Q
                best_pair=(i,j)

        # Fusionar si mejora la modularidad
        if best_pair is not None:
            i,j=best_pair
            communities[i]=communities[i] | communities[j]
            del communities[j]
            improved=True

    # Resultados
    Q_final=modularity(communities,G,m)
    print("Comunidades detectadas:\n")
    for idx,community in enumerate(communities,1):
        print(f"Comunidad {idx}: {sorted(community)}")
    print(f"\nModularidad final Q = {Q_final:.4f}")