
from copy import deepcopy
from typing import List
from xmlrpc.client import boolean
from estrutura import *
import sys
import random

TEST_CASES = ['./tests/brd14051.tsp',
              './tests/d15112.tsp',
              './tests/d18512.tsp',
              './tests/fnl4461.tsp',
              './tests/pla79397.tsp',
              './tests/pla33810.tsp',
              './tests/pla85900.tsp',
              './tests/pr1002.tsp']

NUM_RUNS = 10


<<<<<<< HEAD
def getNearest(g:grafo, node:int, nodesInPath:List[boolean])->int:
=======
def getNearest(g: grafo, node: int, nodesInPath: List[bool]) -> int:
>>>>>>> 1ffc3f9e92a1ef3b30798de4568e2ae17b9a1dc6
    best = math.inf
    nearest = math.inf
    for i in range(len(g.vertices)):
        if i != node:
            dist = distanciaEuclidiana(g.vertices[node], g.vertices[i])
            if (dist < best and not nodesInPath[i]):
                best = dist
                nearest = i
    return nearest

<<<<<<< HEAD
def insereNoCiclo(g:grafo, path:List[int], nodesInPath:List[boolean],vertice:int)->None:
    entryCost=0
    exitCost=0
    bestCost=math.inf
    entryIndex=math.inf
    for i in range(len(path)):
        if i !=0 and i!=len(path)-1:
            exitCost=distanciaEuclidiana(g.vertices[path[i]],g.vertices[path[i-1]])
            entryCost=distanciaEuclidiana(g.vertices[path[i]],g.vertices[vertice])+\
                            distanciaEuclidiana(g.vertices[path[i-1]],g.vertices[vertice])
                            
        elif i==0:
            exitCost=distanciaEuclidiana(g.vertices[path[len(path)-1]],g.vertices[path[i]])
            entryCost=distanciaEuclidiana(g.vertices[path[len(path)-1]],g.vertices[vertice])+\
                            distanciaEuclidiana(g.vertices[path[i]],g.vertices[vertice])
                            
=======

def insereNoCiclo(g: grafo, path: List[int], nodesInPath: List[bool], vertice: int) -> None:
    entryCost = 0
    exitCost = 0
    bestCost = math.inf
    entryIndex = math.inf
    n = len(path)
    for i in range(n):
        if i != 0 and i != n-1:
            exitCost = distanciaEuclidiana(
                g.vertices[path[i]], g.vertices[path[i-1]])
            entryCost = distanciaEuclidiana(g.vertices[path[i]], g.vertices[vertice]) +\
                distanciaEuclidiana(g.vertices[path[i-1]], g.vertices[vertice])

        elif i == 0:
            exitCost = distanciaEuclidiana(
                g.vertices[path[n-1]], g.vertices[path[i]])
            entryCost = distanciaEuclidiana(g.vertices[path[n-1]], g.vertices[vertice]) +\
                distanciaEuclidiana(g.vertices[path[i]], g.vertices[vertice])

>>>>>>> 1ffc3f9e92a1ef3b30798de4568e2ae17b9a1dc6
        else:
            exitCost = distanciaEuclidiana(
                g.vertices[path[i]], g.vertices[path[i-1]])
            entryCost = distanciaEuclidiana(g.vertices[path[i]], g.vertices[vertice]) +\
                distanciaEuclidiana(g.vertices[path[0]], g.vertices[vertice])

        custoTotal = entryCost-exitCost

        if custoTotal < bestCost:
            bestCost = custoTotal
            entryIndex = i

    if entryIndex < n-1:
        path.insert(entryIndex, vertice)
    else:
        path.append(vertice)
    nodesInPath[vertice] = True
    return


def buildNewPath(path: List[int], i: int, j: int) -> List[int]:
    newPath = []
    for k in range(i):
        newPath.append(path[k])
    index = j
    for k in range(i, j+1):
        newPath.append(path[index])
        index = index-1
    for k in range(j+1, len(path)):
        newPath.append(path[k])

    return newPath


def getDistancia(g: grafo, path: List[int]):
    weight = 0
    for i in range(len(path)-1):
        weight = weight + \
            distanciaEuclidiana(
                g.vertices[path[i]], g.vertices[path[i+1]])
    weight = weight + \
        distanciaEuclidiana(
            g.vertices[path[0]], g.vertices[path[len(path)-1]])
    return weight


def getVertices():
    descricao = []
    imput = ''
    vertices = []
    while imput.find('EOF') == -1:
        imput = input()
        descricao.append(imput.strip("\r"))
    construtor = descricao[6: len(descricao)-1]
    for i in range(len(construtor)):
        vertices.append(construtor[i].split(' '))
    return vertices


<<<<<<< HEAD
def isAllInPath(nodesInPath)->boolean:
=======
def isAllInPath(nodesInPath) -> bool:
>>>>>>> 1ffc3f9e92a1ef3b30798de4568e2ae17b9a1dc6
    for i in nodesInPath:
        if not i:
            return False
    return True


def nearestNeighbor(g: grafo) -> List[int]:
    nodesInPath = [False]*len(g.vertices)
    path = [random.randint(0, len(g.vertices)-1)]
    nodesInPath[path[0]] = True
    while not isAllInPath(nodesInPath):
        putNearestAtPath(path, g, nodesInPath)
    return path


<<<<<<< HEAD
def putNearestAtPath(path:List[int], g:grafo, nodesInPath:List[boolean]):
=======
def putNearestAtPath(path: List[int], g: grafo, nodesInPath: List[bool]):
>>>>>>> 1ffc3f9e92a1ef3b30798de4568e2ae17b9a1dc6
    ultimoInserido = path[len(path)-1]
    maisProximo = getNearest(g, ultimoInserido, nodesInPath)
    path.append(maisProximo)
    nodesInPath[maisProximo] = True

<<<<<<< HEAD
def beginCicle(g:grafo,nodesInPath:List[boolean])->List[int]:
=======

def beginCicle(g: grafo, nodesInPath: List[bool]) -> List[int]:
>>>>>>> 1ffc3f9e92a1ef3b30798de4568e2ae17b9a1dc6
    path = []
    v1 = random.randint(0, len(g.vertices)-1)
    path.append(v1)
    nodesInPath[path[0]] = True
    v2 = getNearest(g, v1, nodesInPath)
    path.append(v2)
    nodesInPath[path[1]] = True
    return path


def nearestInsertion(g: grafo) -> List[int]:
    nodesInPath = [False]*len(g.vertices)
    path = beginCicle(g, nodesInPath)
    while not isAllInPath(nodesInPath):
        vertice = path[random.randint(0, len(path)-1)]
        maisProximo = getNearest(g, vertice, nodesInPath)
        insereNoCiclo(g, path, nodesInPath, maisProximo)
    return path


def opt_2(g: grafo, path: List[int], weight):
    bestPath = path
    bestWeight = weight
    n = len(path)
    for i in range(n-1):
        for j in range(i+1, n):
            newPath = buildNewPath(path, i, j)
            newWeight = getDistancia(g, newPath)
            if newWeight < bestWeight:
                bestWeight = newWeight
                bestPath = deepcopy(newPath)
    if bestWeight < weight:
        bestWeight, bestPath = opt_2(g, bestPath, bestWeight)
    return bestWeight, bestPath


def opt_3(g: grafo, path: List[int]):
    better = True
    n = len(path)
    while better:
        descount = 0
        for i in range(n-4):
            for j in range(i + 2, n-2):
                for k in range(j + 2, n):
                    descount = descount + \
                        getBestCase(path, g, i, j, k)
        if descount >= 0:
            better = False
    return path


def getBestCase(path, g, i, j, k):
    if i == 0:
        anti = len(path)-1
    else:
        anti = i-1
    A, B, C, D, E, F = path[anti], path[i], path[j -
                                                 1], path[j], path[k-1], path[k]
    default = distanciaEuclidiana(g.vertices[A], g.vertices[B]) + distanciaEuclidiana(
        g.vertices[C], g.vertices[D]) + distanciaEuclidiana(g.vertices[E], g.vertices[F])
    case1 = distanciaEuclidiana(g.vertices[A], g.vertices[C]) + distanciaEuclidiana(
        g.vertices[B], g.vertices[D]) + distanciaEuclidiana(g.vertices[E], g.vertices[F])
    case2 = distanciaEuclidiana(g.vertices[A], g.vertices[B]) + distanciaEuclidiana(
        g.vertices[C], g.vertices[E]) + distanciaEuclidiana(g.vertices[D], g.vertices[F])
    case3 = distanciaEuclidiana(g.vertices[A], g.vertices[D]) + distanciaEuclidiana(
        g.vertices[E], g.vertices[B]) + distanciaEuclidiana(g.vertices[C], g.vertices[F])
    case4 = distanciaEuclidiana(g.vertices[F], g.vertices[B]) + distanciaEuclidiana(
        g.vertices[C], g.vertices[D]) + distanciaEuclidiana(g.vertices[E], g.vertices[A])

    if default > case1:
        path[i:j] = reversed(path[i:j])
        return case1-default
    elif default > case2:
        path[j:k] = reversed(path[j:k])
        return case2-default
    elif default > case3:
        aux = path[j:k] + path[i:j]
        path[i:k] = aux
        return case3-default
    elif default > case4:
        path[i:k] = reversed(path[i:k])
        return case4-default
    return 0


def main():
    # x = 33522
<<<<<<< HEAD
    construtor = getVertices()
    mediaBuild = 0
    max = 0
    min = math.inf

    minM = math.inf
    maxM = 0
    mediaM = 0
    g = constroiGrafo(construtor)
<<<<<<< HEAD
    for _  in range(10):
        vertices =  nearestNeighbor(g)
        vertices1=deepcopy(vertices)
        caminho = getDistancia(g, vertices)
        if caminho>max:
            max=caminho
        if caminho<min:
            min=caminho
        mediaBuild=mediaBuild+caminho
        best,bestPath = opt_2(g, vertices, caminho)
        if best>maxM:
            maxM=best
        if best<minM:
            minM=best
        mediaM=mediaM+best
        bestpath=opt_3(g,vertices1)
        opt3=getDistancia(g,bestpath)
=======
    for _ in range(2):
        vertices = nearestNeighbor(g)
        vertices1 = deepcopy(vertices)
        caminho = getDistancia(g, vertices)
        if caminho > max:
            max = caminho
        if caminho < min:
            min = caminho
        mediaBuild = mediaBuild+caminho
        best, bestPath = opt_2(g, vertices, caminho)
        bestpath = opt_3(g, vertices1)
        bestopt = getDistancia(g, bestpath)
        if best > maxM:
            maxM = best
        if best < minM:
            minM = best
        mediaM = mediaM+best
>>>>>>> 1ffc3f9e92a1ef3b30798de4568e2ae17b9a1dc6
    print("Media do Contrutivo: "+str(mediaBuild/100))
    print("Pior do Contrutivo: "+str(max))
    print("Melhor do Construtivo: "+str(min))

    print("Media do Melhorativo: "+str(mediaM/100))
    print("Pior do Melhorativo: "+str(maxM))
    print("Melhor do Melhorativo: "+str(minM))
    distante = nearestInsertion(g)
    caminho = getDistancia(g, distante)
    bestd, bestPath1 = opt_2(g, distante, caminho)
    print(distante)
=======

    if sys.argv[1] == "-1":
        print("ola")
    else:
        construtor = getVertices()
        g = constroiGrafo(construtor)
        better = math.inf
        for _ in range(NUM_RUNS):
            vertices = nearestNeighbor(g)
            caminho = getDistancia(g, vertices)
            if caminho > max:
                max = caminho
            if caminho < min:
                min = caminho
            mediaBuild = mediaBuild+caminho
            best, bestPath = opt_2(g, vertices, caminho)

            bestopt = getDistancia(g, bestpath)
            if best > maxM:
                maxM = best
            if best < minM:
                minM = best
            mediaM = mediaM+best
        print("Media do Contrutivo: "+str(mediaBuild/100))
        print("Pior do Contrutivo: "+str(max))
        print("Melhor do Construtivo: "+str(min))
        print("Media do Melhorativo: "+str(mediaM/100))
        print("Pior do Melhorativo: "+str(maxM))
        print("Melhor do Melhorativo: "+str(minM))
        distante = nearestInsertion(g)
        caminho = getDistancia(g, distante)
        bestd, bestPath1 = opt_2(g, distante, caminho)
        print(distante)
>>>>>>> 6236dcd7f973db09613f986f72be4e8a0b907c13


main()
