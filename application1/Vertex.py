import numpy as np
from Edge import Edge

class Vertex:
    #Inicializa Vértice
    def __init__(self, parentGraph, index=0):
        self.__parentGraph = parentGraph
        self.__index = index
        self.__adjacentVertexSet = list()
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
                self.__adjacentVertexSet.append(adjacentVertex)
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