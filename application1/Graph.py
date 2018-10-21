import numpy as np

from Vertex import Vertex
from Vertex import CExplore


class Graph:
    # Incializa a Classe Graph
    def __init__(self, directedGraph=False):
        self.__V = list()
        self.__topological = list()
        self.__directedGraph = directedGraph
        self.__time = 0
        self.__isConnected = None
        return

    # AdicionaAresta -> chamada pelo método createVertex()
    def addVertex(self, v, index):
        if (not (v in self.__V)):
            v.setIndex(index)
            self.__V.insert(index-1, v)
        return v

    def addVertexTopological(self, v):
        if (not (v in self.__V)):
            self.__topological.insert(0, v)
        return v
    
    # Retorna a lista topológica do Grafo caso ele tenha
    def getTopologicalSet(self):
        str = "Ordenacao de Atividades: "
        for vertex in self.__topological:
            str += vertex+" "
        return str
    
    # Retorna se o grafo é conectado.
    # Valor é instanciado após a DFS ser executada. Antes disso, o valor é None
    def getIsConnected(self):
        return self.__isConnected

    # Cria vértice -> chama função addVertex() 
    def createVertex(self, index):
        return self.addVertex(Vertex(self), index)

    # Adiciona aresta
    def addEdge(self, u, v):

        # Verifica se os parâmetros passados são Vértices ou Int
        # Caso sejam int, é chamada novamente a função passando o objeto salvo na posição da lista __V do Graph
        if (isinstance(u, Vertex) and isinstance(v, Vertex)):

            # Verifica se os vértices estão incluídos na lista __V o Graph
            if ((u in self.__V) and (v in self.__V)):

                # Adiciona "v" na lista de adjacência de "u"
                u.addAdjacentVertex(v)

                # Se o grafo não for direcionado, faz o mesmo passo só que "v" para "u"
                if (not self.__directedGraph):
                    v.addAdjacentVertex(u)

                return

            # Se u e v não estiverem na lista __V do Graph, retorna erro
            else:
                raise("Erro metodo 'addEdge'. u e v nao pertence ao grafo.")
        elif (isinstance(u, int) and isinstance(v, int)):
            self.addEdge(self[u-1], self[v-1])
        else:
            raise("Erro metodo 'addEdge'. u e v não sao do tipo Vertex ou Int.")
        return

    # Busca vértice na posição k pertence a lista __V de Graph
    def __getitem__(self, k):
        if ((len(self.__V) > 0) and (k >= 0) and (k < len(self.__V))):
            return self.__V[k]
        return None

    # Retorna tamnho da lista de vértices adjacentes
    def __len__(self):
        return len(self.__V)

    # Imprimir o objeto
    # print(Graph)
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
    # Busca em Profundidade Recursiva
    # Obs: o parâmetro exploredResult=False "inibe" a impressão da exploração dos vértices. Caso queira visualizar, basta passar True

    def DFS_Rec(self, exploreObj=None, exploredResult=False):

        # Cria lista de vértices não explorados
        self.setVertexListAsUnexplored()
        self.__time = 0

        # Partimos do presuposto que não é conectado
        testIsConnected = False

        # Faz uma busca em profundidade e encontra uma componente conexa
        for vertex in self.__V:
            if (not vertex.wasExplored() and not testIsConnected):
                self.__DFS_VISIT_REC(vertex, exploreObj)
                testIsConnected = True
        '''
        Se a componente conexa encontrada pela DFS for do mesmo tamanho da lista de vértices
        o grafo é marcado como conexo, senão como não conexo
        '''
        if(len(self.__topological) == len(self.__V)):
            self.__isConnected = True
        else:
            self.__isConnected = False

        return exploreObj

    def __DFS_VISIT_REC(self, vertex, exploreObj=None):
        # Incrementa tempo e marca a abertura do vértice
        self.__time += 1
        vertex.d = self.__time
        
        # Verifica todos vértices adjacentes ao vértice para chamar recursivamente a função
        for adjacentVertex in vertex.getAdjacentVertexSet():
            if(not adjacentVertex.wasExplored()):
                adjacentVertex.predecessor = vertex
                self.__DFS_VISIT_REC(adjacentVertex, exploreObj)
        
        # Incrementa o tempo e marca o fechamento do vértice
        self.__time += 1
        vertex.f = self.__time
        
        # Salva vértice na ordenação topológica do vértice
        self.addVertexTopological(vertex.getName())

        # Imprime resultado dos vértice explorado
        vertex.explore(exploreObj)
        
        # Retorna o objeto explorado
        return exploreObj
    #####################################################################
    #####################################################################