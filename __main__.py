import time
from random_generators.linear_congruential import LCG
from random_generators.xorshift import Xorshift
from prime_verification.miller_rabin import MillerRabin
from prime_verification.fermat import Fermat

# Para a semente, utilizei o tempo do processador em ns
SEED = time.process_time_ns()

# Utilizei uma das configurações recomendadas para o LCG, porém é possível utilizar outras configurações
M = (2**31)-1
A = 16807
C = 0

BIT_SIZE = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

'''
Função para imprimir os números aleatórios dos dois algoritmos, utiliza uma chamada iterativa do LCG ou Xorshift
seguida de uma união do bit menos significativo da saída do algoritmo com o número anterior shiftado em uma vez.
Foi a forma que encontrei de imprimir números com tamanhos específicos.
'''
def random_numbers():
    print("%%%%%%%% RANDOM NUMBERS %%%%%%%%\n")

    print("Linear congruential generator\n")
    for bit_size in BIT_SIZE:
        start_time = time.process_time_ns()
        lcg = LCG(SEED, M, A, C)

        random_num = 0
        for _ in range(bit_size):
            random_num = (random_num << 1) | (lcg.next() & 1)
        
        end_time = time.process_time_ns()
        elapsed_time = end_time - start_time
    
        print("{} | {} | {} ns\n".format(random_num.bit_length(), random_num, elapsed_time))

    print("Xorshift\n")
    for bit_size in BIT_SIZE:
        start_time = time.process_time_ns()
        xorshift = Xorshift(SEED)
        
        random_num = 0
        for _ in range(bit_size):
            random_num = (random_num << 1) | (xorshift.next() & 1)
        
        end_time = time.process_time_ns()
        elapsed_time = end_time - start_time

        print("{} | {} | {} ns\n".format(random_num.bit_length(), random_num, elapsed_time))

'''
Praticamente igual a random_numbers, mas agora utiliza o teste de Miller-Rabin para verificar se os números gerados são primos.
Caso não seja, gera-se um novo número até obter uma saída desejada.
É possível generalizar os dois métodos de forma que não sejam tão repetitivos, mas fiquei sem tempo :(
'''
def random_prime_numbers():
    print("%%%%%%%% RANDOM PRIME NUMBERS %%%%%%%%\n")

    print("Linear congruential generator\n")
    for bit_size in BIT_SIZE:
        start_time = time.process_time_ns()
        lcg = LCG(SEED, M, A, C)

        random_num = 0
        while not MillerRabin.miller_test(random_num):
            random_num = 0
            for _ in range(bit_size):
                random_num = (random_num << 1) | (lcg.next() & 1)
        
        end_time = time.process_time_ns()
        elapsed_time = end_time - start_time
    
        print("{} | {} | {} ns\n".format(random_num.bit_length(), random_num, elapsed_time))

    print("Xorshift\n")
    for bit_size in BIT_SIZE:
        start_time = time.process_time_ns()
        xorshift = Xorshift(SEED)
        
        random_num = 0
        while not MillerRabin.miller_test(random_num):
            random_num = 0
            for _ in range(bit_size):
                random_num = (random_num << 1) | (xorshift.next() & 1)
            
        end_time = time.process_time_ns()
        elapsed_time = end_time - start_time

        print("{} | {} | {} ns\n".format(random_num.bit_length(), random_num, elapsed_time))

def main():
    random_numbers()
    random_prime_numbers()

if __name__ == "__main__":
    main()
