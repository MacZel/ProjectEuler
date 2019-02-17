def sum_of_3_5_divs(n):
    sum = 0
    for number in range(1, n):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum
    
print('Solution: ', sum_of_3_5_divs(1000), sep='', end='\n')
