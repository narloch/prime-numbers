from random import randint

class Fermat:
    def fermat_test(n, k=40):
        # Caso base: n < 3
        if n in (2,3):
            return True
        # Números menores que 2 não são primos
        if n < 2:
            return False
        # 2 é o único par primo
        if n % 2 == 0:
            return False

        for _ in range(k):
            a = randint(2, n - 2)
            if pow(a, n - 1, n) != 1:
                return False

        return True
