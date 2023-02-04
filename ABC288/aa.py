





N = int(input())

ans = 0

for i in range(N):
    s = input()
    if s =="For":
        ans+=1
if N<2*ans:
    print("Yes")
else:
    print("No")