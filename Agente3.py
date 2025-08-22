
#Aqui precisa usar a busca em largura BFS
class Agente3:
    matriz = []
    movimentos = []
    parentesco = {}  
    n = 0
    i = 0
    j = 0
    obstaculo = -1
    inicio = (0,0)
    destino = (0,0)
    
    def __init__(self,n,obstaculo,inicio,destino):
        self.matriz =[[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.i,self.j = inicio
        self.inicio = inicio
        self.destino = destino
        self.obstaculo = obstaculo
        
    def addObstaculo(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            self.matriz[x][y] = self.obstaculo
            
    def vaiAtras(self):
        self.adicionaMovimento()
        self.j -= 1
        self.adicionaParentesco()
            
    def vaiFrente(self):
        self.adicionaMovimento()
        self.j += 1
        self.adicionaParentesco()
        
    def vaiDireita(self):
        self.adicionaMovimento()
        self.i += 1
        self.adicionaParentesco()
          
    def vaiEsquerda(self):
        self.adicionaMovimento()
        self.i -= 1
        self.adicionaParentesco()
        
    def adicionaMovimento(self):
        self.movimentos.append((self.i, self.j))
    
    def voltar(self):
        self.matriz[self.i][self.j] += 1
        if self.movimentos:
            self.i, self.j = self.movimentos.pop()
            
    def podeVoltar(self):
        return len(self.movimentos) > 0
    
    def podeFrente(self):
        return self.j < self.n - 1 and self.matriz[self.i][self.j + 1] == 0
    
    def podeAtras(self):
        return self.j > 0 and self.matriz[self.i][self.j - 1] == 0
    
    def podeDireita(self):
        return self.i < self.n - 1 and self.matriz[self.i + 1][self.j] == 0
    
    def podeEsquerda(self):
        return self.i > 0 and self.matriz[self.i - 1][self.j] == 0
    
    def imprimeMatriz(self):
        for linha in self.matriz:
            print(" ".join(f"{valor:2}" for valor in linha))
            
    def isDestino(self):
        return (self.i, self.j) == self.destino
    
    def adicionaParentesco(self):
        self.parentesco[(self.i, self.j)] = self.movimentos[-1] if self.movimentos else None
        
    def getCaminho(self):
        caminho = []
        atual = self.destino
        distancia = 0
        
        while atual != self.inicio:
            distancia +=1
            caminho.append(atual)
            atual = self.parentesco.get(atual)
            
        caminho.reverse()
        
        return (caminho,distancia)
            
    def inicia(self):
        self.adicionaMovimento()
        self.adicionaParentesco()
        
        while len(self.movimentos) > 0:
            if self.matriz[self.i][self.j] == 0:
                self.matriz[self.i][self.j] = 1
            
            if self.podeFrente():
                self.vaiFrente()
            elif self.podeDireita():
                self.vaiDireita()
            elif self.podeEsquerda():
                self.vaiEsquerda()
            elif self.podeAtras():
                self.vaiAtras()
            elif self.podeVoltar():
                self.voltar()
                
            if self.isDestino():
                print("Destino alcançado!")
                print(self.getCaminho())
                break
                
        self.imprimeMatriz()
        


