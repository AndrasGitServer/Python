# Calculate PI 
# Gregory_Leibniz series (mathematical infinite series)

# import the math library
import math

odd = 1 
pi  = 4/odd

print(pi, odd)

for odd in range(1, 10_000_000, 4) :
	odd += 2
	pi = pi - 4/odd
	print(pi, odd)
	odd += 2
	pi = pi + 4/odd
	print(pi, odd)

print('PI =', math.pi)


"""
4 CPUs	i7

3.1415928535897395 10000001
PI = 3.141592653589793

real	0m25.479s
user	0m9.690s
sys	0m8.411s

Precission -> 6 floats -> 3.141592

-----------------------------------

2 CPUs   Core2

3.1415928535897395 10000001
PI = 3.141592653589793

real    1m18.599s
user    0m43.557s
sys     0m29.131s

Precission -> 6 floats -> 3.141592

Core2 2.13 GHz takes 3x longer time  vs  4 CPUs i7 2.30 GHz

"""
