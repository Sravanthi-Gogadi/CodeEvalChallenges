def checkprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

count=0
num=2
primes=[]
while(count<1000):
    if checkprime(num):

        count=count+1
        primes.append(num)
    num = num + 1
print(sum(primes))
