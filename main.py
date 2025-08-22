from Agente2 import Agente2
from Agente1 import Agente1
from Agente3 import Agente3

agente1 = Agente1(10, 2, 3)

# agente1.inicia()

agente2 = Agente2(10, 0, 0, -1)

agente2.addObstaculo(0, 4)
agente2.addObstaculo(1, 0)
agente2.addObstaculo(1, 3)
agente2.addObstaculo(2, 2)
agente2.addObstaculo(3, 2)
agente2.addObstaculo(3, 5)
agente2.addObstaculo(4, 1)
agente2.addObstaculo(4, 6)
agente2.addObstaculo(5, 3)
agente2.addObstaculo(5, 5)
agente2.addObstaculo(5, 6)
agente2.addObstaculo(5, 7)
agente2.addObstaculo(5, 8)
agente2.addObstaculo(6, 5)
agente2.addObstaculo(6, 8)
agente2.addObstaculo(7, 5)
agente2.addObstaculo(7, 8)
agente2.addObstaculo(8, 5)
agente2.addObstaculo(8, 7)
agente2.addObstaculo(8, 8)
agente2.addObstaculo(9, 5)

# agente2.inicia()

agente3 = Agente3(10, -1, (0,0), (3,1))

agente3.addObstaculo(0, 4)
agente3.addObstaculo(1, 0)
agente3.addObstaculo(1, 3)
agente3.addObstaculo(2, 2)
agente3.addObstaculo(3, 2)
agente3.addObstaculo(3, 5)
agente3.addObstaculo(4, 1)
agente3.addObstaculo(4, 6)
agente3.addObstaculo(5, 3)
agente3.addObstaculo(5, 5)
agente3.addObstaculo(5, 6)
agente3.addObstaculo(5, 7)
agente3.addObstaculo(5, 8)
agente3.addObstaculo(6, 5)
agente3.addObstaculo(6, 8)
agente3.addObstaculo(7, 5)
agente3.addObstaculo(7, 8)
agente3.addObstaculo(8, 5)
agente3.addObstaculo(8, 7)
agente3.addObstaculo(8, 8)
agente3.addObstaculo(9, 5)

agente3.inicia()