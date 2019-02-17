def sum_of_squares(n):
    sum = 0
    for num in range(n+1):
        sum += num**2
    return sum
    
def square_of_sum(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return sum**2
    
def diff_sum_to_sq(n):
    return square_of_sum(n) - sum_of_squares(n)
    
print('Solution: ', diff_sum_to_sq(100), sep='', end='\n')
    