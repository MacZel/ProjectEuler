import math

def divisors_count(number):
    """works for numbers >= 5"""
    divisors_count = 0
    if number == 0:
        divisors_count = 0
    else:
        for n in range(1, int(math.sqrt(number)) + 1):
            if number % n == 0:
                divisors_count += 1
    return divisors_count * 2
             
def triangular_number(divisors_number):
    number = 0
    next_number = 1
    divisors_quant = 0
    while True:
        number += next_number
        next_number += 1
        divisors_quant = divisors_count(number)
        if divisors_quant >= divisors_number:
            return number, divisors_quant

print('Solution: triangle number: {}, divisors number: {}'.format(*triangular_number(500)), sep='', end='\n')
