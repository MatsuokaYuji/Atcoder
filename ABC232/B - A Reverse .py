







import string

#アルファベットの小文字のみの出力
d = string.ascii_lowercase

def change(alpha,x):
    result = (d.index(alpha) + x+1)%26 
    return d[result]



S = list(input())
T = list(input())
for i in range(1,27):
    ans = []
    for s in S:
        ans.append(change(s,i))
    if ans == T:
        print("Yes")
        exit()
print("No")


