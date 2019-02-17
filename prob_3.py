import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def biggest_prime_factor(dividend):
    min_limit = 2
    max_limit = int(dividend / 2)
    for quotient in range(min_limit, max_limit):
        if dividend % quotient == 0:
            divisor = int(dividend / quotient)
            if is_prime(divisor):
                return divisor
                
print('Solution: ', biggest_prime_factor(600851475143), sep='', end='\n')
