
import math


class grafo:
    def __init__(self) -> None:
        self.vertices = []

    def setVertice(self, x, y):
        v = vertice(x, y)
        self.vertices.append(v)


class vertice:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def distanciaEuclidiana(v: vertice, u: vertice) -> int:
    x = (v.x - u.x)**2
    y = (v.y-u.y)**2
    return math.sqrt(x+y)


def constroiGrafo(descricao) -> grafo:
    g = grafo()

    for vertice in descricao:
        g.setVertice(int(vertice[1]), int(vertice[2]))

    return g


def construtivoVizinhoMaisProximo():
    g = constroiGrafo()

    # fazer algoritmo aqui

    return g


def lerVertices():
    # ler até encontra NODE_COORD_SECTION

    ## linha = lerProximaLinha()
    return
