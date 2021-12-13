from random import randint

class Fermat:
    def testPrime(n, k=200):
        # Known small prime numbers
        if n in (2, 3):
            return True
        # No number smaller than 2 is prime
        if n < 2:
            return False
        # No even number other than 2 is prime
        if n % 2 == 0:
            return False

        # Repeat k times:
        for _ in range(k):
            # Pick a randomly in the range [2, n − 2]
            a = randint(2, n - 2)
            # If a^(n-1) % n != 1, then return composite
            if pow(a, n - 1, n) != 1:
                return False
            # If composite is never returned: return probably prime
        return True