import matplotlib.pyplot as plt
import numpy as np

primes = [2, 3]
factors = []
num_of_factors = []


def get_primes(n):
    n = n // 2
    eliminate = set()
    for i in range(2, n):
        m = 2
        while i * m < n:
            eliminate.update([i * m])
            m += 1

    e_index = 0
    j = 4

    e_list = list(eliminate)


    while e_index < len(e_list):
        if j == e_list[e_index]:
            j += 1
            e_index += 1

        elif j != e_list[e_index] and j > e_list[e_index]:
            e_index += 1

        elif j < e_list[e_index]:
            primes.append(j)
            j += 1


def prime_factors(n, prime_index):
    q, r = divmod(n, primes[prime_index])
    
    if r == 0:
        factors.append(primes[prime_index])
        prime_factors(q, 0)

    elif r!= 0 and q > 2:
        prime_factors(n, prime_index + 1)

    elif r!=0 and q==1:
        factors.append(n)

    else:
        if n != 1:
            factors.append(n)


# n = 13954369

# print("Getting primes")
# get_primes(n)

# print("Beginning factorization")
# prime_factors(n, 0)
# print(factors)


m = 20000

get_primes(m)
for i in range(3, m+3):
    prime_factors(i, 0)
    num_of_factors.append(len(set(factors)))
    factors  = []



x = np.linspace(0, m, m)
y = []

for i in x:
    y.append(num_of_factors[int(i)-1])

fig, ax = plt.subplots()

ax.bar(x, y, linewidth=1.0)
plt.show()
