import os

# Menu inicial
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

status = True
listComputers = ["_","_","_","_","_","_","_","_","_","_"]
#print(listComputers)

# Lê arquivo
linesOfArq = readArq(path)

#Leitura das linhas do arquivo
for i in range(len(linesOfArq)):
    line = linesOfArq[i]
    values = (line.split(' '))
    aux = list(values[0])
    #Dados da aplicação passados pelo arquivo
    nameApplication = aux[0]
    allocatedComputerNumber = aux[1]
    listOfComputer = list(values[1])
    
    #Remove quebra de linha lida do aruqivo
    if "\n" in listOfComputer:
        listOfComputer.remove("\n")
    
    allocated = 0
    while listOfComputer != []:
        computer = listOfComputer.pop(0)
        if allocated == int(allocatedComputerNumber):
            break
        elif listComputers[int(computer)] == "_":
            listComputers[int(computer)] = nameApplication
            allocated += 1

    print(listComputers)
    #print(allocated)
    if allocated == int(allocatedComputerNumber):
        status = True
    else:
        status = False
        break
        
if status == True:
    respost = ""
    for computer in listComputers:
        respost += computer+" "
    print(respost)  
else:
    print("!")