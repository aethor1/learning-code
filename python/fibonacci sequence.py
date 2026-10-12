f = [ 1 , 1 ]

def fib(n):

    if n - 1 < len(f):
        return f[n - 1]


    else:
        q = fib(n-1) + fib(n-2)
        f.append(q)

    return q

print(fib(10))
print(f)





