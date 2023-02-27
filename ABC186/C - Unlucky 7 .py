










N = int(input())

s = set()
ans = 0
for i in range(1,N+1):
    x = str(i)
    flag = False
    for j in range(len(x)):
        if x[j]=="7":
            ans+=1
            flag = True
            break
    if flag == False:
        s.add(i)
# print(ans)

for i in s:
    i = format(i, 'o')
    x = str(i)
    flag = False
    for j in range(len(x)):
        if x[j]=="7":
            ans+=1
            flag = True
            break
print(N-ans)

