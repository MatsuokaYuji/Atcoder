





N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


from collections import Counter

a=Counter(A)
ans = 0

for x in C:
    y = x -1
    k = B[y]
    ans+=a[k]
print(ans)
