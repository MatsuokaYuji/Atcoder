

k = input()

ans = -1

n = len(k)

for i in range(n):
    if k[i] =="a":
        ans = i+1

print(ans)