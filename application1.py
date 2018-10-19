import numpy as np
from collections import deque
from sortedcontainers import SortedSet

class Graph:
    #Incializa a Classe Graph
    #param: @directedGraph:
    #value: True = direcionado
    #       False = naoDirecionado
    def __init__(self, directedGraph=False):
        self.__V = list()
        self.__directedGraph = directedGraph
        self.__time = 0
        return
    
    #AdicionaAresta -> chamada pelo método createVertex()
    #param: @v = vértice, @index = indice do vértice
    def addVertex(self, v, index):
        if (not (v in self.__V)):
            v.setIndex(index)
            self.__V.append(v)
        return v

    #Cria vértice -> chama função addVertex() 
    def createVertex(self, index):
        return self.addVertex(Vertex(self), index)

    #Adiciona aresta
    def addEdge(self, u, v):
        #Verifica se os parâmetros passados são Vértices ou Int
        #Caso sejam int, é chamada novamente a função passando o objeto salvo na posição da lista __V do Graph
        if (isinstance(u, Vertex) and isinstance(v, Vertex)):
            #Verifica se os vértices estão incluídos na lista __V o Graph
            if ((u in self.__V) and (v in self.__V)):
                #Adiciona "v" na lista de adjacência de "u"
                u.addAdjacentVertex(v)

                #Se o grafo não for direcionado, faz o mesmo passo só que "v" para "u"
                if (not self.__directedGraph):
                    v.addAdjacentVertex(u)

                return
            #Se u e v não estiverem na lista __V do Graph, retorna erro
            else:
                raise("Erro método 'addEdge'. u e v não pertence ao grafo.")
        elif (isinstance(u, int) and isinstance(v, int)):
            self.addEdge(self[u-1], self[v-1])
        else:
            raise("Erro método 'addEdge'. u e v não são do tipo Vertex ou Int.")
        return
    
    #Busca vértice na posição k pertence a lista __V de Graph
    def __getitem__(self, k):
        if ((len(self.__V) > 0) and (k >= 0) and (k < len(self.__V))):
            return self.__V[k]
        return None

    def __len__(self):
        return len(self.__V)
    
    #Imprimir o objeto
    #print(Graph)
    def __str__(self):
        graphStr = str("")
        for index, vertex in enumerate(self.__V):
            graphStr += str(vertex)
            if (index < len(self.__V) - 1):
                graphStr += "\n"
        return graphStr
    
    def setVertexListAsUnexplored(self):
        for v in self.__V:
            v.setAsUnexplored()
        return
    #####################################################################
    #####################################################################
    #Busca em Profundidade
    def DFS_Rec(self, exploreObj=None):
        self.setVertexListAsUnexplored()

        self.__time = 0

        for vertex in self.__V:
            if (not vertex.wasExplored()):
                self.__DFS_VISIT_REC(vertex, exploreObj)

        return exploreObj

    def __DFS_VISIT_REC(self, vertex, exploreObj=None):

        self.__time += 1
        vertex.d = self.__time
        

        for adjacentVertex in vertex.getAdjacentVertexSet():
            if(not adjacentVertex.wasExplored()):
                adjacentVertex.predecessor = vertex
                self.__DFS_VISIT_REC(adjacentVertex, exploreObj)
        self.__time += 1
        vertex.f = self.__time
        vertex.explore(exploreObj)
        return exploreObj
    #####################################################################
    #####################################################################

    #Verifica se Graph é conexo
    def isConnected(self):

        if (self.__directedGraph):
            for v in self.__V:
                self.setVertexListAsUnexplored()
                self.DFS_Rec(None)
                for u in self.__V:
                    if (u.d == np.inf):
                        return False
            return True
        return True

    def isAcyclic(self):
        if (self.__directedGraph):
            self.DFS_Rec(None)
            for u in self.__V:
                for v in u.getAdjacentVertexSet():
                    if (Edge.isBackEdge(u, v)):
                        return False
            return True
        return False

class Edge:
    #Aresta de retorno
    @staticmethod
    def isBackEdge(u, v):
        return (v.d <= u.d) and (u.d < u.f) and (u.f <= v.f)

    #Aresta de árvore
    @staticmethod
    def isTreeEdgeOrForwardEdge(u, v):
        return (u.d < v.d) and (v.d < v.f) and (v.f < u.f)

    #Aresta cruzada
    @staticmethod
    def isCrossEdge(u, v):
        return (v.d < v.f) and (v.f < u.d) and (u.d < u.f)

class Vertex:
    #Inicializa Vértice
    def __init__(self, parentGraph, index=0):
        self.__parentGraph = parentGraph
        self.__index = index
        self.__adjacentVertexSet = SortedSet()
        self.__explored = False
        self.__name = ""
        #Documentação numpy.inf : https://www.numpy.org/devdocs/reference/constants.html
        self.d = np.inf
        self.f = np.inf
        self.predecessor = None

    def setIndex(self, index):
        self.__index = index

    def getIndex(self):
        return self.__index

    def addAdjacentVertex(self, adjacentVertex):
        if (isinstance(adjacentVertex, Vertex)):
            if (not (adjacentVertex in self.__adjacentVertexSet)):
                self.__adjacentVertexSet.add(adjacentVertex)
        else:
            raise("addAdjacentVertex error. adjacentVertex must be of class Vertex.")
        return

    def setName(self, name):
        self.__name = name
        return self

    def getName(self):
        if (len(self.__name) == 0):
            return str(self.__index)
        return self.__name

    def getAdjacentVertexSet(self):
        return self.__adjacentVertexSet

    def wasExplored(self):
        return self.__explored

    def setAsUnexplored(self):
        self.__explored = False
        self.d = np.inf
        self.f = np.inf
        self.predecessor = None
        return

    def explore(self, exploreObj=None):
        if ((not self.__explored) and (exploreObj is not None)):
            exploreObj.explore(self)

        self.__explored = True

        return

    def vertex2str(self, showCompleteInfo=False):
        vertexStr = str("")
        vertexStr += self.getName()
        if (showCompleteInfo):
            vertexStr += " [d=" + str(self.d) + "][f=" + str(self.f) + "]"
        vertexStr += " -> "

        if (len(self.__adjacentVertexSet) > 0):
            for adjacentVertex in self.__adjacentVertexSet:
                vertexStr += " " + adjacentVertex.getName()

        return vertexStr

    def __lt__(self, other):
        return self.__index < other.__index

    def __gt__(self, other):
        return self.__index > other.__index

    def __str__(self):
        return self.vertex2str(True)

class CExplore:
    def __init__(self, graph = None):
        self._graph = graph
        self.__initialVertexIndex = 0
        self._indexVertex1 = -1
        self._indexVertex2 = -1
        return

    def check(self, indexVertex1, indexVertex2):
        if (isinstance(indexVertex1, Vertex) and isinstance(indexVertex2, Vertex)):
            return self.check(indexVertex1.getIndex(), indexVertex2.getIndex())

        elif (isinstance(indexVertex1, int) and isinstance(indexVertex2, int)):
            self._indexVertex1 = indexVertex1

            self._indexVertex2 = indexVertex2

            self.setInitialVertexIndex(indexVertex1)

            self._makeCalculations()

        else:
            raise("Error! u and v must be of class Vertex or integers.")

        return self

    def _makeCalculations(self):
        return self

    def setInitialVertexIndex(self, index):
        self.__initialVertexIndex = index
        return

    def getInitialVertexIndex(self):
        return self.__initialVertexIndex

    def explore(self, vertex):
        print ("Explorando vertice: ", vertex.getIndex(), " d=", vertex.d, " f=", vertex.f)


graph = Graph(True)

for i in range(1, 11, 1):
    graph.createVertex(i)

graph.addEdge(1 ,2)
graph.addEdge(1 ,3)
graph.addEdge(1, 4)
graph.addEdge(2, 3)
graph.addEdge(2, 5)
graph.addEdge(2, 6)
graph.addEdge(3, 4)
graph.addEdge(3, 6)
graph.addEdge(4, 6)
graph.addEdge(5, 7)
graph.addEdge(5, 8)
graph.addEdge(5, 9)
graph.addEdge(6, 8)
graph.addEdge(7, 10)
graph.addEdge(8, 9)
graph.addEdge(8, 10)
graph.addEdge(9, 7)
print ("Graph")
print (graph)

print ("DFS Rec")
graph.DFS_Rec(CExplore())