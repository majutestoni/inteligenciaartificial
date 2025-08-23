Ponto = tuple[int, int]

class Agente4:
    matriz = []
    n = 0
    i = 0
    j = 0
    
    inicio: Ponto = (0, 0)
    destino: Ponto = (0, 0)
    
    normal = 1
    areia = 2
    rocha = 3
    
    distancia: dict[Ponto,int]
    nao_visitados: set[Ponto]
    anterior: dict[Ponto,Ponto]
    
    def __init__(self, n, inicio, destino):
        self.matriz = [[self.normal for _ in range(n)] for _ in range(n)]
        self.n = n
        self.i, self.j = inicio
        self.inicio = inicio
        self.destino = destino
        
        self.distancia = { (i,j): float("inf") for i in range(n) for j in range(n) }
        self.nao_visitados = { (i,j) for i in range(n) for j in range(n) }
        self.anterior = {}
        self.distancia[inicio] = 0
        
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
    
    def menorDistancia(self):
        return min(self.nao_visitados, key=lambda v: self.distancia[v])
    
    def dijkstra(self):
        while self.nao_visitados:
            v = self.menorDistancia()
            self.nao_visitados.remove(v)
            
            if v == self.destino:
                break
            
            for vizinho in self.pegaAdj(v):
                if vizinho in self.nao_visitados:
                    i, j = vizinho
                    alt = self.distancia[v] + self.matriz[i][j]
                    if alt < self.distancia[vizinho]:
                        self.distancia[vizinho] = alt
                        self.anterior[vizinho] = v
        return self.distancia[self.destino]
    
    def reconstruir_caminho(self):
        caminho = []
        v = self.destino
        while v in self.anterior or v == self.inicio:
            caminho.append(v)
            if v == self.inicio:
                break
            v = self.anterior[v]
        caminho.reverse()
        return caminho
    
    def imprimeMatrizComCaminho(self, caminho):
        matriz_resp = [[str(self.matriz[i][j]) for j in range(self.n)] for i in range(self.n)]
        for (i,j) in caminho:
            matriz_resp[i][j] = "X"
        for linha in matriz_resp:
            print(" ".join(linha))
    
    def inicia(self):
        print("======= Matriz inicial =======")
        for linha in self.matriz:
            print(" ".join(str(x) for x in linha))
        
        menor_custo = self.dijkstra()
        caminho = self.reconstruir_caminho()
        
        print("\n======= Caminho encontrado =======")
        print(f"Menor custo de {self.inicio} até {self.destino}: {menor_custo}")
        self.imprimeMatrizComCaminho(caminho)
