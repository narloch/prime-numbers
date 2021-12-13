class Xorshift:
    
    def __init__(self, seed):
        self.x = seed

    def next(self):
        self.x ^= self.x << 13
        self.x ^= self.x >> 17
        self.x ^= self.x << 5

        return self.x