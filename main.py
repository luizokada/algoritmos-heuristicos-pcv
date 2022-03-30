
from copy import deepcopy
from typing import List
from estrutura import *
import sys
import random

def getMaisPoximo(g, vertice,inseridos):
    menor = math.inf
    maisProximo = math.inf
    for i in range(len(g.vertices)):
        if i !=vertice:
            dist = distanciaEuclidiana(g.vertices[vertice], g.vertices[i])
            if (dist <menor and not inseridos[i]):
                menor = dist
                maisProximo=i
    return menor,maisProximo
            

def getDistancia(g,vertices):
    pesoTotal=0
    for i in range(len(vertices)-1):
        pesoTotal=pesoTotal+distanciaEuclidiana(g.vertices[vertices[i]],g.vertices[vertices[i+1]])
    return pesoTotal
        
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


def vizinhoMaisProximo(g: grafo):
    inseridos = [False]*len(g.vertices)
    caminho = 0
    roteiro = [random.randint(0, len(g.vertices)-1)]
    inseridos[inseridos[0]]=True
    while not isInseridos(inseridos):
        caminho = insereMaisProximo(roteiro, g, caminho, inseridos)
    roteiro.append(roteiro[0])
    caminho=caminho+distanciaEuclidiana(g.vertices[roteiro[0]],g.vertices[roteiro[len(roteiro)-2]])
    return caminho,roteiro


def insereMaisProximo(roteiro, g, caminho, inseridos):
    ultimoInserido = roteiro[len(roteiro)-1]
    peso,maisProximo = getMaisPoximo(g,ultimoInserido,inseridos)
    if not inseridos[maisProximo]:
        roteiro.append(maisProximo)
        caminho = caminho + peso
        inseridos[maisProximo] = True
    return caminho


def insereMaisLonge(roteiro, Eds, caminho, inseridos):
    ultimoInserido = roteiro[len(roteiro)-1]
    maisLonge = Eds[ultimoInserido].index(max(Eds[ultimoInserido]))
    if not inseridos[maisLonge]:
        roteiro.append(maisLonge)
        caminho.append(Eds[ultimoInserido][maisLonge])
        inseridos[maisLonge] = True
    Eds[ultimoInserido][maisLonge] = math.inf
    Eds[maisLonge][ultimoInserido] = math.inf



def opt_2(g,vertices,caminho):
    melhorCaminho = vertices
    melhor=caminho
    for i in range(1,len(vertices)-3):
        aux=vertices[i]
        for j in range(i+1,len(vertices)-1):
            vertices[i]=vertices[j]
            vertices[j]=aux
            novoCaminho=getDistancia(g,vertices)
            if novoCaminho<melhor:
                melhor=novoCaminho
                melhorCaminho=deepcopy(vertices)
            vertices[j]=vertices[i]
            vertices[i]=aux
    if melhor<caminho:
        melhor= opt_2(g,melhorCaminho,melhor)
    return melhor
    


def main():
    x = 33522
    construtor = getVertices()
    g = constroiGrafo(construtor)
    menor=math.inf
    if len(g.vertices)>60:
        exc=3
    else:
        exc=10
    for i in range(exc):
        _,vertices = vizinhoMaisProximo(g)
        caminho=getDistancia(g,vertices)
        best=opt_2(g,vertices,caminho)    
        if best<menor:
            menor=best  
    print(menor)


main()
