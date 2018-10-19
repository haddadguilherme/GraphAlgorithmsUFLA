from Vertex import Vertex
from Vertex import CExplore

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

    def __repr__(self):
        return str(self.__V)
    
    #AdicionaAresta -> chamada pelo método createVertex()
    #param: @v = vértice, @index = indice do vértice
    def addVertex(self, v, index):
        if (not (v in self.__V)):
            v.setIndex(index)
            self.__V.insert(index-1, v)
        return v

    #Cria vértice -> chama função addVertex() 
    def createVertex(self, index):
        return self.addVertex(Vertex(self), index)

    def printList(self):
        print ("Final List : ", self.__V.__getitem__)

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