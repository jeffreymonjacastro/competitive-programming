import sys
import math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

MOD = 10**9 + 7
INF = float('inf')

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) // gcd(a, b)

def sieve(n):
  is_prime = [True] * (n + 1)
  is_prime[0] = is_prime[1] = False
  for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
      for j in range(i*i, n + 1, i):
        is_prime[j] = False
  return [i for i in range(2, n + 1) if is_prime[i]]

def factorial_mod(n, mod=MOD):
  result = 1
  for i in range(1, n + 1):
    result = (result * i) % mod
  return result

def solve():
  pass

def main():
  t = 1
  # t = int(input())
  for _ in range(t):
    solve()

if __name__ == "__main__":
  main()
