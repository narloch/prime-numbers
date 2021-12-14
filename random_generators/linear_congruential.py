class LCG():

    def __init__(self, seed, m, a, c):
        self.x = seed
        self.m = m
        self.a = a
        self.c = c
    
    '''
    Utiliza x (que inicialmente é seed) para gerar um número pseudoaleatório através da fórmula abaixo.
    A atribuição do resultado a x ocorre para que a cada chamada o valor gerado seja diferente.
    '''
    def next(self):
        self.x = (self.x * self.a + self.c) % self.m
        return self.x

