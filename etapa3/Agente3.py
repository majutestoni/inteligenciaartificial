
#Aqui precisa usar a busca em largura BFS
Ponto = tuple[int, int]

class Agente:
    matriz = []
    n = 0
    i = 0
    j = 0
    obstaculo = -1
    
    inicio:Ponto = (0,0)
    destino:Ponto = (0,0)
    
    parentesco: dict[Ponto,Ponto] = {}
    distancia: dict[Ponto,int] = {}
    fila: list[Ponto] = []
    
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
        
    def imprimeMatriz(self):
        for linha in self.matriz:
            print(" ".join(f"{valor:2}" for valor in linha))
            
    def getCaminho(self,p):
        v = p
        c = []
        
        while v is not None:
            c.append(v)
            if v in self.parentesco:
                v = self.parentesco[v]
            else:
                v = None
                
        return c
    
    def imprimeMatrizComCaminho(self, caminho):
        matriz_resp = [[str(self.matriz[i][j]) for j in range(self.n)] for i in range(self.n)]
        for (i,j) in caminho:
            matriz_resp[i][j] = "X"
        for linha in matriz_resp:
            print(" ".join(f"{x:2}" for x in linha))

    def imprimeDestino(self):
        if self.destino not in self.distancia:
            print("Não foi possível chegar no destino")
            return
        
        distancia = self.distancia.get(self.destino)

        print("======= Caminho encontrado ======= ")
        print(f"Menor custo de {self.inicio} até {self.destino}: {distancia}")
        caminho = self.getCaminho(self.destino)
        self.imprimeMatrizComCaminho(caminho)
            
    def pegaAdj(self,ponto) -> list[Ponto]:
        adj = []
        i,j = ponto
        
        if j < self.n -1:
            adj.append((i,j+1)) #direita
        if j > 0:
            adj.append((i,j-1)) #esquerda
        if i < self.n-1:
            adj.append((i+1,j)) #baixo
        if i > 0:
            adj.append((i-1,j)) #cima
        
        return adj
            
    def inicia(self):
        self.fila.append(self.inicio)
        self.distancia[self.inicio] = 0
        i,j = self.inicio
        self.matriz[i][j] = 1
        achou = False
        
        while len(self.fila) > 0 and not achou:
            
            v = self.fila.pop(0)
            i,j = v
            
            for p in self.pegaAdj(v):
                i,j = p
                
                if self.matriz[i][j] == 0:
                    self.fila.append(p)
                    self.matriz[i][j] = 1
                    self.parentesco[p] = v
                    self.distancia[p] = self.distancia[v] + 1
                    
                    if p == self.destino:
                        achou = True
                        break
                    
            self.matriz[i][j] = 2
            
        self.imprimeDestino()
     
                
  
        
        


