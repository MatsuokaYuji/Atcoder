







N = int(input())

S = input()
s =list(S)
if s.count("-")==0:
    print(-1)
    exit()

ans = 0
count=0
for i in range(N):
    x = s[i]
    if x=="-":
        if count >=1:
            count=0
    else:
        count+=1
    ans = max(ans,count)
if ans!=0:
    print(ans)
else:
    print(-1)

# N, S = input(), input()
# print(max(map(len, S.split('-'))) if 'o' in S and '-' in S else -1)


# ['o', 'oooo', '', '', 'o']

