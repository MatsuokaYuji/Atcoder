



from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
    s = input()
    d[s]+=1
print(max(d, key=d.get))