from functools import lru_cache

memo = {}

def fibonacci(n):
  if n in memo:
    return memo[n]
  elif n == 1:
    return 1
  elif n == 2:
    return 1

  memo[n - 1] = fibonacci(n - 1)
  memo[n - 2] = fibonacci(n - 2)
  return memo[n - 1] + memo[n - 2]

@lru_cache(maxsize = 1000)
def fibonacci2(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  return fibonacci2(n - 1) + fibonacci2(n - 2)

for i in range(1, 1001):
    print(fibonacci2(i))
