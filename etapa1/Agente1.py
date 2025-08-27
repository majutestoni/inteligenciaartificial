class Agente:
    matriz = []
    direita = False
    cima  = False
    baixo = False
    esquerda = False
    n = 0
    i = 0
    j = 0

    def __init__(self, n,i,j):
        self.matriz =[[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.i = i
        self.j = j
        
    def vaiDireita(self):
        self.j += 1

    def vaiEsquerda(self):
        self.j -= 1

    def vaiBaixo(self):
        self.i -= 1

    def vaiCima(self):
        self.i+=1

    def podeDireita(self):
        return self.j < self.n -1 and not self.direita

    def podeBaixo(self):
        return self.i < self.n -1 and not self.baixo

    def podeEsquerda(self):
        return self.i == self.n -1 and not self.esquerda and self.j != 0

    def podeCima(self):
        return self.i > 0 and not self.cima

    def imprimeMatriz(self):
        for linha in self.matriz:
            print(" ".join(f"{valor:2}" for valor in linha))
            
    def inicia(self):
        while (not self.direita or not self.esquerda or not self.esquerda or not self.cima):
            self.matriz[self.i][self.j] = 1

            if self.podeDireita():
                self.vaiDireita()
            elif self.podeBaixo():
                self.direita = True
                self.vaiCima()
            elif self.podeEsquerda():
                self.baixo = True
                self.vaiEsquerda()
            elif self.podeCima():
                self.esquerda = True
                self.vaiBaixo()
            else:
                self.cima = True

        self.imprimeMatriz()


