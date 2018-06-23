def chequear_minimo(nodo, vecino, grafo, pesos, predecesor):    
    if pesos[nodo] + grafo[nodo][vecino] < pesos[vecino]:
        pesos[vecino]  = pesos[nodo] + grafo[nodo][vecino]
        predecesor[vecino] = nodo
       

def Bellman(grafo, origen):
    pesos, predecesor = inicializar(grafo, origen)
    for i in range(len(grafo)-1): # Para el resto de los nodos
       
        for nodo in grafo: # Para cada nodo del grafo
            for vecino in grafo[nodo]: #Para cada vecino de un nodo
                chequear_minimo(nodo, vecino, grafo, pesos, predecesor) #Chequear distancia
            
    
    return pesos, predecesor


def inicializar(grafo, origen):
    pesos = {}
    predecesor = {}
    for nodo in grafo:
        predecesor[nodo]= ''
        pesos[nodo] = float('Inf')# Pesos inciales Infinitos
       
    pesos[origen] = 0 # Peso del "origen" cero
    return pesos, predecesor


def main():
    grafo = {
        'a': {'b': -2, 'c':  5},
        'b': {'c':  2, 'd':  3, 'e':  1},
        'c': {'e':2},
        'd': {'b':  1, 'c':  2},
        'e': {'d': -2}
        }
    nodo_inicial='a'
    print "Nodo incial", nodo_inicial
    pesos, predecesores = Bellman(grafo, nodo_inicial)
    informe(pesos,predecesores,grafo,nodo_inicial)

def informe(pesos,predecesores,grafo,nodo_inicial):

    print "-------------------------------------------"
    print "Caminos minimos desde el nodo:", nodo_inicial
    for nodo in predecesores:
        for vecino in predecesores[nodo]:
            print "Nodo Destino: ", nodo, "Anterior:", vecino, "Costo Camino Minimo:", pesos[nodo]


            
                

main();
