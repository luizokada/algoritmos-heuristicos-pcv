
from copy import deepcopy
from typing import List
from xmlrpc.client import boolean
from estrutura import *
import sys
import random

TEST_CASES = [
    './tests/pla48.tsp',
    './tests/a280.tsp',
    './tests/att532.tsp',
    './tests/bier127.tsp',
    './tests/fnl4461.tsp',
    './tests/pla7397.tsp',
    './tests/brd14051.tsp',
    './tests/d15112.tsp',
    './tests/d18512.tsp',
    './tests/pla33810.tsp',
    './tests/pla85900.tsp'
]

NUM_RUNS = 10


def getNearest(g: grafo, node: int, nodesInPath: List[bool]) -> int:
    best = math.inf
    nearest = math.inf
    for i in range(len(g.vertices)):
        if i != node:
            dist = distanciaEuclidiana(g.vertices[node], g.vertices[i])
            if (dist < best and not nodesInPath[i]):
                best = dist
                nearest = i
    return nearest


def putInPath(g: grafo, path: List[int], nodesInPath: List[bool], vertice: int) -> None:
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


def getConstructiorByArq(path):
    arq = open(path)
    vertices = []
    description = []
    lines = arq.readlines()
    for line in lines:
        description.append(line.strip('\n'))
    if description[len(description)-1].find('EOF') == -1:
        n = len(description)
    else:
        n = len(description)-1
    construtor = description[6: n]
    for i in range(len(construtor)):
        vertices.append(construtor[i].split(' '))
    arq.close()
    return vertices


def writeResults(nearestNeihgborWeihgt, nearestInsertionWeight, opt2, opt3, path):
    response = "./results/"+path
    arq = open(response, 'w')
    arq.write("Teste: " + path+"\n")
    arq.write("Nearest Neihgbor: " + str(nearestNeihgborWeihgt)+"\n")
    arq.write("Opt 2 para Nearest Neihgbor: " + str(opt2[0])+"\n")
    arq.write("Opt 3 para Nearest Neihgbor: " + str(opt3[0])+"\n")
    arq.write("Nearest insertion: " + str(nearestInsertionWeight)+"\n")
    arq.write("Opt 2 para Nearest insertion: " + str(opt2[1])+"\n")
    arq.write("Opt 3 para Nearest insertion: " + str(opt3[1])+"\n")

    arq.close()
    return


def isAllInPath(nodesInPath) -> bool:
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


def putNearestAtPath(path: List[int], g: grafo, nodesInPath: List[bool]):
    ultimoInserido = path[len(path)-1]
    maisProximo = getNearest(g, ultimoInserido, nodesInPath)
    path.append(maisProximo)
    nodesInPath[maisProximo] = True


def beginCicle(g: grafo, nodesInPath: List[bool]) -> List[int]:
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
        putInPath(g, path, nodesInPath, maisProximo)
    return path


def opt_2(g: grafo, path: List[int], weight):
    bestPath = path
    bestWeight = weight
    n = len(path)
    for i in range(n-1):
        for j in range(i+1, n-1):
            if i == 0:
                anti = n-1
            else:
                anti = i-1
            if j == n-1:
                afterj = 0
            else:
                afterj = j+1
            exitCost = distanciaEuclidiana(
                g.vertices[path[i]], g.vertices[path[anti]])+distanciaEuclidiana(g.vertices[path[j]], g.vertices[path[afterj]])
            entryCost = distanciaEuclidiana(
                g.vertices[path[j]], g.vertices[path[anti]])+distanciaEuclidiana(g.vertices[path[i]], g.vertices[path[afterj]])
            newWeight = weight-exitCost+entryCost
            if newWeight < bestWeight:
                bestWeight = newWeight
                changVerteexi = i
                changVerteexj = j
    if bestWeight < weight:
        bestPath = buildNewPath(path, changVerteexi, changVerteexj)
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
    if sys.argv[1] == "test":
        for test in TEST_CASES:
            opt2Cases = []
            opt3Cases = []
            constructor = getConstructiorByArq(test)
            g = constroiGrafo(constructor)
            newpath = test.split("/")

            nearestNeighborPath = nearestNeighbor(g)
            nearestNeighborPath2 = deepcopy(nearestNeighborPath)
            nearestNeighborWeight = getDistancia(g, nearestNeighborPath)

            print("Nearest Neihgbor pronto para: "+newpath[2])

            opt2Weight, opt2Path = opt_2(
                g, nearestNeighborPath, nearestNeighborWeight)
            opt2Cases.append(opt2Weight)
            print("opt2 Nearest Neihgbor pronto para: "+newpath[2])

            opt3Path = opt_3(g, nearestNeighborPath2)
            opt3Weight = getDistancia(g, opt3Path)

            opt3Cases.append(opt3Weight)
            print("Opt3 Nearest Neihgbor pronto para: "+newpath[2])

            nearestInsertionPath = nearestInsertion(g)
            nearestInsertionPath2 = deepcopy(nearestInsertionPath)
            nearestInsertionWeight = getDistancia(g, nearestInsertionPath)
            print("Nearest insertion pronto para: "+newpath[2])

            opt2Weight, opt2Path = opt_2(
                g, nearestInsertionPath, nearestInsertionWeight)
            opt2Cases.append(opt2Weight)
            print("Opt2 Nearest insertion pronto para: "+newpath[2])

            opt3Path = opt_3(g, nearestInsertionPath2)
            opt3Weight = getDistancia(g, opt3Path)

            opt3Cases.append(opt3Weight)
            print("Opt 3 Nearest insertion pronto para: "+newpath[2])

            writeResults(nearestNeighborWeight, nearestInsertionWeight,
                         opt2Cases, opt3Cases, newpath[2])
    elif sys.argv[1] == "run":
        construtor = getVertices()
        opt2Cases = []
        opt3Cases = []
        g = constroiGrafo(construtor)

        nearestNeighborPath = nearestNeighbor(g)
        nearestNeighborPath2 = deepcopy(nearestNeighborPath)
        nearestNeighborWeight = getDistancia(g, nearestNeighborPath)

        opt2Weight, opt2Path = opt_2(
            g, nearestNeighborPath, nearestNeighborWeight)
        opt2Cases.append(opt2Weight)

        opt3Path = opt_3(g, nearestNeighborPath2)
        opt3Weight = getDistancia(g, opt3Path)
        opt3Cases.append(opt3Weight)

        nearestInsertionPath = nearestInsertion(g)
        nearestInsertionPath2 = deepcopy(nearestInsertionPath)
        nearestInsertionWeight = getDistancia(g, nearestInsertionPath)

        opt2Weight, opt2Path = opt_2(
            g, nearestInsertionPath, nearestInsertionWeight)
        opt2Cases.append(opt2Weight)

        opt3Path = opt_3(g, nearestInsertionPath2)
        opt3Weight = getDistancia(g, opt3Path)
        opt3Cases.append(opt3Weight)
        best = []
        best.append(min(opt2Cases))
        best.append(min(opt3Cases))
        print(min(best))


main()
