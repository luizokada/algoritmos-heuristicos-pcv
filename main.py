
from copy import deepcopy
from typing import List
from estrutura import *
import sys
import random


def getVertices():
    descricao = []
    imput = ''
    vertices = []
    while imput.find('EOF')==-1:
        imput = input()
        descricao.append(imput.strip("\r"))
        
    index = descricao.index('NODE_COORD_SECTION')
    construtor = descricao[index + 1: len(descricao)-1]
    for i in range(len(construtor)):
       
        vertices.append(construtor[i].split(' '))
    return vertices

def getDistancias(g: grafo) -> List[List[int]]:
    EDs = []
    for i in range(len(g.vertices)):
        ED = []
        for j in range(len(g.vertices)):
            dist = distanciaEuclidiana(g.vertices[i], g.vertices[j])
            if dist == 0:
                dist = math.inf
            ED.append(dist)
        EDs.append(ED)
    return EDs


def isInseridos(inseridos):
    for i in inseridos:
        if not i:
            return False
    return True


def vizinhoMaisProximo(g: grafo, EDs):
    inseridos = [False]*len(g.vertices)
    caminho = []
    Eds = deepcopy(EDs)
    roteiro = [random.randint(0, len(g.vertices)-1)]
    while not isInseridos(inseridos):
        insereMaisProximo(roteiro, Eds, caminho, inseridos)
    return caminho


def insereMaisProximo(roteiro, Eds, caminho, inseridos):
    ultimoInserido = roteiro[len(roteiro)-1]
    maisProximo = Eds[ultimoInserido].index(min(Eds[ultimoInserido]))
    if not inseridos[maisProximo]:
        roteiro.append(maisProximo)
        caminho.append(Eds[ultimoInserido][maisProximo])
        inseridos[maisProximo] = True
    Eds[ultimoInserido][maisProximo] = math.inf
    Eds[maisProximo][ultimoInserido] = math.inf


def insereMaisLonge(roteiro, Eds, caminho, inseridos):
    ultimoInserido = roteiro[len(roteiro)-1]
    maisLonge = Eds[ultimoInserido].index(max(Eds[ultimoInserido]))
    if not inseridos[maisLonge]:
        roteiro.append(maisLonge)
        caminho.append(Eds[ultimoInserido][maisLonge])
        inseridos[maisLonge] = True
    Eds[ultimoInserido][maisLonge] = math.inf
    Eds[maisLonge][ultimoInserido] = math.inf


def main():
    x = 33522
    construtor = getVertices()
    g = constroiGrafo(construtor)
    EDs = getDistancias(g)
    menor=math.inf
    if len(g.vertices)>100:
        num_exec=2
    else:
        num_exec=100
        
    for i in range(num_exec): 
        caminho = vizinhoMaisProximo(g, EDs)
        soma = 0
        for peso in caminho:
            soma = soma+peso
        if soma<menor:
            menor = soma
            
    print(menor)


main()
