
n = 10
obstaculo = -1
matriz = [[0 for _ in range(n)] for _ in range(n)]
direita = False
cima  = False
baixo = False
esquerda = False
i = 0
j = 0

matriz[0][4] = obstaculo
matriz[1][0] = obstaculo
matriz[1][3] = obstaculo
matriz[2][2] =obstaculo

pilha = []

def vaiDireita():
    global j
    j += 1

def vaiEsquerda():
    global j
    j -= 1

def vaiBaixo():
    global i
    i -= 1

def vaiCima():
    global i
    i+=1

def podeDireita():
    global j,n,obstaculo,i

    return j < n -1 and matriz[i][j+1] != obstaculo and matriz[i][j+1] !=2

def podeBaixo():
    global i,n,j,obstaculo

    return i < n -1 and matriz[i+1][j] !=obstaculo and matriz[i+1][j] !=2

def podeEsquerda():
    global j,obstaculo,i

    return j != 0 and matriz[i][j-1] != obstaculo and matriz[i][j-1] !=2

def podeCima():
    global i,cima,obstaculo

    return i > 0 and matriz[i-1][j] !=obstaculo and matriz[i-1][j] !=2

def pinta():
    global i,j
    posicao =  matriz[i][j]

    if posicao == 0 :
        matriz[i][j] = 1

while (True):
      pilha.append([i,j])
      pinta()
    

      if podeDireita():
        vaiDireita()
      elif podeBaixo() :
        vaiCima()
      elif podeEsquerda():
        vaiEsquerda()
      elif podeCima():
        vaiBaixo()

      if pilha

    
      

for linha in matriz:
    print(linha)



# Iterative DFS function
def dfs_iterative(tree, start):
    visited = set()  # Track visited nodes
    stack = [start]  # Stack for DFS

    while stack:  # Continue until stack is empty
        node = stack.pop()  # Pop a node from the stack
        if node not in visited:
            visited.add(node)  # Mark node as visited
            print(node)        # Print the current node (for illustration)
            stack.extend(reversed(tree[node]))  # Add child nodes to stack

# Run DFS starting from node 'A'
dfs_iterative(tree, 'A')