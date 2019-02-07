'''
"Every composite number has a factor less than or equal to its squareroot"
'''
def primepalindrome(given):
    # Initialize a list
    primes = []
    for i in range(2, given + 1):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(i ** 0.5) + 1):
            if i % num == 0:
                isPrime = False
                break
        if isPrime and str(i) == str(i)[::-1]:
            primes.append(i)

    return (primes[-1])
print(primepalindrome(1000))

