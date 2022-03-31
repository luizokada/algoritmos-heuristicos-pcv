
from copy import deepcopy
from typing import List
from estrutura import *
import sys
import random


def getMaisPoximo(g, vertice, inseridos):
    menor = math.inf
    maisProximo = math.inf
    for i in range(len(g.vertices)):
        if i != vertice:
            dist = distanciaEuclidiana(g.vertices[vertice], g.vertices[i])
            if (dist < menor and not inseridos[i]):
                menor = dist
                maisProximo = i
    return menor, maisProximo

def insereNoCiclo(g, vertices:List[int], inseridos,vertice):
    custoDeEntrada=0
    custoAnterior=0
    menorCusto=math.inf
    indiceDeEntrada=math.inf
    for i in range(len(vertices)):
        if i !=0 and i!=len(vertices)-1:
            custoAnterior=distanciaEuclidiana(g.vertices[i],g.vertices[i+1])
            custoDeEntrada=distanciaEuclidiana(g.vertices[i],g.vertices[vertice])+distanciaEuclidiana(g.vertices[i+1],g.vertices[vertice])
        elif i==0:
            custoAnterior=distanciaEuclidiana(g.vertices[i],g.vertices[i+1])
            custoDeEntrada=distanciaEuclidiana(g.vertices[len(vertices)-1],g.vertices[vertice])+distanciaEuclidiana(g.vertices[i+1],g.vertices[vertice])
        else:
            custoAnterior=distanciaEuclidiana(g.vertices[i],g.vertices[0])
            custoDeEntrada=distanciaEuclidiana(g.vertices[i],g.vertices[vertice])+distanciaEuclidiana(g.vertices[0],g.vertices[vertice])
        custoTotal=custoDeEntrada-custoAnterior
        if custoTotal<menorCusto:
            menorCusto=custoTotal
            indiceDeEntrada=i
    if indiceDeEntrada< len(vertices)-1:
        vertices.insert(indiceDeEntrada,vertice)
    else:
        vertices.append(vertice)
    inseridos[vertice]=True
    return 

def inverteSubLista(vertice,i,j):
    lista=[]
    for k in range(i):
        lista.append(vertice[k])
    indice = j
    for k in range(i,j+1):
        lista.append(vertice[indice])
        indice=indice-1
    for k in range(j+1,len(vertice)):
        lista.append(vertice[k])
        
    return lista

def getDistancia(g, vertices):
    pesoTotal = 0
    for i in range(len(vertices)-1):
        pesoTotal = pesoTotal + \
            distanciaEuclidiana(
                g.vertices[vertices[i]], g.vertices[vertices[i+1]])
    pesoTotal = pesoTotal + \
            distanciaEuclidiana(
                g.vertices[vertices[0]], g.vertices[vertices[len(vertices)-1]])
    return pesoTotal


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


def isInseridos(inseridos):
    for i in inseridos:
        if not i:
            return False
    return True


def vizinhoMaisProximo(g: grafo):
    inseridos = [False]*len(g.vertices)
    caminho = 0
    roteiro = [random.randint(0, len(g.vertices)-1)]
    inseridos[roteiro[0]]=True
    while not isInseridos(inseridos):
        caminho = insereMaisProximo(roteiro, g, caminho, inseridos)
    caminho = caminho + \
        distanciaEuclidiana(
            g.vertices[roteiro[0]], g.vertices[roteiro[len(roteiro)-2]])
    return caminho, roteiro


def insereMaisProximo(roteiro, g, caminho, inseridos):
    ultimoInserido = roteiro[len(roteiro)-1]
    peso, maisProximo = getMaisPoximo(g, ultimoInserido, inseridos)
    roteiro.append(maisProximo)
    caminho = caminho + peso
    inseridos[maisProximo] = True
    return caminho

def insercaoMaisProximo(g: grafo):
    inseridos = [False]*len(g.vertices)
    caminho = 0
    v1=random.randint(0, len(g.vertices)-1)
    v2=random.randint(0, len(g.vertices)-1)
    while v2==v1:
        v2=random.randint(0, len(g.vertices)-1)
    v3=random.randint(0, len(g.vertices)-1)
    while v3==v1 or v3==v2:
        v3=random.randint(0, len(g.vertices)-1)
    roteiro = [v1,v2,v3]
    inseridos[roteiro[0]]=True
    inseridos[roteiro[1]]=True
    inseridos[roteiro[2]]=True
    while not isInseridos(inseridos):
        vertice=roteiro[random.randint(0,len(roteiro)-1)]
        _,maisProximo=getMaisPoximo(g,vertice,inseridos)
        insereNoCiclo(g,roteiro,inseridos,maisProximo)
    return roteiro




def opt_2(g, vertices, caminho):
    melhorCaminho=vertices
    melhor = caminho
    for i in range(len(vertices)-1):
        for j in range(i+1, len(vertices)):
            novoCaminho = inverteSubLista(vertices,i,j)
            novoPeso=getDistancia(g,novoCaminho)
            if novoPeso < melhor:
                melhor = novoPeso
                melhorCaminho = deepcopy(novoCaminho)        
    if melhor < caminho:
        melhor,melhorCaminho = opt_2(g, melhorCaminho, melhor)
    return melhor,melhorCaminho


def main():
    #x = 33522
    construtor = getVertices()
    mediaBuild = 0
    max = 0
    min= math.inf
    
    minM=math.inf
    maxM=0
    mediaM=0
    g = constroiGrafo(construtor)
    for _  in range(100):
        _, vertices = vizinhoMaisProximo(g)
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
    print("Media do Contrutivo: "+str(mediaBuild/100))
    print("Pior do Contrutivo: "+str(max))
    print("Melhor do Construtivo: "+str(min))
    
    
    print("Media do Melhorativo: "+str(mediaM/100))
    print("Pior do Melhorativo: "+str(maxM))
    print("Melhor do Melhorativo: "+str(minM))
    """distante=insercaoMaisProximo(g)
    caminho = getDistancia(g, distante)
    bestd,bestPath1 = opt_2(g, distante, caminho)
    print(distante)"""

main()
