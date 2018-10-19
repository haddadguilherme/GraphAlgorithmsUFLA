from Graph import Graph
from Vertex import CExplore

graph = Graph(True)

for i in range(1, 11, 1):
    graph.createVertex(i)

graph.addEdge(1 ,2)
graph.addEdge(1 ,3)
graph.addEdge(1, 4)
graph.addEdge(2, 3)
graph.addEdge(2, 5)
graph.addEdge(6, 5)
graph.addEdge(3, 4)
graph.addEdge(3, 6)
graph.addEdge(4, 6)
graph.addEdge(5, 7)
graph.addEdge(5, 8)
graph.addEdge(5, 9)
graph.addEdge(6, 8)
graph.addEdge(7, 10)
graph.addEdge(8, 10)
graph.addEdge(9, 7)
print ("Graph")
print (graph)

print ("DFS Rec")
graph.DFS_Rec(CExplore())