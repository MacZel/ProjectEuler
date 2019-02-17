import math

def pythagorean_triple():
	for a in range(1, 1000):
		for b in range(2, 1000):
			c = math.sqrt(a**2 + b**2)
			if a + b + c == 1000:
				return a, b, int(c), int(a*b*c)
				
print('Solution: a: {}, b: {}, c: {}, a*b*c: {}'.format(*pythagorean_triple()))
