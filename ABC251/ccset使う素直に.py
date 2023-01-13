

N = int(input())


existString = set()

## オリジナル管理
A = [("",0,0)]

for i in range(1,N+1):
    S,T = input().split()
    t = int(T)
    if S  in existString:
        continue
    else:
        existString.add(S)
        A.append((S,i,t))
# [('', 0, 0), ('aaa', 0, 9), ('bbb', 1, 10), ('ccc', 2, 10), ('ddd', 3, 10)]

maxNum = 0
for list in A:
    if list[2] >= maxNum:
        maxNum = list[2]
for list in A:
    if list[2] == maxNum:
        print(list[1])
        exit()
