

import sys


def getVertices(caminho):
    arq = open(caminho)
    descricao = []
    vertices = []
    for line in arq:
        descricao.append(line)
    index = descricao.index('NODE_COORD_SECTION\n')
    construtor = descricao[index + 1: len(descricao)-1]
    for i in range(len(construtor)):
        vertices.append(construtor[i].split(' ', 3))
    return vertices


def main():
    x = 33522
    caminho = sys.argv[1]
    construtor = getVertices(caminho)
    print(construtor)


main()
