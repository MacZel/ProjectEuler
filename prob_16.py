def exponent_to_sum(exponent):
    exponent = list(str(2**1000))
    return sum([int(digit) for digit in exponent])

print('Solution: ', exponent_to_sum(1000), sep='', end='\n')
