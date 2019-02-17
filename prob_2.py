def fibonacci(n):
    if n==1 or n ==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_sum(n):
    sum = 0       
    for i in range(1, 50):
        number = fibonacci(i)
        if number > n:
            return sum
        if number % 2 == 0 and number < n:
            sum += number
   
print('Solution: ', fibonacci_sum(4000000), sep='', end='\n')
