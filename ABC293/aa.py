





S = input()

s = list(S)
# print(s)
l = len(s)
ans = []
for i in range(l//2):
    x = s[2*i]
    y = s[2*i+1]
    ans.append(y)
    ans.append(x)
print("".join(ans))    



# S=input()
# print(S)