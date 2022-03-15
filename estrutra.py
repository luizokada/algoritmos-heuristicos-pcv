

from cv2 import sqrt


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
    return sqrt(x+y)
