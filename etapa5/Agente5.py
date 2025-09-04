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

    def pegaDirecoes(self):
        i_destino, j_destino = self.destino

        direcoes = {
            'b': i_destino > self.i,
            'c': i_destino < self.i,
            'd': j_destino > self.j,
            'e': j_destino < self.j
        }

        return direcoes

    def ordenaAdj(self, adjs):
        modificada = []
        direcoes = self.pegaDirecoes()

        for i, j, v, d in adjs:
            if direcoes.get(d, False):
                v += 1
            modificada.append((i, j, v, d))

        modificada.sort(key=lambda adj: adj[2], reverse=True)
        return [(i, j) for i, j, v, d in modificada]
           
    def pegaAdj(self,ponto) -> list[Ponto]:
        adjs = []
        i,j = ponto

        if j < self.n -1:
            adjs.append((i,j+1, 0,'d')) # direita
        if j > 0:
            adjs.append((i,j-1, 0,'e')) # esquerda
        if i < self.n-1:
            adjs.append((i+1,j, 0,'b')) # baixo
        if i > 0:
            adjs.append((i-1,j, 0,'c')) # cima
        
        return self.ordenaAdj(adjs)
    
    def imprimeMatrizComCaminho(self):
        matriz_resp = [[str(self.matriz[i][j]) for j in range(self.n)] for i in range(self.n)]
        print(f"Caminho encontrado em {len(self.caminho) -1} etapas")
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

        
        
