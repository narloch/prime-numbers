from random import randint

class MillerRabin:

    def miller_test(n, k=40):
        # Caso base: n < 3
        if n in (2,3):
            return True
        # Números menores que 2 não são primos
        if n < 2:
            return False
        # 2 é o único par primo
        if n % 2 == 0:
            return False

        # Computar d e r de forma que d*2^r = n-1
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        for _ in range(k):
            a = randint(2, n - 1)
            
            x = pow(a, d, n)

            if x == 1 or x == n - 1:
                continue
            
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            
            else:
                return False
        return True
        