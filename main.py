
#IMPORTAMOS DE LA GUI LOS ARCHIVOS A NECESITAR
from gui import graficarDijkstra, graficarIDDFS

#IMPORTAMOS LAS FUNCIONES A USAR DEL ARCHIVO COD
from cod import G, imprimirGrafoNormal, algoritmoDijkstra, IDDFS


#funcion del main
def main():
    '''
    ***************************************************************************************************
    FUNCION PRINCIPAL (MAIN)
    ***************************************************************************************************
    '''
    while True:
   
        print("MENU DE OPCIONES\n")
        print("1. MOSTRAR GRAFO")
        print("2. MOSTRAR DIJSKTRA")
        print("3. MOSTRAR BUSQUEDA PROFUNIDAD ITERADA LIMITADA")
        print("4. FIN\n")
        
        opcion = (input("Seleccione su opcion: ")) #variable de selección de opciones
         
        if opcion == "1":
            print("Cargando ... ")
            imprimirGrafoNormal() #imprimimos el grafo normal
        

        if opcion == "2":
            #debemos evaluar si los datos ingresado por el usuario estan dentro del grafo-archivo
            #evaluar el nodo inicial y el nodo final

            inicio = int(input("INGRESE SU AEROPUERTO DE INICIO: "))
            destino = int(input("INGRESE SU AEROPUERTO DE DESTINO: "))

            if inicio in G and destino in G:  #verificamos que el inicio y el destino esten en el grafo G
                resultado = algoritmoDijkstra(G, inicio, destino) #resultado almacena el algoritmo de dijkstra
                
                if resultado is not None: #si el resultado si tiene ALGO que mostrar
                    costo_minimo, camino = resultado #separamos los elementos de costo minimo y el camino encontrado

                    print(f"\nCamino: {camino}") #imprimimos el camino encontrado :v
                    print(f"\nCosto Minimo: {costo_minimo}")
                    print("Cargando ... ")
                    graficarDijkstra(G, camino)

                else: #si el resultado es vacio (no hay nada ... :c)
                    print("Lo siento papu, no podras salir de tu choza")

        if opcion == "3":
            inicio = int(input("INGRESE SU AEROPUERTO DE INICIO: "))
            destino = int(input("INGRESE SU AEROPUERTO DE DESTINO: "))
            escalas = int(input("INGRESE EL LIMITE DE ESCALAS: "))
            if inicio in G and destino in G:  #verificamos que el inicio y el destino esten en el grafo G
                resultado = IDDFS(G, inicio, destino, escalas) #resultado almacena el algoritmo IDDFS para las escalas

                if resultado is not None: #si el resultado si tiene ALGO que mostrar
                    print("cargando ...")
                    graficarIDDFS(resultado)
            
                else:
                    print("No se encontraron resultados")

        if opcion == "4":
            print("Gracias :v\n")
            print("¡NO REGRESES!!!!!")
            break



#usamos esta condicional para que la funcion main sea la funcion principal, referencia a c++ :v
#me apoye de la IA XD
if __name__ == "__main__":
    main()