










S = list(input())
T = list(input())

l=len(S)
if S ==T:
    print("Yes")
    exit()

for i in range(l-1):
    S[i],S[i+1] = S[i+1],S[i]
    if S ==T:
        print("Yes")
        exit()
    S[i+1],S[i] = S[i],S[i+1]
print("No")

