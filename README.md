# Inteligência Articial 

Repositório da Disciplina de Inteligência Articial da FURB 2025/2

### Alunos
- Micael Luan Conti
- Maju Testoni

### Professor
Maiko Rafael Spiess (Doutorado em Política Científica e Tecnológica)

## Etapas

### Etapa 1
1. Nosso 1° passo foi definir que o representaria o ambiente em uma matriz
2. Definir que andar um espaço cada vez, o seja, valor = 1
3. Escolher preferencia de direção = 1° Direita , 2° baixo, 3° esquerda e 4° cima
4. E setar que irá mudar a direção ao encontrar uma "parede" 
5. O fim deve ser ao chegar no que é a 1° posição da matriz

### Etapa 2
Na etapa 2 foi utilizado em alusão ao algoritmo de DFS (Busca em profundidade)

Aqui temos uma lista de movimentos, onde em cada rodada é adicionado o movimento do agente;

#### As posições possuem 3 estados:
- 0 - não visitadas
- 1 - encontrado
- 2 - totalmente visitado 

#### A cada rodada o seguinte ocorre:

1. A posição atual do agente é marcada como encontrada(1)
2. A posição atual é adicionada a lista de movimentos
3. É verificada a direção que o agente pode ir
4. O agente visita a posição
5. Quando não puder ir para nenhuma direção o agente volta
6. Ao voltar a célula é marcada como totalmente visitada
7. O movimento é retirado da lista de movimentos
8. Quando a lista de movimentos estiver vazia o agente para

### Etapa 3
Na etapa 3 foi utilizado em alusão ao algoritmo de BFS (Busca em largura) 

#### Aqui temos: 
- lista de parentesco
- lista de distancia
- fila posicoes

#### As posições possuem 3 estados:
- 0 - não visitadas
- 1 - encontrado
- 2 - totalmente visitado 

#### Antes de iniciar o loop:
1. A posicao inicial é adicionada a fila de posições
2. A posicao inicial é marcada como encontrada(1)
3. A distancia da posicao inicial é marcada como 0

#### A cada rodada do loop o seguinte ocorre:
1. A posicao p é retirada de fila
2. Para cara posicao a adjacente de p:
    1. a é adicionada a fila de posicoes
    2. a é marcada como encontrada
    3. p é marcado como pai de a
    4. a distancia de a é marcada como a distancia de p+1
    5. se a for igual ao destino o loop para
3. A posicao é marcada como totalmente visitada

### Etapa 4

 Foi verificado que no ambiente, há tipos de terrenos e cada um com seu custo:
 - normal = 1
 - arenoso = 2
 - rochoso = 3
 1. Com base nisso, a matriz que foi herdada de todos os agente anteriores passou psor uma mudança, . onde caso espaço passou a ter um valor (vulgo custo)
 2. Próximo passo foi pensar em como o robo analisaria seu ambiente e definiria seu caminho, caso, ele teria de explorar seus vizinhos -> escolher o vertice de custo mais baixo -> repete o processo
 3. Assim, monta uma árvore de custo minimo

### Etapa 5

Aqui temos uma lista de caminho

### Antes do loop:
Valores das pocisões podem ser:
 - normal = 1
 - arenoso = 2
 - rochoso = 3

#### A cada rodada do loop o seguinte ocorre:
1. A posicao p é adicionada ao caminho
2. se p = destino para o loop
3. marca o valor de p como p+1
4. pega os valores adjacentes
    1. Pega todos adjacentes
    2. Ordena os adjacentes com base na direção do destino
5. pega o adjcente com menor valor e seta como posicao p
