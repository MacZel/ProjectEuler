from fractions import gcd

def lcm_of_list(min, max):
    list = range(min, max)
    lcm = list[0]
    for number in list:
        lcm = lcm * int(number/gcd(lcm, number))
    return lcm

print('Solution: ', lcm_of_list(11, 20), sep='', end='\n')
