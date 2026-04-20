# Module 11 – Numerical Programming

## What you will learn
- Primality testing algorithms
- Brute-force vs optimised approaches
- Iterating efficiently with `range(start, stop, step)`
- Square-root optimisation: only check divisors up to `√n`
- Summing prime numbers up to a limit

## Files
| File | Topics covered |
|------|---------------|
| `testing primality/test.py` | Brute-force smallest-divisor, optimised `is_prime()` with `√n` bound, `sum_of_primes()` up to 1000 |

## Key concepts

### Brute-force primality check
```python
def is_prime_naive(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
```
Time complexity: **O(n)** — slow for large numbers.

### Optimised primality check (√n bound)
```python
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(n ** 0.5) + 1, 2):   # only odd divisors up to √n
        if n % d == 0:
            return False
    return True
```
Time complexity: **O(√n)** — much faster.

### Sum of all primes below 1000
```python
def sum_of_primes(limit=1000):
    return sum(n for n in range(2, limit) if is_prime(n))

print(sum_of_primes())   # 76127
```

### Using range() with a step
```python
# Odd numbers from 3 to 99
for n in range(3, 100, 2):
    print(n)
```

## Practice exercises
1. Write `is_prime(n)` from scratch and test it for `n = 2, 3, 4, 17, 18, 97`.
2. Find all prime numbers between 1 and 100 (the Sieve of Eratosthenes is a bonus challenge).
3. Find the largest prime number less than 10 000.
4. Sum all prime numbers between 1 and 1 000 000 and measure how long it takes.
