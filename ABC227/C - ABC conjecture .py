





N = int(input())

ans = 0
for a in range(1,5*10**3):
    if a **3>N:
        break
    for b in range(a,N+1):
        if a*b*b > N:
            break
        ab = a*b
        c_min = b
        c_max = N//ab
        ans += c_max - c_min +1
print(ans)
