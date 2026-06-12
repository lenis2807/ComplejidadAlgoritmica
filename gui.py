import networkx as nx
import matplotlib.pyplot as plt 


# ============================================================  
# SECCIÓN 5: GRAFICOS RESULTANTES #funciones que muestran el gráfico resultante 
# ============================================================  
def graficarDijkstra(grafo, camino): #creamos una funcion para graficar el algoritmo de dijkstra
 
    plt.figure(figsize=(15,10)) #colocamos el tamaño de nuestra pantalla
    pos = nx.spring_layout(grafo, k=0.5, seed=42) #configuramos el spring 

    colores = [] #arreglo de colores
    for nodo in grafo.nodes(): #para cada nodo en el grafo
        if nodo not in camino: #si el nodo no esta en el camino 
            colores.append("red") #agregamos al arreglo colores el color rojo
        else: #sí, si esta en el camino
            colores.append("skyblue") #agregamos al arreglo colores el color celeste 

    #use IA
    aristas_del_camino = list(zip(camino[:-1], camino[1:]))

    #graficamos los nodos
    nx.draw_networkx_nodes(grafo, pos, node_size=20, node_color="skyblue")

    #graficamos las aristas
    nx.draw_networkx_edges(grafo, pos, alpha=0.8, width=0.5, edge_color="gray")

    #remarcamos el camino encontrado con rojo
    nx.draw_networkx_edges(grafo, pos, edgelist=aristas_del_camino, edge_color="red", width=3.0)

    #graficamos las etiquetas (labels)
    nx.draw_networkx_labels(grafo, pos, font_size=5, font_family="sans-serif")

    plt.title("Algoritmo de Dijkstra", fontsize=16) #titulo del grafo 
    plt.axis("off") #dejamos unicamente los datos visibles
    plt.tight_layout() #para los margenes
    plt.show() #mostramos el grafo
 
 
def graficarIDDFS(camino):
    G_camino = nx.DiGraph()

    edges = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]
    G_camino.add_edges_from(edges)
 
    plt.figure(figsize=(10,6))
    pos = nx.spring_layout(G_camino, seed=42)
    nx.draw_networkx_nodes(G_camino, pos, node_color='tomato', node_size=700)
    nx.draw_networkx_edges(G_camino, pos, edge_color='gray', width=2, arrowsize=20)
    nx.draw_networkx_labels(G_camino, pos, font_size=12, font_family='sans-serif', font_weight='bold')
    
    plt.title("Ruta Óptima Encontrada por IDDFS", fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.show()

