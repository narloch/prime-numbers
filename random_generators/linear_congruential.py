class LCG():

    def __init__(self, seed, m, a, c):
        self.x = seed
        self.m = m
        self.a = a
        self.c = c

    def next(self):
        self.x = (self.x * self.a + self.c) % self.m
        return self.x

