class Xorshift:
    
    def __init__(self, seed):
        self.x = seed

    '''
    Utiliza x (que inicialmente é seed) para gerar um número pseudoaleatório utilizando shifts de bits.
    A atribuição do resultado a x ocorre para que a cada chamada o valor gerado seja diferente.
    '''
    def next(self):
        self.x ^= self.x << 13
        self.x ^= self.x >> 17
        self.x ^= self.x << 5

        return self.x