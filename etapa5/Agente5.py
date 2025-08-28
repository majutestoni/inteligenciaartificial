Ponto = tuple[int, int]

class Agente:
    matriz = []
    caminho = []
    n = 0
    i = 0
    j = 0
    
    inicio: Ponto = (0, 0)
    destino: Ponto = (0, 0)
    
    normal = 1
    areia = 2
    rocha = 3
    
    def __init__(self, n, inicio, destino):
        self.matriz = [[self.normal for _ in range(n)] for _ in range(n)]
        self.n = n
        self.i, self.j = inicio
        self.inicio = inicio
        self.destino = destino
        
    def addAreia(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            self.matriz[x][y] = self.areia
            
    def addRocha(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            self.matriz[x][y] = self.rocha 
    
    def pegaAdj(self,ponto) -> list[Ponto]:
        adj = []
        i,j = ponto
        if j < self.n -1:
            adj.append((i,j+1)) # direita
        if j > 0:
            adj.append((i,j-1)) # esquerda
        if i < self.n-1:
            adj.append((i+1,j)) # baixo
        if i > 0:
            adj.append((i-1,j)) # cima
        return adj
    
    def imprimeMatrizComCaminho(self):
        matriz_resp = [[str(self.matriz[i][j]) for j in range(self.n)] for i in range(self.n)]
        print(f"Caminho encontrado em {len(self.caminho)} etapas")
        for (i,j) in self.caminho:
            matriz_resp[i][j] = "X"
        for linha in matriz_resp:
            print(" ".join(f"{x:2}" for x in linha))

    def pegaAdjMinimo(self,adjs):
        min = adjs[0]

        for adj in adjs:
            i,j = adj
            min_i,min_j = min

            valor = self.matriz[i][j]
            valor_min = self.matriz[min_i][min_j]

            if valor < valor_min:
                min = adj

        return min

    def inicia(self):
        while True:
            ponto = (self.i,self.j)
            self.caminho.append(ponto)

            if ponto== self.destino:
                break

            self.matriz[self.i][self.j] += 1
            adjs = self.pegaAdj(ponto)
            min = self.pegaAdjMinimo(adjs)
            
            self.i,self.j = min

        self.imprimeMatrizComCaminho()

        
        
