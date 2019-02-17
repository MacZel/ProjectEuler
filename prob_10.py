def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def sum_of_primes(limit):
	generator = primes_sieve(limit)
	sum = 0
	for prime in generator:
		sum += prime
	return sum

print('Solution: ', sum_of_primes(2000000), sep='', end='\n')
