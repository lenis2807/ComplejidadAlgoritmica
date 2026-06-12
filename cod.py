# ============================================================  
# SECCIÓN 1: IMPORTACIONES  # Esta parte carga módulos de Python necesarios para el desarrollo del código
# ============================================================  
import os
import heapq 
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt 


'''
***************************************************************************************************
'''
# ============================================================  
# SECCIÓN 2: VARIABLES GLOBALES #configuración de variables necesarias para el programa
# ============================================================  

#ruta para leer el archivo de kagglehub
#ruta = kagglehub.dataset_download("adriana14852/airports-distances-and-others")

ruta = "complete_airport_flight_network_dataset.csv"
df = pd.read_csv(ruta) #leemos el archivo con la libreria Pandas 

G = nx.Graph() #leemos el grafo con el nx

#importamos a la variable G (grafo) los elementos a usar del archivo csv con pandas
G = nx.from_pandas_edgelist(df, source="origin_airport_id", target="destination_airport_id", edge_attr="distance_km")
'''
***************************************************************************************************
'''


# ============================================================  
# SECCIÓN 3: Impresión de grafo normal #Se imprime el grafo a evaluar
# ============================================================  

def imprimirGrafoNormal(): #funcion para imprimir el grafo
    '''
    ***************************************************************************************************
    IMPRIMIREMOS EL GRAFO NORMAL
    ***************************************************************************************************
    '''
    
    G = nx.Graph() #leemos el grafo con el nx

    #importamos a la variable G (grafo) los elementos a usar del archivo csv con pandas
    G = nx.from_pandas_edgelist(df, source="origin_airport_id", target="destination_airport_id", edge_attr="distance_km")

    plt.figure(figsize=(15,10)) #colocamos el tamaño de nuestra pantalla
    pos = nx.spring_layout(G, k=0.5, seed=42) #configuramos el spring 

    #graficamos los nodos
    nx.draw_networkx_nodes(G, pos, node_size=20, node_color="skyblue")

    #graficamos las aristas
    nx.draw_networkx_edges(G, pos, alpha=0.8, width=0.5, edge_color="gray")

    #graficamos las etiquetas (labels)
    nx.draw_networkx_labels(G, pos, font_size=5, font_family="sans-serif")


    plt.title("Grafico rutas aereas", fontsize=16) #titulo del grafo 
    plt.axis("off") #dejamos unicamente los datos visibles
    plt.tight_layout() #para los margenes
    plt.show() #mostramos el grafo




# ============================================================  
# SECCIÓN 4: DESARROLLO DE ALGORITMOS A USAR  #En está parte desarrollamos y justificamos el desarrollo de los algoritmos a usar
# ============================================================  
def algoritmoDijkstra(grafo, inicio, destino): 
    '''
    ***************************************************************************************************
    JUSTIFICACION: EL ALGORITMO DE DIJKSTRA NOS PERMITIRA ENCONTRAR EL MEJOR CAMINO ENTRE DOS NODOS
    CONSIDERANDO EL PESO DE LAS ARISTAS COMO LAS DISTANCIAS MEDIDAS EN KILOMETROS

    SI NO SE ENCUENTRA EL CAMINO, DEVOLVERA NONE (NULL)
    ESTAMOS USANDO LA LIBRERIA HEAP PARA LA EVALUACION DE LOS NODOS
    ***************************************************************************************************
    '''
    cola = [] #creamos una cola para evaluar los nodos 

    heapq.heappush(cola, (0, inicio, [inicio])) #hacemos un heappush para evaluar
    #los elementos de la cola a su vez que agregamos el costo y mostraremos el camino

    costo_g = {n : float('inf') for n in grafo} #inicializamos los costos en infinito
    costo_g[inicio] = 0 #colocamos el nodo inicio en 0

    #hacemos una validacion que si el nodo ingresado es igual al del final
    #no retorne nada 
    if inicio == destino: 
        print("Seas pendejo pues :v") #retornamos 
        return 0, [inicio] #devolvemos el costo 0 y el "camino" xd

    #haremos un while "recursivo"
    while cola: #mientras la cola no este vacia
        costo_acumulado, nodo, camino = heapq.heappop(cola)
        #sacamos del heapq.heappush(cola, (0, inicio, [inicio]))
        #donde: costo_Acumulado = 0
        #       nodo = inicio
        #       camino = [inicio]

        if nodo == destino: #si el nodo inicial es igual al nodo del destino
            #retornamos el costo_Acumulado y el camino
            return costo_acumulado, camino 

        if costo_acumulado > costo_g[nodo]: #si el costo_Acumulado actual es mayor al costo del diccionario en la pos nodo
            continue #saltamos porque no vale la pena cambiar el costo, bruh

        #para cada vecino y su costo de aristas evaluado en el grafo de pos nodo
        for vecinos, datos_arista in grafo[nodo].items(): 

            #sumamos a la variable de costo actual el costo acumulado mas el costo de aristas
            #de cada vecino
            costo_aristas = datos_arista['distance_km']
            costo_Actual = costo_acumulado + costo_aristas 


            #hacemos la condicion de evaluar la cantidad del costo actual contra la de los costos en g
            if costo_Actual < costo_g[vecinos]:
                costo_g[vecinos] = costo_Actual #hacemos un swap de costos

                #hacemos un heappush para cada vecino que cumpla la condicion
                #además que en cada push mostramos el camino con el nodo de menor
                #peso encontrado
                heapq.heappush(cola, (costo_Actual, vecinos, camino + [vecinos]))

    return None #si no encontramos camino retornamos None (Null)

def dls(grafo, inicio, destino, limite): #creamos una funcion dls para iterar los nodos
    '''
    ***************************************************************************************************
    ESTA SERÁ NUESTRA FUNCIÓN PARA ENCONTRAR Y VERIFICAR EL CAMINO ENCONTRADO
    CON PARAMETROS COMO:
    INICIO = INGRESADO POR EL USUARIO
    DESTINO = INGRESADO POR EL USUARIO
    LIMITE = ESCALA, EL USUARIO INGRESARA LA ESCALA CORRESPONDIENTE A SU GUSTO

    SI EL DLS NO ENCUENTRA UN CAMINO CORRESPONDIENTE EN EL NIVEL ACTUAL 
    DEVOLVERA UN NONE

    SI LO ENCUENTRA DEVOLVERA EL RESULTADO FINAL

    LA VARIABLE DE VISITADOS ESTA CREADA BAJO UN SET PARA MEJORAR LA EFICIENCIA DEL ALGORITMO
    COMPLEJIDAD TEMPORAL
    ***************************************************************************************************
    '''

    visitados = set() #creamos un set de visitados para la eficiencia temporal

    def dls(nodo, camino, limite): #funcion recursiva dls
        #donde nodo es igual al nodo actual a evaluar
        #el limite es el limite pues :v
    
        if nodo == destino: #si el nodo actual es igual al destino
            return camino #retornamos el camino 

        if limite == 0: #si llegamos al 0
            return None #retornamos None
                     
        visitados.add(nodo) #agregamos al set visitados el nodo actual a evaluar

        #si el limite es mayor a 0 
        if limite > 0 : 
            for vecinos, _ in grafo[nodo].items(): #para cada vecino del grafo en pos nodo
                #hacemos "_" para que no haya problema al buscar elementos en la tupla de cosas (se puede modificar ese caracter)
                #ejemplo:  [ ... , (1234, {'distance_km': 500} ) , ... ]
                #vecinos = 1234       and            _ = {'distance_km':500}

                if vecinos not in visitados: #si el vecino no esta en el arreglo de visitados
                    
                    #agregamos una variable resultado que llama a la funcion recursivamente dls
                    #en cada iteracion del bucle for
                    resultado = dls(vecinos, camino + [vecinos], limite-1)

                    #si el resultado no esta vacio (contiene elementos)                    
                    if resultado is not None:
                        return resultado #retorna el resultado y mostrara el camino
            
            visitados.remove(nodo) #fuera del bucle for pero dentro de la condicional, removemos el nodo actual
            #para que en la siguiente iteración del bucle for, el nodo actual no aparezca como visitado
            
            return None #si no hay camino retorna None


    resultado_final = dls(inicio, [inicio], limite) #llamamos a la funcion dls
    
    #nos mostrara el camino y el limite encontrado
    return resultado_final #retornamos el resultado final

                

#funcion BUSQUEDA EN PROFUNDIDAD LIIMITADA ITERATIVA
#esta funcion nos servira para la busqueda de escalas
def IDDFS(grafo, inicio, destino, limite): 
    '''
    ********************************************************************************************************
    JUSTIFICACION: USAREMOS EL ALGORITMO DE BUSQUEDA EN PROFUNDIDAD LIMITADA ITERATIVA, PUESTO 
    QUE DLS (BUSQUEDA EN PROFUNDIDAD LIMITADA) NOS SERÁ DE VITAL IMPORTANCIA PARA ENCONTRAR EL CAMINO 
    CORRESPONDIENTE, SI NO SE ENCUENTRA EN EL NIVEL ACTUAL EL IDDFS PASARA A EVALUAR EL SIGUIENTE NIVEL

    CON ESTO EVITAREMOS ENCONTRAR UN CAMINO NO EFICIENTE

    SI SE USARA EL ALGORITMO DE DFS (BUSQUEDA EN PROFUNDIDAD) PODEMOS LLEGAR A ENCONTRAR CAMINOS DE 50 PASOS
    LO CUAL NO ES MUY EFICIENTE
    ********************************************************************************************************
    '''

    #iteraremos hasta el rango del limite ingresado por el usuario
    #incrementaremos en + 1 para evaluar los limites exactos

    #si fuera limite = 5, el compilador lo va a leer hasta el rango 4
    #incrementar en +1 nos garantizara evaluar las escalas deseadas por el usuario
    for nivel_Actual in range(limite + 1): 

        #la variable camino devolvera la funcion dls

        #la variable nivel_Actual es la que iterara el dls
        camino = dls(grafo, inicio, destino, nivel_Actual) 
        
        #si el camino no esta vacio (tiene un resultado)
        if camino is not None:
            return camino #retornamos el camino

    return None #si no hemos encontrado nada retornamos None (Null)



