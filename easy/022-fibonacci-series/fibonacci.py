'''
With recursion
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
print(fibonacci(n))

'''
   Without recursion
'''
x = [0,1,1]
n=int(input())
def fib(n):
    for i in range(20):
        x.append(x[-1] + x[-2])
    return x[n]
print(fib(n))
