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