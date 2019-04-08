#recursion
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#optimization
def fib2(n):
    f1 = f2 = 1
    for k in range(1,n):
        f1, f2 = f2, f2 + f1
    return  f2
    

n = 10000
ff = fib2(n)
