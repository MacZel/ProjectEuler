import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
    
def find_n_prime(n):
    i = 1
    number = 2
    while i != n:
        number += 1
        if is_prime(number):
            i += 1
    return number

print('Solution: ', find_n_prime(10001), sep='', end='\n')
