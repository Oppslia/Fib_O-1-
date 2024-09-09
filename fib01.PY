def fib(fibs):
    a = 0
    b = 1
    c = None
    for x in range(fibs - 1): 
        c = b
        b = a
        a = b + c
    return a

print(fib(32))