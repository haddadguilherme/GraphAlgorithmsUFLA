import sys


# Leitura do arquivo
def lerArquivo(path):

    arquivo = open(path, 'r')
    return arquivo.readlines()


# Criação da matriz com as interseções originais
def criaMatrizOriginal():

    for i in range(1, intersecoes+1):
    elementos = linhasArquivo[i].split()

    for n in range(len(elementos)):
        elementos[n] = int(elementos[n])

        if elementos[n] == i:
        matrizDistancia[i-1][i-1] = 0

        else:
        matrizDistancia[i-1][(elementos[n]-1)] = 1


# Criação da matriz com as interseções propostas
def criaMatrizSugerida():

    for i in range(1, intersecoes+1):
    elementos = linhasArquivo[i+intersecoes].split()

    for n in range(len(elementos)):
        elementos[n] = int(elementos[n])

        if elementos[n] == i:
        matrizDistancia2[i-1][i-1] = 0

        else:
        matrizDistancia2[i-1][(elementos[n]-1)] = 1


# Floyd-Warshall
def calcularMenoresDistancias(matriz):

    for k in range(intersecoes):
        for i in range(intersecoes):
            for j in range(intersecoes):
                matriz[i][j] = min(matriz[i][j], matriz[i][k] + matriz[k][j])

    return matriz


def validarProposta(matrizOriginal, matrizSugerida):

    resultado = "Sim"
    for i in range(intersecoes):
        for j in range(intersecoes):

            if matrizSugerida[i][j] > (matrizOriginal[i][j] * fator + constante):
                resultado = "Não"

    print(resultado)


linhasArquivo = lerArquivo(
    "/home/gustavo/git/GraphAlgorithmsUFLA/Implementação 2/entrada2.txt")
intersecoes = int(linhasArquivo[0])
fator = int(linhasArquivo[intersecoes*2+1][0])
constante = int(linhasArquivo[intersecoes*2+1][2])

# Criação das matrizes de distância com valores inteiros máximos
matrizDistancia = [[sys.maxsize] * intersecoes for i in range(intersecoes)]
matrizDistancia2 = [[sys.maxsize] * intersecoes for i in range(intersecoes)]

# Atribui a menor distância entre todas interseções na matriz
matrizDistancia = calcularMenoresDistancias(matrizDistancia)
matrizDistancia2 = calcularMenoresDistancias(matrizDistancia2)

validarProposta(matrizDistancia, matrizDistancia2)
