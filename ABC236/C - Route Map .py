
N,M = map(int,input().split())


S = input().split()
# print(S)
T = input().split()
T = set(T)
for i in S:
    if i in T:
        print("Yes")
    else:
        print("No")
