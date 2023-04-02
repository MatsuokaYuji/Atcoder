



N = int(input())
S = input()

s = list(S)
x = s[0]

for i in range(N-1):
    # print(x)
    if x==s[i+1]:
        print("No")
        exit()
    x =s[i+1]
print("Yes")
