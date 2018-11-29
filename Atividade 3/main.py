import os
# Python program to find  
# maximal Bipartite matching. 
class GFG: 
    def __init__(self,graph): 
          
        # Grafo 
        self.status = False
        self.graph = graph  
        self.app = len(graph) #aplicações
        self.computers = len(graph[0])-2 #computadores
        self.numberOfApp = list() #lista de qtd EXIGIDA de app's a serem inicializados
        self.nameOfApp = list() #nome dos app's
        for v in range(self.app):
            self.numberOfApp.append(self.graph[v][10])
            self.nameOfApp.append(self.graph[v][11])

    def getNameOfApp(self, app):
        return self.nameOfApp[app]
    
    def getNumberOfApp(self, app):
        return int(self.numberOfApp[app])

    def getStatus(self):
        return self.status

   
    # Uma função recursiva baseada em DFS
    # retorna true 
    # se uma correspondência para o vértice u for possível
    def bpm(self, u, matchR, seen): 
  
        # Try every job one by one 
        for v in range(self.computers): 
  
            # Se a aplicação estiver interessada no computador
            # e o computador não estiver visitado
            if self.graph[u][v] and seen[v] == False: 
                  
                # Marca V como visitado
                seen[v] = True 
  
                '''
                Se o computador 'v' não estiver atribuído a uma aplicação 
                OU a aplicação atribuída anteriormente ao computador v 
                (que é matchR [v]) tiver um computador alternativo disponível. 
                Como v é marcado como visitado na linha acima, 
                matchR [v] na seguinte chamada recursiva 
                não obterá o computador 'v' novamente
                '''
                if matchR[v] == "_" or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False
  
    # Retorna o número máximo de correspondência
    # Maximum Bipartite Matching (MBP) 
    def maxBPM(self): 
        '''
        Uma matriz para acompanhar as aplicações atribuídos a computadores.
        O valor da correspondência matchR[i] é o número 
        da aplicação atribuído ao computador i, 
        o valor -1 indica que ninguém está atribuído.
        '''
        matchR = ["_"] * self.computers 
          
        # Count of jobs assigned to applicants 
        result = 0 
        for i in range(self.app): 
              
            # Marcar todos os trabalhos como não vistos para o próximo computador. 
            seen = [False] * self.computers 

            for j in range(self.getNumberOfApp(i)):
                # Descubra se a aplicação 'u' pode conseguir um computador
                if self.bpm(i, matchR, seen): 
                    result += 1
            
            if result == self.getNumberOfApp(i):
                self.status = True
            else:
                self.status = False
            result = 0
        return matchR 

#############################################################################################
# Menu inicial
#############################################################################################
def print_menu_arquivo():
    print("\nDigite o nome do arquivo a ser lido:")

# Leitura do arquivo
def readArq(path):
    arq = open(path, 'r')
    return arq.readlines()

loop = True
while loop:
    print_menu_arquivo()
    arquivo = input()
    path = None

    # Navega pela pasta a procura do arquivo
    for root, dirs, files in os.walk("instances"):
        if path is None:  # Evita encontrar dois arquivos com o mesmo nome
            for file in files:
                if arquivo in file:
                    print("\nArquivo encontrado!")
                    path = os.path.join(root, file)
                    print("Caminho: " + path + "\n")
                    loop = False
                    break  # Evita encontrar dois arquivos com o mesmo nome

    if path is None:
        print("\n" + 90 * "#")
        print("Arquivo nao encontrado! Certifique-se de estar rodando o sistema a partir da pasta raiz!")
        print("" + 90 * "#")

# Lê arquivo
linesOfArq = readArq(path)

#Inicializa lista que será utilizada para calcular o fluxo
bpGraph = list()

#Tratramento do arquivo de entrada
for i in range (len(linesOfArq)):
    lista = [0,0,0,0,0,0,0,0,0,0]
    result = 0
    line = linesOfArq[i]
    values = (line.split(' '))
    
    aux = list(values[0])
    #Dados da aplicação passados pelo arquivo
    nameApplication = aux[0]
    allocatedComputerNumber = aux[1]
    listComputer = list(values[1])
    
    #Remove quebra de linha lida do aruqivo
    if "\n" in listComputer:
        listComputer.remove("\n")
    
    for i in range (len(listComputer)):
        lista[int(listComputer[i])] = 1

    
    lista.append(allocatedComputerNumber)
    lista.append(nameApplication)
    bpGraph.append(lista)


g = GFG(bpGraph) 
aux = list()
aux = g.maxBPM()
for i in range (len(aux)):
    if aux[i] != "_":
        aux[i] = g.getNameOfApp(int(aux[i]))

################################################
# Resposta Final
################################################
if g.getStatus():
    answer = ""
    for computer in aux:
        answer += computer+" "
    print(answer)
else:
    print("!")
