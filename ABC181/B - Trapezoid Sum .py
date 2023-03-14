








N = int(input())
ans = 0

for i in range(N):
    A,B = map(int,input().split())
    n = B-A+1
    # Aまでの和
    s1 = (1/2) * (A-1) *A
    # Bまでの和
    s2 = (1/2) * (B) *(B+1)
    tmp = s2-s1
    ans+=tmp
print(int(ans))
