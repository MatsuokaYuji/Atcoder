




N = int(input())

A = list(map(int, input().split()))
from collections import Counter

S=Counter(A)
print(len(S))