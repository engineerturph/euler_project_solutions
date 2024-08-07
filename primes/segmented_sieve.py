import math

def simple_sieve(limit):
    """ Simple Sieve of Eratosthenes to find all primes up to `limit` """
    prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if prime[p]]

def segmented_sieve(n):
    """ Segmented Sieve of Eratosthenes to find all primes up to `n` """
    limit = int(math.sqrt(n)) + 1
    primes = simple_sieve(limit)
    low = limit
    high = 2 * limit

    while low < n:
        if high >= n:
            high = n
        
        mark = [True] * (high - low + 1)
        
        for prime in primes:
            # Find the minimum number in the current segment that is a multiple of prime
            lo_lim = max(prime * prime, low + (prime - low % prime) % prime)
            
            for j in range(lo_lim, high, prime):
                mark[j - low] = False

        
        print(high)
        
        low = low + limit
        high = high + limit

    return

n = 10**15
segmented_sieve(n)