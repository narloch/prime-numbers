from random import randint

class MillerRabin:
    def decompose(n):
        r = 0
        while n % 2 == 0:
            r += 1
            n = n >> 1
        return r, n

    def testPrime(n, k=200):
        # Known small prime numbers
        if n in (2,3):
            return True
        # No number smaller than 2 is prime
        if n < 2:
            return False
        # No even number other than 2 is prime
        if n % 2 == 0:
            return False

        # Write n as 2^r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
        r, d = MillerRabin.decompose(n - 1)

        # WitnessLoop: repeat k times:
        for _ in range(k):
            # Pick a random integer a in the range [2, n − 2]
            a = randint(2, n - 2)
            # x ← a^d mod n
            x = pow(a, d, n)
            # if x = 1 or x = n − 1 then continue WitnessLoop
            if x in (1, n - 1):
                continue
            try:
                # repeat r − 1 times:
                for _ in range(r - 1):
                    # x ← x^2 mod n
                    x = pow(x, 2, n)
                    # if x = n − 1 then continue WitnessLoop
                    if x == n - 1:
                        raise Exception()
            except Exception as e:
                continue

            return False
        return True