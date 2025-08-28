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
- 0 - não visitadass
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

### Etapa 4

 Foi verificado que no ambiente, há tipos de terrenos e cada um com seu custo:
 - normal = 1
 - arenoso = 2
 - rochoso = 3
 1. Com base nisso, a matriz que foi herdada de todos os agente anteriores passou por uma mudança, . onde caso espaço passou a ter um valor (vulgo custo)
 2. Próximo passo foi pensar em como o robo analisaria seu ambiente e definiria seu caminho, caso, ele teria de explorar seus vizinhos -> escolher o vertice de custo mais baixo -> repete o processo
 3. Assim, monta uma árvore de custo minimo


