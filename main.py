
from typing import List
from estrutura import *
import sys


def getVertices(caminho):
    arq = open(caminho)
    descricao = []
    vertices = []
    for line in arq:
        descricao.append(line.strip('\n'))
    index = descricao.index('NODE_COORD_SECTION')
    construtor = descricao[index + 1: len(descricao)-1]
    for i in range(len(construtor)):
        vertices.append(construtor[i].split(' ', 3))
    return vertices


def getDistancias(g: grafo) -> List[List[int]]:
    EDs = []
    for i in range(len(g.vertices)):
        ED = []
        for j in range(i+1, len(g.vertices)):
            dist = distanciaEuclidiana(g.vertices[i], g.vertices[j])
            ED.append(dist)
        EDs.append(ED)
    return EDs


def main():
    x = 33522
    caminho = sys.argv[1]
    construtor = getVertices(caminho)
    g = constroiGrafo(construtor)
    EDs = getDistancias(g)
    print(EDs)


main()
