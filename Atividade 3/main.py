import os

class GFG: 
    def __init__(self,graph): 
          
        # Grafo 
        self.__status = False
        self.__graph = graph  
        self.__app = len(graph) #aplicações
        self.__computers = len(graph[0])-2 #computadores
        self.__numberOfApp = list() #lista de qtd EXIGIDA de app's a serem inicializados
        self.__nameOfApp = list() #nome dos app's
        for v in range(self.__app):
            self.__numberOfApp.append(self.__graph[v][10])
            self.__nameOfApp.append(self.__graph[v][11])

    def getNameOfApp(self, app):
        return self.__nameOfApp[app]
    
    def getNumberOfApp(self, app):
        return int(self.__numberOfApp[app])

    def getStatus(self):
        return self.__status

   
    # Uma função recursiva baseada em DFS
    # retorna true 
    # se uma correspondência para o vértice u for possível
    def bpm(self, u, matchR, seen): 
  
        # Testa todos os computadores um a um 
        for v in range(self.__computers): 
  
            # Se a aplicação estiver interessada no computador
            # e o computador não estiver visitado
            if self.__graph[u][v] and seen[v] == False: 
                  
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
  
    # Retorna o matriz de match máximo
    # Maximum Bipartite Matching (MBP) 
    def maxBPM(self): 
        '''
        Uma matriz para acompanhar as aplicações atribuídos a computadores.
        O valor da correspondência matchR[i] é o número 
        da aplicação atribuído ao computador i, 
        o valor -1 indica que ninguém está atribuído.
        '''
        matchR = ["_"] * self.__computers 
          
        # Contador de número de aplicações alocadas 
        result = 0 
        for i in range(self.__app): 
              
            # Marcar todos os trabalhos como não vistos para o próximo computador. 
            seen = [False] * self.__computers 

            for j in range(self.getNumberOfApp(i)):
                # Descubra se a aplicação 'u' pode conseguir um computador
                if self.bpm(i, matchR, seen): 
                    result += 1
            
            if result == self.getNumberOfApp(i):
                self.__status = True
            else:
                self.__status = False
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

#Instancia o objeto GFG
g = GFG(bpGraph) 

#Lista auxiliar para substituir corretamento os nomes das aplicações
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
