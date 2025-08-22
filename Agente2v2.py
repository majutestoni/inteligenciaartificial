Ponto = tuple[int, int]

class Agente2v2:
    matriz = []
    n = 0
    i = 0
    j = 0
    obstaculo = -1
    inicio:Ponto = (0,0)
    
    
    def __init__(self,n,obstaculo,inicio,destino):
        self.matriz =[[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.i,self.j = inicio
        self.inicio = inicio
        self.obstaculo = obstaculo