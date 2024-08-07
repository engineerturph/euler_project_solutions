import sympy

def generate_primes_up_to(limit):
    """Generate primes up to a specified limit using sympy's primerange."""
    return list(sympy.primerange(2, limit))

def write_primes_to_file(primes, filename):
    """Write the list of primes to a text file, one prime per line."""
    with open(filename, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")

def main():
    limit = 10**9 # Limit set to 10^9
    primes = generate_primes_up_to(limit)
    write_primes_to_file(primes, f'primes_up_to_{limit}.txt')
    print(f"Primes up to {limit} have been written to primes_up_to_{limit}.txt")

if __name__ == "__main__":
    main()