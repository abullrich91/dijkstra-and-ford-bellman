class Dijkstra(object):
    def __init__(self, grafo):
        self.posibles_lista = []
        self.recorridos_lista = []
        self.anterior = []
        self.grafo = grafo
        self.nodo_actual = None
        self.distancia = 0	
        self.paso = 0
        self.unico = True

    def camino_minimo(self, nodo_inicio, nodo_fin):
        self.nodo_actual = {nodo_inicio: self.distancia}
        self.posibles_lista.append(self.nodo_actual)
        self.anterior.append({nodo_inicio: nodo_inicio})

        while list(self.nodo_actual.keys())[0] != nodo_fin:
            self.recorridos_lista.append(list(self.nodo_actual.keys())[0])
            self.posibles_lista.pop(self.posibles_lista.index(self.nodo_actual))
            for nodo in self.grafo:
                if nodo['Nodo'] in list(self.nodo_actual.keys()):
                    for elemento in nodo:
                        if elemento != 'Nodo':
                            if elemento not in self.recorridos_lista:
                                if any(elemento in d for d in
                                       self.posibles_lista):
                                    for posible_proximo in self.posibles_lista:
                                        if list(posible_proximo.keys())[0] == elemento:
                                            if nodo.get(elemento) + self.distancia < list(posible_proximo.values())[0]:
                                                posible_proximo	[list(posible_proximo.keys())[0]] = nodo.get(elemento) + self.distancia
                                                for p in self.anterior:
                                                    if list(p.keys())[0] == elemento:
                                                        p[list(posible_proximo.keys())[0]] = list(self.nodo_actual.keys())[0]
                                else:
                                    self.posibles_lista.append({elemento: nodo.get(elemento) + self.distancia})
                                    self.anterior.append({elemento: list(self.nodo_actual.keys())[0]})

            values = []
            for elemento in self.posibles_lista:
                for nodo in elemento:
                    values.append(elemento.get(nodo))
            self.nodo_actual = self.posibles_lista[(values.index(min(values)))]
            self.distancia = list(self.nodo_actual.values())[0]
            self.informe()

        a = nodo_fin
        string = str(nodo_fin)
        while a != nodo_inicio:
            for elemento in self.anterior:
                for nodo in elemento:
                    if  nodo == a:
                        a = elemento.get(nodo)
                        string = str(a) + " -> " + string
        print("\n El camino minimo entre " + str(nodo_inicio) + " y " + str(nodo_fin) + " es:  " + string)

    def informe(self):
            if self.unico:
                self.unico = False
                print("Paso | Nodo | Distancia")
            nodo = list(self.nodo_actual.keys())[0]
            value = list(self.nodo_actual.values())[0]
            print("%4d" % self.paso + " | %4s" % nodo + " | %8s" % value + " | Posibles: " + str(
                self.posibles_lista) + " | Recorridos: " + str(self.recorridos_lista))
            self.paso += 1

grafo = []
A = {'Nodo': 'A', 'C': 5, 'F': 7, 'J': 12}
B = {'Nodo': 'B', 'E': 2, 'G': 1, 'H': 4}
C = {'Nodo': 'C', 'A': 5, 'D': 3}
D = {'Nodo': 'D', 'F': 6, 'E': 0, 'C': 3}
E = {'Nodo': 'E', 'D': 0, 'B': 2, 'G': 5}
F = {'Nodo': 'F', 'A': 7, 'D': 6, 'J': 0, 'H': 7}
G = {'Nodo': 'G', 'B': 1, 'E': 5}
H = {'Nodo': 'H', 'B': 4, 'F': 7, 'J': 2, 'I': 1}
I = {'Nodo': 'I', 'H': 1, 'J': 8}
J = {'Nodo': 'J', 'A': 12, 'F': 0, 'H': 2, 'I': 8}



grafo.append(A)
grafo.append(B)
grafo.append(C)
grafo.append(D)
grafo.append(E)
grafo.append(F)
grafo.append(G)
grafo.append(H)
grafo.append(I)
grafo.append(J)

Dijkstra = Dijkstra(grafo)
Dijkstra.camino_minimo('A', 'B')
    
