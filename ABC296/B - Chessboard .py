






import string

lowerAlpha = string.ascii_lowercase


S = [list(input()) for _ in range(8)]

L = ["a","b",]

L =[]
ans = ""
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            ans+=lowerAlpha[j]
            ans+=str(8-i)
            break
print(ans)
            
        