

















N = int(input())
S = input()
s = list(S)

for i in range(len(s)):
    if s[i] == "0":
        continue
    if i%2==0 :
        print("Takahashi")
        exit()
    else:
        print("Aoki")
        exit()
    