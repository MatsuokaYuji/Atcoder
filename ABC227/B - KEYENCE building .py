













N = int(input())
S= list(map(int, input().split()))

s = set()
a = 1
b = 1

def kei(a,b):
    return 4*a*b + 3*a + 3*b 
y = 4*a*b + 3*a + 3*b 
s.add(y)

for i in range(1,300):
    for j in range(1,300):
        y = kei(i,j)
        s.add(y)
ans = 0

for i in S:
    if i not in s:
        ans+=1
# print(s)
print(ans)