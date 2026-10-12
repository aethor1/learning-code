import math

factorize=139
primeFactors = []
primeList = [2, 3]


def get_primes(n):
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
            primeList.append(j)
            j += 1




def prime(n, i):
    print(i, len(primeList))
    q, r = divmod(n, primeList[i])

    if r == 0 and q != 1:
        primeFactors.append(primeList[i])
        prime(q, i)

    elif r == 0 and q == 1:
        primeFactors.append(n)
    
    elif r != 0:
        i += 1
        prime(n, i)



get_primes(factorize)
prime(factorize,0)

print(primeFactors)












# primeCount = 0x

# for i in range(1,factorize):
#     if ((factorize % i) == 0):
#         i = primeCount+1


# if ((100%2)==0):
#     primeCount+=1
#     if ((100/2)%2)==0:
#         primeCount+=1


    








# print(primeCount)
#for i in range(1,1000):
#    if ((factorize % i) == 0):
#        primeFactors.append(i)

# the above just prints its factors not prime factors


#have to make a list of primes first


#failed attempt

# s = 10
# primeChk = range(2, s + 1)

# for prime in primeChk:
#     if ((primeChk % prime) == 0):
#         print(f"NOT PRIME--{prime}")
#     elif ((primeChk % prime) != 0):
#         print(f"PRIME--{prime}")
        
# retry

    
