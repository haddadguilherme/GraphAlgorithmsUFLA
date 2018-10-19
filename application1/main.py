import os

from Graph import Graph
from Vertex import CExplore

#Menu inicial
def print_menu_arquivo():
    print ("\nDigite o nome do arquivo a ser lido:")

#Leitura do arquivo
def readArq(path):
    arq = open(path, 'r')
    return arq.readlines()

loop=True      
while loop:
    print_menu_arquivo()
    arquivo = input()
    path = None

    # Navega pela pasta a procura do arquivo
    for root, dirs, files in os.walk("instances"):
        if path is None: # Evita encontrar dois arquivos com o mesmo nome
            for file in files:
                if arquivo in file:
                    print("\nArquivo encontrado!")
                    path = os.path.join(root, file)
                    print("Caminho: " + path +"\n")
                    loop = False
                    break # Evita encontrar dois arquivos com o mesmo nome
    
    if path is None:
        print("\n" + 67 * "#")
        print("Arquivo nao encontrado! Certifique-se de estar rodando o sistema a partir da pasta raiz!")
        print("" + 67 * "#")
#Lê arquivo
lines = readArq(path)

#Verifica tipo do grafo na primeira linha do arquivo
if("UNDIRECTED" in lines[0]):
    directedGraph = False
else:
    directedGraph = True

graph = Graph(directedGraph)
numberVertex = int(lines[1])
for i in range(1, numberVertex+1, 1):
    graph.createVertex(i)

#Adiciona arestas entre os vértices do grafo
for i in range(2, len(lines)):
    line = lines[i].split()
    graph.addEdge(int(line[0]), int(line[1]))

print("Graph")
print(graph)

print ("DFS Rec")
graph.DFS_Rec(CExplore())

print("Graph after DFS")
print(graph)

print(graph.getTopologicalSet())
