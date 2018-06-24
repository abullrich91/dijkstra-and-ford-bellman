def calcularcaminos(recorridos_inicio_a_nodo,distancias,nodo_inicio):
            print "RECORRIDOS MINIMOS DESDE: ", nodo_inicio, "AL RESTO DE LOS NODOS"
            print "-----------------------------------------------------------------------"
            for nodo in recorridos_inicio_a_nodo.items():
                if nodo[0]==nodo_inicio or nodo[1]==nodo_inicio:
                    if nodo[0]<>nodo[1]:
                        print "Desde: ",nodo_inicio,"Hasta", nodo[0], "|    Distancia: ",distancias[nodo[0]]
                        print "-----------------------------------------------------------------------"
            
                else:
                    #busco el recorrido
                    Recorrido=nodo[1]+nodo[0]
                    nodo_actual=nodo[1]
                    while recorridos_inicio_a_nodo[nodo_actual]<>nodo_inicio:
                        if recorridos_inicio_a_nodo[nodo_actual]<>nodo_inicio:
                            nodo_actual=recorridos_inicio_a_nodo[nodo_actual]
                            Recorrido=nodo_actual+Recorrido
                            
                    Recorrido=Recorrido
                    print "Desde: ",nodo_inicio,"Hasta", nodo[0],"|    Distancia: ",distancias[nodo[0]]
                    print "Recorrido", nodo_inicio+Recorrido
                    print "-----------------------------------------------------------------------"
            
                        
def dijkstra(aristas,nodos,nodo_inicio):
    distancia={}
    visitados={}
    recorridos_inicio_a_nodo={}
    # INICIALIZO EL DISCCIONARIO DE DISTANCIAS Y VISITADOS EN FALSE PARA TODOS
    
    for nodo in nodos:
    
       distancia.update({nodo: float('Inf')})
       visitados.update({nodo: 'FALSE'})
       recorridos_inicio_a_nodo.update({nodo: nodo_inicio})
    print "Distancias iniciales", distancia
    print "Vector visitados inciales", visitados
    print "Aristas,",aristas
    print "NODO INCIAL:", nodo_inicio


    for arista in aristas:
        if arista[0]==nodo_inicio:
            distancia.update({arista[1]: arista[2]})



    # PONGO EN CERO LA DISTANCIA DEL NODO ORIGEN Y LO MARCO COMO VISITADO
    distancia.update({nodo_inicio: 0})
    visitados.update({nodo_inicio: 'TRUE'})
    
    #AHORA ME FIJO LOS QUE FALTAN VISITAR Y LOS PONGO EN UN DICCIONARIO AUXILIAR PARA RECORRERLOS
    no_visitados={}
    for nodo, estado in visitados.items():
        if estado=='FALSE':
            no_visitados.update({nodo:distancia[nodo]})

    while len(no_visitados)>0:
            
            visitados.update({min(no_visitados.items(), key=lambda x: x[1])[0]: 'TRUE'})
            for arista in aristas:
                if arista[0]==min(no_visitados.items(), key=lambda x: x[1])[0]:
                    if distancia[arista[1]]>distancia[min(no_visitados.items(), key=lambda x: x[1])[0]]+arista[2]:
                        distancia[arista[1]]=distancia[min(no_visitados.items(), key=lambda x: x[1])[0]]+arista[2]
                        recorridos_inicio_a_nodo[arista[1]] = arista[0]
                        no_visitados.update({arista[1]:distancia[arista[1]]})            

            del no_visitados[min(no_visitados.items(), key=lambda x: x[1])[0]]
            
    print "-------------"
    print "DISTANCIAS", distancia
                        
    calcularcaminos(recorridos_inicio_a_nodo,distancia,nodo_inicio);
    

grafo = []

aristas = [("A","C",5),("A","F",7),("A","J",12),
           ("B","E",2),("B","G",1),("B","H",4),
           ("C","A",5),("C","D",3),
           ("D","F",6),("D","E",0),("D","C",3),
           ("E","D",0),("E","B",2),("E","G",5),
           ("F","A",7),("F","D",6),("F","J",0),("F","H",7),
           ("G","B",1),("G","E",5),
           ("H","B",4),("H","F",7),("H","J",2),("H","I",1),
           ("I","H",1),("I","J",8),
           ("J","A",12),("J","F",0),("J","H",2),("J","I",8)]
nodos="ABCDEFGHIJ"


dijkstra(aristas,nodos,"A")
